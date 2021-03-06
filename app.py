# Imports
from flask import Flask, render_template


# App Config.
app = Flask(__name__)


# Controllers.
@app.route('/')
def home():
    return render_template('index.html')


# Default port:
if __name__ == '__main__':
    app.run(debug=True)
