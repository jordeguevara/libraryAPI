Case:

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

Getting Started

Building Application
Create Environment

---

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

```sh
GET api/wishlist
```

<b>Body</b>

```sh

```

```sh
POST api/wishlist/<ISBN>
```

<b>Body</b>

```sh

```

```sh
DELETE api/wishlist/<ISBN>
```

<b>Body</b>

```sh

```
