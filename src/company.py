from flask import Flask, request, render_template, redirect, url_for, flash, session, logging
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Nitheesh Chandra:12345678@10.111.1.219:5100/ehub'
app.config['SERVER_NAME'] = '10.111.1.219:5000'

db = SQLAlchemy(app)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return "<h1>ERROR</h1>"

    return render_template("register.html", form=form)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
