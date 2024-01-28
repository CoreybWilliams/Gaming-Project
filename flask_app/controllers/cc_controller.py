from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.creditcard_model import Creditcard
from flask_app.models.user_model import User
from flask_app.models.products_model import Products
from flask_app.models.billing_address_model import billing_address
from flask_app.models.shipping_address_model import shipping_address


@app.route('/card_info', methods=['post'])
def card_info():
    is_valid = Creditcard.validate_cc(request.form)
    if not is_valid:
        return redirect('/payment')
    else:
        data={
            'name_on_card':request.form['name_on_card'],            
            'card_number': bcrypt.generate_password_hash(request.form['card_number']),
            'expiration_date': request.form['expiration_date'],
            'cvc' :request.form['cvc']
        }
        id=Creditcard.save_cc(data)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/payment')
        else:
            session['creditcard_id'] = id
            flash("Welcome, you are now logged in")
            return redirect('/nav')