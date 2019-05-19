
import os
import psycopg2
import requests
from util import checkBookProperties, prepareResponseListOfBooks, create_session, prepareWishList
from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from dotenv import load_dotenv
load_dotenv()


db_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_URL


db = SQLAlchemy(app)


manual_session = create_session(app.config)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(200), unique=False, nullable=True)
    title = db.Column(db.String(100), unique=False, nullable=True)
    numpages = db.Column(db.Integer, unique=False, nullable=True)
    author = db.Column(db.Text, unique=False, nullable=True)
    publishdate = db.Column(db.String(100), unique=False, nullable=True)


@app.route('/')
def index():
    return 'Working! Head on over to /api'


@app.route('/api/books')
def getBookSearchData():
    try:
        title = request.args.get('title')
        response = requests.get(
            f'http://openlibrary.org/search.json?q={title}')
        jsonResponseObj = response.json()
        bookList = prepareResponseListOfBooks(jsonResponseObj)
        return jsonify(Books=bookList)
    except requests.exceptions.RequestException as e:
        return jsonify({'debug': e}), 404


@app.route('/api/book/<isbn>')
def getBookData(isbn):
    response = requests.get(
        f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json')
    return jsonify(response.json())


@app.route('/api/wishlist')
def getWishList():
    query = Book.query.all()
    lst = []
    for book in query:
        lst.append({'title': book.title, 'id:': book.id, 'isbn': book.isbn,
                    'publish_date': book.publishdate, 'num_pages': book.numpages})
    return jsonify(myWishlist=lst), 200


@app.route('/api/wishlist/<isbn>', methods=['DELETE'])
def removeFromWishlist(isbn):
    exisit = manual_session.query(Book) \
        .filter(Book.id == isbn).delete()
    if(exisit == 0):  # DoesNotExisit
        return jsonify({'message': f'Book does not exisit in collection'}), 200
    manual_session.commit()
    return jsonify({'message': f'Deleted {isbn}.'}), 200


@app.route('/api/wishlist/<isbn>', methods=['POST'])
def addToWishlist(isbn):
    try:
        response = requests.get(f'http://127.0.0.1:5000/api/book/{isbn}')
        id = f'ISBN:{isbn}'
        bookData = prepareWishList(response.json(), id)
        print(f'book Data => {bookData}')
        book = Book(
            isbn=isbn,
            title=bookData[0]["title"],
            author=bookData[0]["authors"],
            numpages=bookData[0]["number_of_pages"],
            publishdate=bookData[0]["publish_date"]

        )
        manual_session.add(book)
        manual_session.commit()
        return jsonify({'message': 'New book successfully added to WishList.'}), 201
    except IntegrityError:
        manual_session.rollback()
        return jsonify({'error': '400', 'debug': ' This may exisit in the DB already'}), 400
