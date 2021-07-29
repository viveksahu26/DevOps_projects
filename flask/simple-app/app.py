import subprocess
from flask import Flask, render_template
from flask import request
from subprocess import getoutput

app = Flask(__name__)

@app.route("/docker")
def home():

    return "Welcome to Docker Homepage !!"


@app.route("/intro", methods=["GET"])
def intro():
    name      =   request.args.get("x")
    cname     =   request.args.get("y")
    html_code =   render_template("intro.html", your_name=name, company=cname)

    return html_code


# Create new container --> name and image name required
@app.route("/create_container", method=["GET"])
def create_container():
    name      =   request.args.get("x")
    image     =   request.args.get("y")
    command   =   "docker run -dit --name {0} {1}".format(name, image)
    output    =   subprocess.getoutput(command)

    return     "<pre>" + command + "</pre>"


#Stop particular container from a name or id --> name or id of container
@app.route("/stop_container")
def stop_container():
    name      =   request.args.get("x")
    command   =   "docker rm {0}".format(name)
    output    =   subprocess.getoutput(command)

    return    "<pre>" + command + "</pre>"


#Show all running containers --> no input required
@app.route("/show_running_containers")
def show_running_containers():
    command     =   "docker ps"
    output      =   subprocess.getoutput(command)

    return      "<pre>" +  output + "</pre>"


#Show all stopped containers --> no input required
@app.route("/show_stopped_containers")
def show_stopped_containers():
    command     =   "docker ps -a"
    output      =   subprocess.getoutput(command)

    return      "<pre>" +  output + "</pre>"


#Show all images --> no input required
@app.route("/show_all_images")
def show_all_images():
    command    =   "docker images"
    output     =   subprocess.getoutput(command)

    return "<pre>" +  output + "</pre>"


#Show all stopped containers --> no input required
@app.route("/stop_all_containers")
def stop_all_containers():
    command    =   "docker rm -f $(docker ps -aq)"
    output     =   subprocess.getoutput(command)

    return     "<pre>" +  output + "</pre>"


#Delete image with name or image id --> image id or name is required
@app.route("/delete_images")
def delete_images():
    name     =   request.args.get("x")
    command  =   "docker rmi {0}".format(name)
    output   =   subprocess.getoutput(command)

    return   "<pre>" + command + "</pre>"


#Delete all images --> no input required
@app.route("/delete_all_images")
def delete_all_images():
    command  =   "docker rmi -f $(docker images)"
    output   =   subprocess.getoutput(command)

    return   "<pre>" +  output + "</pre>"


#Pull images --> image name required
@app.route("/pull_images")
def pull_images():
    name     =   request.args.get("x")
    tag      =   request.args.get("y")
    command  =   "docker pull {0}:{1}".format(name, tag)
    output   =   subprocess.getoutput(command)

    return   "<pre>" + command + "</pre>"


#Expose container with a port --> port number, image name and container name required
@app.route("/expose_container")
def expose_container():
    name      =   request.args.get("x")
    image     =   request.args.get("y")
    port      =   request.args.get("z")
    command   =   "docker run -dit --name {0} --port={2}  {1}".format(name, image, port)
    output    =   subprocess.getoutput(command)

    return     "<pre>" + command + "</pre>"


@app.route("/description_container")
def pull_images():
    name     =   request.args.get("x")
    command  =   "docker inspect {0}".format(name)
    output   =   subprocess.getoutput(command)

    return   "<pre>" + command + "</pre>"



#Build image from Dockerfile --> name of image with tag and path
@app.route("/build_image")
def build_image():

    return "This is email page..."

#
if __name__ =="__main__":  
    app.run(debug = True)  