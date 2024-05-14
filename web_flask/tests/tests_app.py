import unittest
import sys
sys.path.append('../web_flask')  # Add the web_flask directory to sys.path
from app import app, db, Booking


class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()

        # Establish application context and create database tables
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        # Remove database session
        db.session.remove()

        # Drop all tables
        db.drop_all()

        # Pop application context
        self.ctx.pop()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_services(self):
        response = self.app.get('/services')
        self.assertEqual(response.status_code, 200)

    def test_submit_booking(self):
        response = self.app.post('/submit-booking', data=dict(
            name='John Doe',
            email='john@example.com',
            age=30,
            gender='male',
            therapy='individual',
            about='I need help with anxiety',
            reason='I want to improve my mental health'
        ), follow_redirects=False)
        self.assertEqual(response.status_code, 302)  # 302: Redirect status code

        # Check if booking is stored in the database
        booking = Booking.query.filter_by(email='john@example.com').first()
        self.assertIsNotNone(booking)
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.age, 30)  # Check age field
        self.assertEqual(booking.gender, 'male')  # Check gender field
        self.assertEqual(booking.therapy, 'individual')


if __name__ == '__main__':
    unittest.main()