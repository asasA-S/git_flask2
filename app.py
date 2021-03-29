from flask import Flask, render_template, request

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

@app.route("/menu2_2")
def menu2_2():
    h = request.args.get("h")
    h = int(h)
    en = h * 2 * 3.14
    men = h * h * 3.14
    return render_template("menu2_2.html",en=en,men=men)    

if __name__ == "__main__":
    app.run(debug=True)