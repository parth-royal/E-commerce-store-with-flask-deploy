from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

app = Flask(__name__)

# In-memory database to store user data
users = {}
sessions = {}
cart = {}


logged_in = False

@app.route('/')
def index():
    return render_template('index.html',logged_in=logged_in)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cart')
def view_cart():
    session_id = request.cookies.get('session_id')
    logged_in = session_id is not None and sessions.get(session_id, False)

    if logged_in:
        total_price = sum(item['price'] * item['quantity'] for item in cart.values()) if cart else 0
        return render_template('cart.html', cart=cart, total_price=total_price)
    else:
        return redirect(url_for('login'))

@app.route('/add-to-cart', methods=['GET'])
def add_to_cart():
    session_id = request.cookies.get('session_id')
    logged_in = session_id is not None and sessions.get(session_id, False)

    if logged_in:
        product_id = request.args.get('productId')
        if product_id:
            if product_id in cart:
                cart[product_id]['quantity'] += 1
            else:
                cart[product_id] = {'quantity': 1, 'name': f'Product {product_id}', 'price': 99.99}  # You can replace these with actual product details
        return redirect(url_for('view_cart'))
    else:
        return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')

# @app.route('/login-submit', methods=['POST'])
# def login_submit():
#     username = request.form['username']
#     password = request.form['password']

#     if username in users and users[username]['password'] == password:
#         session_id = str(uuid.uuid4())
#         sessions[session_id] = True
#         response = redirect(url_for('index'))
#         response.set_cookie('session_id', session_id, httponly=True)
#         return response
#     else:
#         return redirect(url_for('login', error=1))

@app.route('/login-submit', methods=['POST'])
def login_submit():
    global logged_in  # Declare logged_in as global

    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        session_id = str(uuid.uuid4())
        sessions[session_id] = True
        logged_in = True  # Update logged_in to True when the user logs in successfully
        response = redirect(url_for('index'))
        response.set_cookie('session_id', session_id, httponly=True)
        return response
    else:
        return redirect(url_for('login', error=1))



@app.route('/register-submit', methods=['POST'])
def register_submit():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    users[username] = {'password': password, 'email': email}
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    global logged_in  # Declare logged_in as global

    session_id = request.cookies.get('session_id')
    if session_id in sessions:
        sessions.pop(session_id)
    logged_in = False  # Update logged_in to False when the user logs out
    response = redirect(url_for('index'))
    response.set_cookie('session_id', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
