
import psycopg2
import requests
from util import checkBookProperties, prepareResponseListOfBooks, create_session
from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wishlist'
db = SQLAlchemy(app)

manual_session = create_session(app.config)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(200), primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=True)


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
        print(e)


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
        lst.append({'title': book.title, 'id:': book.id})
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
        bookData = response.json()
        id = f'ISBN:{isbn}'
        book = Book(
            id=isbn,
            title=bookData[id]["title"]
        )
        manual_session.add(book)
        manual_session.commit()
        return jsonify({'message': 'New book successfully added to WishList.'}), 201
    except IntegrityError:
        manual_session.rollback()
        return jsonify({'error': '400', 'debug': ' This may exisit in the DB already'}), 400
