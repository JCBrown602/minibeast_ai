from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from .model import predict_image

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        if "image" not in request.files:
            return redirect(request.url)
        image = request.files["image"]
        if image.filename == "":
            return redirect(request.url)
        if image:
            filename = secure_filename(image.filename)
            filepath = os.path.join("static/uploads", filename)
            image.save(filepath)
            prediction = predict_image(filepath)
    return render_template("index.html", prediction=prediction)
