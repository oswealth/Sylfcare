from flask import Flask, render_template, request, redirect, url_for
from models import db, Booking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    therapy = request.form['therapy']
    about = request.form['about']
    reason = request.form['reason']
    
    booking = Booking(name=name, email=email, therapy=therapy, about=about, reason=reason)
    db.session.add(booking)
    db.session.commit()

    return redirect(url_for('services'))

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)