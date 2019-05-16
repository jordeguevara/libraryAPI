
import psycopg2
import requests
from util import checkBookProperties, prepareResponseListOfBooks, create_session
from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wishlist'
db = SQLAlchemy(app)

manual_session = create_session(app.config)

test = ' add some test'


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=True)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(200), primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=True)


@app.route('/')
def index():
    return 'Working! Head on over to /api'


@app.route('/api/books')
def getBookSearchData():
    title = request.args.get('title')
    response = requests.get(
        f'http://openlibrary.org/search.json?q={title}')
    jsonResponseObj = response.json()
    bookList = prepareResponseListOfBooks(jsonResponseObj)
    return jsonify(Books=bookList)


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
    manual_session.query(Book) \
        .filter(Book.id == isbn).delete()
    manual_session.commit()
    return jsonify({'message': f'Delete {isbn}.'}), 200


@app.route('/api/wishlist/<isbn>', methods=['POST'])
def addToWishlist(isbn):
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


# TO DO implement WishList
# @app.route('/create_student', methods=["POST"])
# def create_student():
#     dict_body = request.get_json()  # convert body to dictionary
#     print(dict_body)  # have a look at what is coming in
#     student = Student(id=dict_body["id"], first_name=dict_body['first_name'])
#     manual_session.add(student)
#     manual_session.commit()
#     return jsonify({'message': 'New student successfully created.'}), 201
# GET DELETE ROUTES --done
# TO DO sync up database ---done
# Easiest DB POSTGRES/ SQLite? --done psql
# TO DO Deep Dive into Documentation
# Integrate Building info, POSTMAN, RESPONSE, REQUEST like Stripe
# TO DO Add testing to end points
# Add a few test to endpoints
# TO DO Add Error handling
# DONE
