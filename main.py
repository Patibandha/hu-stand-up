from flask import Flask, render_template
from whos_next import get_all_members

app = Flask(__name__)


@app.route('/')
def index():
    all_members = get_all_members()
    return render_template('index.html', posts=all_members)