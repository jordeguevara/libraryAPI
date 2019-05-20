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
        response = tester.get(
            f'/api/book/{testBookData["ISBN"]}', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Check if retrieving wishlist collection data is working correctly
    def test_wishlist(self):
        tester = app.test_client(self)
        response = tester.get(
            f'/api/wishlist', content_type='application/json')
        self.assertEqual(response.status_code, 200)

     # Check if posting to wishlist is working properly
     # TO DO: create mock
    # def test_postToWishlist(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/api/wishlist/9780751321036')
    #     self.assertEqual(response.status_code, 201)

    def test_formatAuthor(self):
        tester = app.test_client(self)
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
