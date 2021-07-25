from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/home")
def home():
    return "This is home page of vivek..."

@app.route("/intro", methods=["GET"])
def intro():
    name = request.args.get("x")
    cname = request.args.get("y")
    html_code = render_template("intro.html", your_name=name, company=cname)
    return html_code

@app.route("/mail")
def mail():
    return "This is email page..."

@app.route("/")
def main_page():
    html_code = render_template("main.html")
    return html_code

@app.route("/docker")
def docker():
    html_code = render_template("docker.html")
    return html_code

@app.route("/kubernetes")
def kubernetes():
    html_code = render_template("kubernetes.html")
    return html_code

@app.route("/car")
def car():
    return render_template("index.html")

@app.route("/form")
def form():
    html_code = render_template("form.html")
    return html_code

if __name__ =="__main__":  
    app.run(debug = True)  