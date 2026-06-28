from flask import Flask, render_template

app = Flask(__name__)

# ---------------- PAGE ROUTES ----------------

@app.route("/")
def homepage():
    """Homepage: hero section, intro to The Velvet Still"""
    return render_template("home.html")


@app.route("/menu")
def menu_page():
    """Service page: cocktail menu"""
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)