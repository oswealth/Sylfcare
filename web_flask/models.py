from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)  # Add age field
    gender = db.Column(db.String(10), nullable=False)  # Add gender field
    therapy = db.Column(db.String(50), nullable=False)
    about = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Booking(name={self.name}, email={self.email}, therapy={self.therapy})"