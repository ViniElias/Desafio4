from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "fatec"
app.config["MYSQL_DB"] = "stardew"
mysql = MySQL(app)


@app.route("/feedback")
def feedback():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM feedback")
    feedback = cur.fetchall()
    cur.close()
    return render_template("feedback.html", feedback=feedback)


@app.route("/add", methods=["POST"])
def add_fb():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        comentario = request.form["comentario"]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO feedback (nome, email, comentario) VALUES (%s, %s, %s)",
            (nome, email, comentario),
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("feedback"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/peixes")
def peixes():
    return render_template("peixes.html")


@app.route("/itens")
def itens():
    return render_template("itens.html")


@app.route("/form")
def form():
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
