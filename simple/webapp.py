"""
A simple Flask web application demonstrating templates.
"""

import datetime

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    dayname = datetime.date.today().strftime('%A')
    return render_template('home.html', dayname=dayname)


@app.route('/page-two/')
def page_two():
    return render_template('page-two.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
