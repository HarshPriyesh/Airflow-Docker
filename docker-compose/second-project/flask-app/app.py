from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="db",  # Container name of MySQL from docker-compose
    user="root",
    password="root",
    database="user_data",
)

cursor = db.cursor()

# Create a table for storing names if it doesn't exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
)
db.commit()


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
