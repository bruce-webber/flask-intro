"""
Add sample people and phones to the Team Accolade database.
"""

from webapp import db
from webapp import Person, Phone

# Delete records from tables of interest.
Person.query.delete()
Phone.query.delete()

# John Adams

person = Person()
person.first_name = 'John'
person.last_name = 'Adams'

phone = Phone()
phone.phone_number = '555-1234'
phone.phone_type = 'home'
person.phones.append(phone)

phone = Phone()
phone.phone_number = '555-5555'
phone.phone_type = 'cell'
person.phones.append(phone)

db.session.add(person)

# Sara Smith

person = Person()
person.first_name = 'Sara'
person.last_name = 'Smith'

phone = Phone()
phone.phone_number = '555-9999'
phone.phone_type = 'cell'
person.phones.append(phone)

db.session.add(person)

# Richard Recluse

person = Person()
person.first_name = 'Richard'
person.last_name = 'Recluse'

db.session.add(person)

# Commit the records to the database.
db.session.commit()
