from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/crud")
def crud():
    return render_template("crud.html")


@app.get("/about")
def about():
    return render_template("about.html")