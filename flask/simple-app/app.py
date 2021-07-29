from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/docker")
def home():
    return "Welcome to Docker Homepage !!"

@app.route("/intro", methods=["GET"])
def intro():
    name = request.args.get("x")
    cname = request.args.get("y")
    html_code = render_template("intro.html", your_name=name, company=cname)
    return html_code

# Create new container --> name and image name required
@app.route("/create_container")
def create_container():
    return "This is email page..."

#Stop particular container from a name or id --> name or id of container
@app.route("/stop_container")
def stop_container():
    html_code = render_template("main.html")
    return html_code

#Show all running containers --> no input required
@app.route("/show_running_containers")
def show_running_containers():
    html_code = render_template("docker.html")
    return html_code

#Show all stopped containers --> no input required
@app.route("/show_stopped_containers")
def show_stopped_containers():
    html_code = render_template("kubernetes.html")
    return html_code

#Show all images --> no input required
@app.route("/show_all_images")
def show_all_images():
    return render_template("index.html")

#Show all stopped containers --> no input required
@app.route("/stop_all_containers")
def stop_all_containers():
    html_code = render_template("form.html")
    return html_code

#Delete image with name or image id --> image id or name is required
@app.route("/delete_images")
def delete_images():
    return "This is email page..."

#Delete all images --> no input required
@app.route("/delete_all_images")
def delete_all_images():
    return "This is email page..."

#Pull images --> image name required
@app.route("/pull_images")
def pull_images():
    return "This is email page..."

#Expose container with a port --> port number, image name and container name required
@app.route("/expose_container")
def expose_container():
    return "This is email page..."

#Build image from Dockerfile --> name of image with tag and path
@app.route("/build_image")
def build_image():
    return "This is email page..."

#
if __name__ =="__main__":  
    app.run(debug = True)  