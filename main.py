from datetime import date
from flask import Flask, render_template
from birthday_dates import archived, current

# Initialize Flask app and set constants
app = Flask(__name__)
LETTER = "Г"  # Letter appended to the year
YEAR = 2013  # Year when started school


# Do not modify below
def get_grade_name(year: int, letter: str) -> str:
    y = date.today().year - year
    if date.today().month < 6:
        y -= 1
    grade = str(y) + letter
    if y > 11:
        grade = f"выпускников 11{LETTER} класса"
    return grade


grade = get_grade_name(YEAR, LETTER)


@app.route("/")
@app.route("/main")
@app.route("/index")
@app.route("/main.html")
@app.route("/index.html")
def index() -> str:
    return render_template("base.html", students=current, grade=grade)


@app.route("/other")
@app.route("/others")
@app.route("/archive")
@app.route("/history")
@app.route("/archived")
@app.route("/other.html")
@app.route("/others.html")
@app.route("/history.html")
@app.route("/archive.html")
@app.route("/archived.html")
def history() -> str:
    return render_template(
        "base.html", students=archived, grade=grade, archived=True
    )


if __name__ == "__main__":
    app.run()
