import unittest
from app import app, db, Booking

class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_submit_booking(self):
        response = self.app.post('/submit-booking', data=dict(
            name='John Doe',
            email='john@example.com',
            therapy='individual',
            about='I need help with anxiety',
            reason='I want to improve my mental health'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Booking submitted successfully', response.data)

        # Check if booking is stored in the database
        booking = Booking.query.filter_by(email='john@example.com').first()
        self.assertIsNotNone(booking)
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.therapy, 'individual')

if __name__ == '__main__':
    unittest.main()