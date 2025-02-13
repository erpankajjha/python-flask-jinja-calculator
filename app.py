from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import math

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if "memory" not in session:
        session["memory"] = 0

    if "expression" not in session:
        session["expression"] = ""

    if request.method == "POST":
        if request.form.get("action") == "calculate":
            try:
                session["expression"] = str(eval(session["expression"]))
            except:
                session["expression"] = "Error"
        elif request.form.get("action") == "clear":
            session["expression"] = ""
        elif request.form.get("action") == "memory_add":
            session["memory"] += eval(session["expression"])
        elif request.form.get("action") == "memory_subtract":
            session["memory"] -= eval(session["expression"])
        elif request.form.get("action") == "memory_clear":
            session["memory"] = 0
        elif request.form.get("action") == "memory_recall":
            session["expression"] = str(session["memory"])
        else:
            session["expression"] += request.form.get("action")
        return redirect(url_for("calculator"))

    return render_template("calculator.html", expression=session["expression"])

if __name__ == "__main__":
    app.run(debug=True)