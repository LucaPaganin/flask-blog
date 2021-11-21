from flask import render_template
from blog import app

@app.route("/")
def homepage():
    posts = [{"title": "primo post", "body": "random content"}, 
             {"title": "secondo post", "body": "random content"}]
    flag = True
    return render_template("homepage.html", posts=posts, boolean_flag=flag)