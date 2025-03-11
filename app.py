from flask import Flask, render_template
from flask_wtf import FlaskForm
from pymsgbox import password
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_mysqldb import MySQL
import bcrypt
app=Flask(__name__)
#mysql configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQQL_DB']='mydata'


class RegisteerForm(FlaskForm):
    name=StringField("name",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    password=StringField("Password",validators=[DataRequired()])
    submit=StringField("Register")


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/register')
def register():
    form=RegisteerForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data

        hashed_password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())


    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__== '__main__':
    app.run(debug=True)
