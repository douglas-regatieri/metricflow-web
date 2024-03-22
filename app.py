from flask import Flask, render_template, request

app = Flask(__name__, static_folder='templates')

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/privace-policy')
def privace_policy():
    return render_template("privace-policy.html")

@app.route('/produtos')
def produtos():
    return render_template("produtos.html")

app.run(debug=True)
