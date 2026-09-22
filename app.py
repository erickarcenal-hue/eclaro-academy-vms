import os
from flask import Flask, render_template, request, redirect, url_for, session

# Kunin ang mismong folder kung nasaan nakaposisyon ang app.py na ito
basedir = os.path.abspath(os.path.dirname(__file__))

# I-set nang direkta ang templates folder gamit ang absolute path
app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))
app.secret_key = 'your_secret_key_here'

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
