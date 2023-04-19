from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.get("/questions")
def make_questions():
    """Put the questions on the page"""

    app.request()

    html = render_template("questions.html",place= )

debug = DebugToolbarExtension(app)
