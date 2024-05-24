from flask import Flask, render_template

app = Flask("__name__")

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