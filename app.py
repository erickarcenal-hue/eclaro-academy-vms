import os
from flask import Flask, render_template, request, redirect, url_for, session

# Explicitly set the template folder path for Vercel serverless environment
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key_here'  # Replace with your actual secret key if needed

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add your login logic here
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# This is only needed if you run it locally; Vercel handles the serverless execution automatically.
if __name__ == '__main__':
    app.run(debug=True)
