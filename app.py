import os
from flask import Flask, render_template, request, redirect, url_for, session

# Kunin ang absolute path ng templates folder para sa Vercel serverless environment
basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def welcome():
    try:
        return render_template('welcome.html')
    except Exception as e:
        template_path = os.path.join(template_dir, 'welcome.html')
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        return f"Template error: {str(e)}"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Ilagay dito ang login verification logic mo
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ilagay dito ang registration logic mo
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
