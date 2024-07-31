from flask import Flask, render_template
from table import d as sums

app = Flask(__name__)

@app.route("/table")
def table():
    return render_template('index.html', sums=sums)


app.run(debug=True)