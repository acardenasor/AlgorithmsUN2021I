
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import backend

app = Flask(__name__ , template_folder = "/home/acardenaso/mysite/")

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        return render_template("index.html", output = backend.valorTriangular(int(text)), user_text = text)


