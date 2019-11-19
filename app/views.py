from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from app import app
from .models import Post, Base
import traceback

db = SQLAlchemy(app)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    Base.metadata.create_all(bind=db.engine)
    db.session.commit()


@app.route('/', methods=['GET'])
def index():
    """
    Displays the 5 recent posts and has a form to add posts.
    """
    posts = db.session.query(Post).limit(5).all()
    content = {
        "posts": reversed(posts)
    }

    return render_template("index.html", **content)


@app.route('/save_post', methods=['POST'])
def save_post():
    try:
        title = request.form['title']
        content = request.form['post_content']

        db.session.add(Post(title, content))
        db.session.commit()
        return redirect(url_for('index'))
    except:
        traceback.print_exc()
        return 'failed'


@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)