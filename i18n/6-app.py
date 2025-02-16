#!/usr/bin/env python3
""" Flask app with i18n and mock login """

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz


app = Flask(__name__)


# Configuring Babel
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


# Mock user database
users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
        },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
        },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"},
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
        },
}


# Get user by ID
def get_user():
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


# Before request, check if user is logged in
@app.before_request
def before_request():
    g.user = get_user()


# Determine best locale
@babel.localeselector
def get_locale():
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale

    if g.user and g.user.get("locale") in Config.LANGUAGES:
        return g.user["locale"]
    
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
