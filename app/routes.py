from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('index.html')

# Halaman Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Cek apakah username sudah digunakan
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        # Hash password sebelum menyimpannya
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html')

# Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Cek apakah user ada di database
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!')
            return redirect(url_for('order'))
        else:
            flash('Invalid credentials!')
    return render_template('login.html')

# Halaman Pesanan
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        order_details = request.form['order_details']
        flash('Order placed successfully!')
        return redirect(url_for('index'))
    return render_template('order.html')
