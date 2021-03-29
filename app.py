from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")    

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/result")
def result():
    a = request.args.get("a")
    b = request.args.get("b")
    c = int(a) * int(b)
    return render_template("result.html", c=c) 

@app.route("/menu2")
def menu2():
    return render_template("menu2.html")    

if __name__ == "__main__":
    app.run(debug=True)