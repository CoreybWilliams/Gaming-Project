from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_model import User
from flask_app.models.creditcard_model import Creditcard
from flask_app.models.products_model import Products
from flask_app.models.billing_address_model import billing_address
from flask_app.models.shipping_address_model import shipping_address

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
    if not User.validate(request.form):
        print("For Registration use VAL:",User.validate)
        print('Request form:',request.form)
        return redirect('/sign_in')
    data={
        'name':request.form['name'],            
        'email':request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id=User.save(data)
    session['user_id'] = id
    flash("Welcome, you are now logged in")
    return redirect('/navigation')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email or Password", "login")
        return redirect('/sign_in')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email or Password", "login")
        return render_template('login.html')
    session['user_id'] = user.id
    print(session)
    return redirect('/navigation')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/navigation')

@app.route('/logoutcc')
def logoutcc():
    session.clear()
    return redirect ('/order')

@app.route('/order')
def order():
    return render_template('order_com.html')




@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        product_id = request.form['id']
        product_name = request.form['name_of_product']
        product_price = request.form['price']

        cart = session.get('cart', [])

        cart.append({
            'id': product_id,
            'name_of_product': product_name,
            'price': product_price
        })

        session['cart'] = cart

        cart_count = len(cart)
        print(session.get('cart', []))
        return redirect('/payment')
    
@app.route('/payment')
def payment():
    cart = session.get('cart', [])
    products_in_cart = [(product['id'], product['name_of_product'], product['price']) for product in cart]
    total_price = round(sum(float(product[2]) for product in products_in_cart), 2)
    print(session.get('cart', []))
    return render_template('payment.html', products=products_in_cart, total_price=total_price)