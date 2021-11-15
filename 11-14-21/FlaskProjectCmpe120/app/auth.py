from flask import Blueprint, render_template, request
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Connor:Bustos@cluster0.z1idj.mongodb.net/RegistrationData?retryWrites=true&w=majority")

db = cluster["RegistrationData"]
collection = db["RegistrationInfo"]

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html",text="test")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password = request.form.get('password1')
        password_confirm = request.form.get('password2')

        user_data = {"email": email, "name": name, "password": password_confirm}

        collection.insert_one(user_data)
        print(user_data)

        # check = False
        # # check statements for if valid
        # if '@' in email:
        #     check = True
        # if len(password) < 8:
        #     print("Password must be 8 characters or longer.")
        # if password != password_confirm:
        #     check = False
        #     print("Password does not match with the Confirm password")
        # if check:
        #     print('All valid checks passed to create an account.')
    return render_template("signup.html")

@auth.route('/calen')
def calen():
    return render_template("calendar.html")
