#!/usr/bin/env python3
"""Basic Flask web application.

This module initializes a simple Flask app with a single route (`/`).
It serves an HTML template (`0-index.html`).
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render and return the 0-index.html template."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
