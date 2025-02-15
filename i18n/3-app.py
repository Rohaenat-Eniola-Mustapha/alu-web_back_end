#!/usr/bin/env python3
"""
Flask app with Babel integration for multilingual support.

This module initializes a Flask application with Babel to provide
English and French translations.

Functions:
    get_locale: Determines the best language for the user.
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _
from flask_babel import Babel, _


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)  # Initialize Babel


@babel.localeselector
def get_locale():
    """
    Determine the best match for
    supported languages based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the 3-index.html template with translations.
    """
    return render_template(
        '3-index.html',
        home_title=_("home_title"),
        home_header=_("home_header")
        )


if __name__ == '__main__':
    app.run(debug=True)
