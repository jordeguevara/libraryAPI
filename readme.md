Case:
1.Create an API that allows users to search for books using the open library API
2.get details about a specific book
3.Added feature we would also like to have a global “wish list”
a)where we can add
b)remove books
c) view books that are in the wish list.

Requirements:
a) APIs should be RESTful and use the HTTP methods appropriately.
b) You’re using Open Library as a third-party client to search and get details of books.
c) You’re building a “wish list” feature as an added feature in the API
d) Design the API endpoints as you see fit but provide clear documentation on how we can
use them.
e) Use any data store you prefer for the wish list functionality (examples can be Postgres,
SQLite, Elasticsearch, etc.), just make sure there’s a way for us to use it (whether it’s a
built in DB or an online one).

Technologies used: Flask, SQLite

Getting Started

Building Application
Create Environment
`mkdir OpenLibAPI cd OpenLibAPI python3 -m venv venv`
Activate the enviroment
`. venv/bin/activate`

Installing the Database (Postgres)
`pip install Flask-SQLAlchemy`
`pip install Flask-Migrate`
`pip install marshmallow`
`pip install marshmallow-sqlalchemy`
`pip install Flask-Marshmallow`
`pip install psycopg2`
Documentation:

GET api/book?title=<InsertBookTile>
