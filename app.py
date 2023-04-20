from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.get("/")
def make_questions():

    """Put the questions on the page"""



    html = render_template("questions.html", prompt_list=silly_story.prompts)
    #                        place=place,
    # noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)

    return html

@app.get("/results")
def make_results():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")

debug = DebugToolbarExtension(app)
