from flask import Flask, render_template
from flask_wtf import FlaskForm


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)