#!/usr/bin/env python3
from flask import Flask, render_template
'''
Create a single / route and an index.html template
'''

app = Flask(__name__)


@app.route('/')
def index():
    '''
    returns the template 0-index.html
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
