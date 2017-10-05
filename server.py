from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ninja")
def ninja():
    return render_template("ninja.html")
@app.route("/ninja/<color>")
def turtle(color):
    print color
    name = ""
    if color == "red":
        name = "raphael"
    elif color == "blue":
        name = "leonardo"
    elif color == "purple":
        name = "donatello"
    elif color == "orange":
        name = "michelangelo"
    else:
        name = "notapril"
    return render_template("color.html", name=name)
app.run(debug=True)