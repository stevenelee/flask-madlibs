from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def make_questions():
    """Put the questions on the page"""
    return  render_template("questions.html", prompt_list=silly_story.prompts)

@app.get("/results")
def make_results():
    """Return story with values from form"""
    story = silly_story.get_result_text(request.args)

    return render_template("results.html", story=story)