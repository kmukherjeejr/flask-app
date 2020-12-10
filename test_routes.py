import unittest

from app import app


class BasicTestCase(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        tester = app.test_client(self)
        response = tester.get('/about-us', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contactus(self):
        tester = app.test_client(self)
        response = tester.get('/contact-us', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contacted(self):
        data = {
            'name': 'John Doe',
            'phone': '9876543210',
            'email': 'john.doe@example.com'
        }
        tester = app.test_client(self)
        response = tester.get('/contact-details', data=data, content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()