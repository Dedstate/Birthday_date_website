from main import app
from flask import url_for

if __name__ == "__main__":
    app.run()
    app.add_url_rule(
        "/favicon.ico", redirect_to=url_for("static", filename="favicon.png")
    )
