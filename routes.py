from flask import Flask, render_template, redirect, request
from forms import AddPostForm, RegisterForm, LoginForm
from os import path
from ext import app, db
from models import User, Blog
from flask_login import login_user, current_user, login_required, logout_user


@app.route("/")
def home():
    blogs = Blog.query.all()
    return render_template("index.html", blog=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route("/blog", methods=['POST', 'GET'])
@login_required  # Ensure the user is logged in to access this route
def blog():
    form = AddPostForm()
    if form.validate_on_submit():
        img_filename = None
        if form.img.data:
            img_filename = form.img.data.filename
            file_dir = path.join(app.root_path, "static", img_filename)
            form.img.data.save(file_dir)

        new_blog = Blog(title=form.title.data, text=form.desc.data, img=img_filename, author=current_user)
        db.session.add(new_blog)
        db.session.commit()

        return redirect('/')  # Redirect to the home page after successful submission
    
    return render_template("blog.html", form=form)

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=form.password.data)    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template("signup.html", form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        password = User.query.filter(User.password == form.password.data).first()
        if user and user.password == form.password.data  and user.email == form.email.data:
            login_user(user)
        return redirect('/')
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required  # Ensures the user is logged in to access this route
def logout():
    logout_user()  # Logs out the current user
    return redirect('/')
