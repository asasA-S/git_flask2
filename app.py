from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")    

@app.route("/menu")
def menu():
    return render_template("menu.html")    

@app.route("/menu2")
def menu2():
    return render_template("menu2.html")    

if __name__ == "__main__":
    app.run(debug=True)