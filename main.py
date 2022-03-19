from flask import Flask, render_template
from birthday_dates import a

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html", a=a)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
