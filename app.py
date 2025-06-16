# filepath: c:\Users\bruhg\pyproj\ict_portfolio\app.py
import logging
from flask import Flask, render_template

# Enable logging
logging.basicConfig(level=logging.DEBUG)
print("Starting Flask app...")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return "Flask is working!"

if __name__ == '__main__':
    print("Before running Flask app...")
    app.run(debug=True)