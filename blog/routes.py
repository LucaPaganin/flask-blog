from flask import render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from blog import app

auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route("/")
# @auth.login_required
def homepage():
    posts = [{"title": "primo post", "body": "random content"}, 
             {"title": "secondo post", "body": "random content"}]
    flag = True
    return render_template("homepage.html", posts=posts, boolean_flag=flag)


@app.route("/about")
def about():
    return render_template("about_page.html")