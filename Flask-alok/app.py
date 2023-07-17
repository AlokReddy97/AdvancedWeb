from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

failed_attempts = 0

@app.route('/report', methods=['POST'])
def report():
    global failed_attempts

    username = request.form['username']
    password = request.form['password']

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    ends_with_number = password[-1].isdigit()
    length_check = len(password) >= 8
    passed_requirements = has_uppercase and has_lowercase and ends_with_number and length_check

    if passed_requirements:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        failed_attempts = 0
    else:
        failed_attempts += 1

    warning = failed_attempts > 3

    return render_template('report.html', passed_requirements=passed_requirements, has_uppercase=has_uppercase,
                           has_lowercase=has_lowercase, ends_with_number=ends_with_number, length_check=length_check,
                           warning=warning)
                           
@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
