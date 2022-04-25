from flask import render_template, redirect, flash, url_for, abort, request
from flask_login import current_user, login_user, logout_user, login_required

from blog import app, db
from blog.models import Post, User
from blog.forms import LoginForm, PostForm
from blog.utils import title_slugifier

@app.route("/")
def homepage():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("homepage.html", posts=posts)


@app.route("/posts/<string:post_slug>")
def post_detail(post_slug):
    post = Post.query.filter_by(slug=post_slug).first_or_404()
    return render_template("post_detail.html", post=post)


@app.route("/create-post", methods=["GET", "POST"])
@login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, 
                        body=form.body.data, 
                        description=form.description.data, 
                        author=current_user, 
                        slug=title_slugifier(form.title.data))
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('post_detail', post_slug=new_post.slug))
    return render_template("post_editor.html", form=form)


@app.route("/posts/<string:post_slug>/update", methods=["GET", "POST"])
@login_required
def post_update(post_slug):
    post_instance = Post.query.filter_by(slug=post_slug).first_or_404()
    if post_instance.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_instance.title = form.title.data
        post_instance.description = form.description.data
        post_instance.body = form.body.data
        db.session.commit()
        return redirect(url_for('post_detail', post_slug=post_instance.slug))
    elif request.method == "GET":
        form.title.data = post_instance.title
        form.description.data = post_instance.description
        form.body.data = post_instance.body
    return render_template("post_editor.html", form=form)


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
@login_required
def post_delete(post_id):
    post_instance = Post.query.get_or_404(post_id)
    if post_instance.author != current_user:
        abort(403)
    db.session.delete(post_instance)
    db.session.commit()
    return redirect(url_for('homepage'))


@app.route("/about")
def about():
    return render_template("about_page.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('username and password do not match')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))