from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'aloksecretkey'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Add Usr model below
class Usr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usr {self.email}>'

# Create the database tables before running the application
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/db', methods=['GET'])
def db_details():
    users = Usr.query.all()
    return render_template('db_details.html', users=users)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Usr.query.filter_by(email=email, password=password).first()
        if user:
            return render_template('secretPage.html')
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        print(first_name, last_name, email, password, confirm_password)
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
        else:
            existing_user = Usr.query.filter_by(email=email).first()
            print(email)
            print(existing_user)
            if existing_user:
                flash('Email address already exists. Please use a different email.', 'danger')
                return render_template('email_used.html')
            else:
                # Save the user data to the database
                new_user = Usr(first_name=first_name, last_name=last_name, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                return render_template('thankyou.html')

    return render_template('signup.html')

@app.route('/secretPage')
def secret_page():
    return render_template('secretPage.html')

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
