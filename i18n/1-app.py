#!/usr/bin/env python3
"""Flask app with Babel internationalization."""

from flask import Config, Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)  # Instantiate the Babel extension


@app.route('/')
def index():
    """Render the 1-index.html template."""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
