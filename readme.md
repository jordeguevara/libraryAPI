# Case:

1. Create an API that allows users to search for books using the open library API

2. Get details about a specific book

3. Added feature we would also like to have a global “wish list”

- where we can add

- remove books

- view books that are in the wish list.

Requirements:

a) APIs should be RESTful and use the HTTP methods appropriately.

b) You’re using Open Library as a third-party client to search and get details of books.

c) You’re building a “wish list” feature as an added feature in the API

d) Design the API endpoints as you see fit but provide clear documentation on how we can
use them.

e) Use any data store you prefer for the wish list functionality (examples can be Postgres,
SQLite, Elasticsearch, etc.), just make sure there’s a way for us to use it (whether it’s a
built in DB or an online one).

Technologies used: Flask, postgres

# Getting Started

In order for application to run, please install <b>python3</b> and <b>postgres</b> on your computer

<b>Building Application</b>

1)Clone repo

```
git clone https://github.com/jordeguevara/librayAPI.git
```

Then make your way into project directory

```
cd librayAPI
```

2)Create virtual Environment

---

`python3 -m venv venv`

Activate the enviroment

`. venv/bin/activate`

## on Windows

```
py -3 -m venv venv
\Python27\Scripts\virtualenv.exe venv
```

3. Install Depedencies

```sh
pip install Flask
pip install os psycopg2 requests python-dotenv
```

Installing the Database (Postgres)

```pip install Flask-SQLAlchemy

pip install psycopg2
```

<b>PSQL</b>

open up terminal and start PSQL by

```
psql -U postgres
```

create books table

```
CREATE TABLE books (id serial PRIMARY KEY, isbn varchar(100), title varchar(100), numpages integer, author varchar(100), publishdate varchar(100));
```

run tests

```
python3 test.py -v
```

## Documentation:

<i>Retrieves single book data based on IBSN </i>

```sh
GET api/book/<ISBN>
```

<b>Body</b>

```sh
{
  "ISBN:9780321585448": {
    "authors": [
      {
        "name": "Toby Donaldson",
        "url": "https://openlibrary.org/authors/OL6691858A/Toby_Donaldson"
      }
    ],
    "by_statement": "Toby Donaldson.",
    "classifications": {
      "lc_classifications": [
        "QA76.73.P98 F44 2009"
      ]
    },
    "identifiers": {
      "goodreads": [
        "6113209"
      ],
      "isbn_10": [
        "0321585445"
      ],
      "isbn_13": [
        "9780321585448"
      ],
      "lccn": [
        "2009419509"
      ],
      "librarything": [
        "7010486"
      ],
      "openlibrary": [
        "OL23556899M"
      ]
    },
    "key": "/books/OL23556899M",
    "notes": "Rev. ed. of: Pyton / Chris Fehily. c2002.\n\nIncludes index.",
    "number_of_pages": 185,
    "pagination": "vi, 185 p. :",
    "publish_date": "2009",
    "publish_places": [
      {
        "name": "Berkeley, CA"
      }
    ],
    "publishers": [
      {
        "name": "Peachpit Press"
      }
    ],
    "subjects": [
      {
        "name": "Internet Archive Wishlist",
        "url": "https://openlibrary.org/subjects/internet_archive_wishlist"
      }
    ],
    "title": "Python",
    "url": "https://openlibrary.org/books/OL23556899M/Python"
  }
}
```

<i>Using third party Open Library API, it returns JSON from a search endpoint based on query params </i>

```sh
GET api/books?title=<InsertBookTile>
```

<b>Body</b>

```sh
{
  "Books": [
    {
      "ISBN": [
        "9780321585448",
        "0321585445"
      ],
      "author": [
        "Toby Donaldson"
      ],
      "bookTitle": "Python",
      "publish_year": 2009
    },
    {
      "ISBN": [
        "1567661807",
        "9781567661804"
      ],
      "author": [
        "Don Patton"
      ],
      "bookTitle": "Pythons",
      "publish_year": 1996
    }
    ...
```

<i>Retrieve collection of books in Wishlist </i>

```sh
GET api/wishlist
```

<i>Retreive books in wishlist ollection</i>

<b>Body</b>

```sh
{
  "myWishlist": [
    {
      "author": "J. R. R. Tolkien",
      "id": 7,
      "isbn": "8020409262",
      "num_pages": -1,
      "publish_date": "2001",
      "title": "Pán prstenů: Společentvo prstenu"
    }
  ]
}
```

<i>Adds to a collection of books in Wishlist passing in ISBN in URL route</i>

```sh
POST api/wishlist/<ISBN>
```

<b>Body</b>
<i> Success <i>

```sh
{
  "message": "New book successfully added to WishList."
}
```

<i> negative # of pages indicates it was not present from OpenLib </i>

<i>removes from a collection of books in Wishlist by passing in ISBN in URL route</i>

```sh
DELETE api/wishlist/<id>
```

<b>Body</b>

<i>No Book Exisits</i>

```sh
{
  "message": "Book does not exisit in collection"
}
```

<i>Success</i>

```
{
    "message": "Deleted book from  wishlist collection."
}
```

<b>Postman Doc. </b>

https://documenter.getpostman.com/view/5049741/S1M3v5Uc?version=latest
