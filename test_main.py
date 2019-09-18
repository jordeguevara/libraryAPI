from app import app
import unittest
from util import formatAuthors


testBookData = {
    "title": "Data structures",
    "ISBN": "9780131990432"
}


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Check if retrieving search data is working correctly
    def test_books(self):
        tester = app.test_client(self)

        response = tester.get('/api/books', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Check if getting an individual is working correctly
    def test_book(self):
        tester = app.test_client(self)
        url = '/api/book/9780131990432'
        response = tester.get(url, content_type='application/json')
        expected = b'{"ISBN:9780131990432":{"authors":[{"name":"Jeffrey Esakov","url":"https://openlibrary.org/authors/OL952972A/Jeffrey_Esakov"}],"by_statement":"Jeffrey Esakov, Tom  Weiss.","identifiers":{"isbn_10":["0131990438"],"openlibrary":["OL17141271M"]},"key":"/books/OL17141271M","notes":"Bibliography: p361-366 - Includes index.","number_of_pages":372,"pagination":"xi, 372p. ;","publish_date":"1988","publish_places":[{"name":"London"}],"publishers":[{"name":"Prentice-Hall International"}],"subjects":[{"name":"In library","url":"https://openlibrary.org/subjects/in_library"},{"name":"Data structures (Computer science)","url":"https://openlibrary.org/subjects/data_structures_(computer_science)"},{"name":"C (Computer program language)","url":"https://openlibrary.org/subjects/c_(computer_program_language)"}],"subtitle":"an advanced approach using C","title":"Data structures","url":"https://openlibrary.org/books/OL17141271M/Data_structures"}}\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,expected)

    # Check if retrieving wishlist collection data is working correctly
    def test_wishlist(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/wishlist', content_type='application/json')
        expectedWishList = b'{"myWishlist":[{"author":"J. R. R. Tolkien","id":7,"isbn":"8020409262","num_pages":-1,"publish_date":"2001","title":"P\\u00e1n prsten\\u016f: Spole\\u010dentvo prstenu"},{"author":"J. R. R. Tolkien","id":8,"isbn":"8020409262","num_pages":-1,"publish_date":"2001","title":"P\\u00e1n prsten\\u016f: Spole\\u010dentvo prstenu"},{"author":"J. R. R. Tolkien","id":9,"isbn":"8020409262","num_pages":-1,"publish_date":"2001","title":"P\\u00e1n prsten\\u016f: Spole\\u010dentvo prstenu"}]}\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,expectedWishList)



    def test_formatAuthor(self):
        authors = [
            {
                "name": "Jorde G",
            },
            {
                "name": "Moe P.",
            }
        ]

        correctFormat = "Jorde G Moe P. "
        authorsFormatted = formatAuthors(authors)
        self.assertEqual(authorsFormatted, correctFormat)


if __name__ == '__main__':
    unittest.main()
