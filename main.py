from flask import Flask, render_template, url_for, 
from birthday_dates import a

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html", a=a)


app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.png'))


if __name__ == "__main__":
    app.run()
