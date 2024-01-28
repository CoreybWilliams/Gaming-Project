from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navigation')
def navigation():
    return render_template('nav.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/dnd')
def dnd():
    return render_template('dnd.html')

@app.route('/fab')
def fab():
    return render_template('fab.html')

@app.route('/board_games')
def board_games():
    return render_template('board_games.html')

@app.route('/dcg')
def dcg():
    return render_template('dcg.html')

@app.route('/sign_in')
def sign_in():
    return render_template('login.html')


@app.route('/registration', methods=['post'])
def registration():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/registration')
    else:
        data={
            'name':request.form['name'],            
            'email':request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id=User.save(data)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/registration')
        else:
            session['user_id'] = id
            flash("Welcome, you are now logged in")
            return redirect('/nav')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email or Password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email or Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/nav.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/card_info', methods=['post'])
def card_info():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/payment')
    else:
        data={
            'name_on_card':request.form['name_on_card'],            
            'card_number': bcrypt.generate_password_hash(request.form['card_number']),
            'expiration_date': request.form['expiration_date'],
            'cvc' :request.form['cvc']
        }
        id=User.save(data)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/payment')
        else:
            session['user_id'] = id
            flash("Welcome, you are now logged in")
            return redirect('/nav')