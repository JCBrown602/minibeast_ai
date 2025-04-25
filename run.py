# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello from MinibeastAI!"

if __name__ == "__main__":
    app.run(debug=True)
