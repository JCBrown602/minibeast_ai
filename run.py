# app.py
from app import create_app
#from flask import Flask, render_template, request

app = create_app()
#app = Flask(__name__)

#@app.route("/", methods=["GET", "POST"])
#def index():
#    return "Hello from MinibeastAI!"

if __name__ == "__main__":
    app.run