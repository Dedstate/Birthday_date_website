from flask import Flask
from birthday_dates import a

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "\n".join(a)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
