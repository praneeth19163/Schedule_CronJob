from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  


def get_db_connection():
    conn = sqlite3.connect("schedule.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userid = request.form["userid"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE userid=? AND password=?", (userid, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["userid"] = user["userid"]
            session["preferred_tech"] = user["preferred_tech"]
            return redirect("/schedule")
        else:
            return "Invalid credentials! Try again."

    return render_template("login.html")
@app.route("/schedule")
def schedule():
    if "userid" not in session:
        return redirect("/")

    preferred_tech = session["preferred_tech"]
    today_date = datetime.now().strftime("%Y-%m-%d")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM schedule WHERE preferred_tech=? AND date=?", (preferred_tech, today_date))
    tasks = cursor.fetchall()
    conn.close()

    return render_template("schedule.html", userid=session["userid"], tasks=tasks, preferred_tech=preferred_tech)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
