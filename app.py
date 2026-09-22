import os
from flask import Flask, render_template, request, redirect, url_for, session

# Kunin ang path ng kasalukuyang directory
basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def welcome():
    # Sinisigurong babasahin niya nang direkta ang file kung sakaling hindi mahanap ng Jinja loader
    try:
        return render_template('welcome.html')
    except Exception as e:
        # Fallback sakaling mag-error pa rin ang template loader sa Vercel
        template_path = os.path.join(template_dir, 'welcome.html')
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        return f"Template error: {str(e)} (Path checked: {template_path})"

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
