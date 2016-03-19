"""
Create the Team Accolade database.
"""

from webapp import db

# Create the database based on the model.
db.create_all()
