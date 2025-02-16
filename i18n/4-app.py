#!/usr/bin/env python3
"""
Flask app with Babel integration to handle i18n
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for language selection.
    Prioritizes the 'locale' query parameter if it's a supported language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
