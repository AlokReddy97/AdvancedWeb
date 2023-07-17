from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

password_attempts = 0
"""
SQL Lite DB details.
"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'aloksecretkey'

db = SQLAlchemy(app)
"""
Creating a User model in the DB.
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35))
    password = db.Column(db.String(35))

@app.route('/', methods=['GET'])
def index():
    """
    Display the index.html page
    This route handles the GET request for the index page and renders the 'index.html' template.
    """
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    """
    Handle the form submission and process the report using a html page

    This route handles the POST request when the form is submitted.
    It retrieves the username and password from the form and checks the password requirements.
    If the requirements are met, it creates a new User object and adds it to the database.
    If the requirements are not met, it increments the password_attempts counter.
    It renders the 'report.html' template with the appropriate data.
    """
    global password_attempts

    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    ends_with_number = password[-1].isdigit()
    length_check = len(password) >= 8
    passed_requirements = has_uppercase and has_lowercase and ends_with_number and length_check

    # Check password requirements
    is_valid_password = True
    if not any(char.isupper() for char in password):
        is_valid_password = False
    if not any(char.islower() for char in password):
        is_valid_password = False
    if not password[-1].isdigit():
        is_valid_password = False
    if len(password) < 8:
        is_valid_password = False

    if is_valid_password:
        # Create a new User object and add it to the database
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        password_attempts = 0
    else:
        password_attempts += 1

    warning = password_attempts > 3

    return render_template('report.html', passed_requirements=is_valid_password, has_uppercase=has_uppercase,
                           has_lowercase=has_lowercase, ends_with_number=ends_with_number, length_check=length_check,
                           warning=warning)

@app.route('/db', methods=['GET'])
def show_db_details():
    """
    Retrieve all users from the database and render the user details page.

    This route handles the GET request to show the database details.
    It retrieves all users from the User table and renders the 'db.html' template
    with the user details.
    """
    users = User.query.all()
    return render_template('db.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        # Create the necessary tables in the database
        db.create_all()
    app.run(debug=True)
