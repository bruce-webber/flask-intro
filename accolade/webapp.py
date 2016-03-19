"""
Team Accolade web application.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


# Database model.

class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phones = db.relationship('Phone', backref='person')


class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    phone_number = db.Column(db.String(50))
    phone_type = db.Column(db.String(50))


# Routes.

@app.route("/")
def home_page():
    return render_template('home.html')


@app.route("/roster/")
def roster_page():
    people = Person.query.order_by(Person.last_name, Person.first_name).all()
    return render_template('roster.html', people=people)


if __name__ == "__main__":
    app.debug = True
    app.run()
