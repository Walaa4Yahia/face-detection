from flask import request
from flask import Blueprint
from utils import *
from recognition import *
import json


views = Blueprint(__name__, "views")


@views.route("/")
def index():
    return "Flask Server!"


# handle post request that is sent from Node.js app
@views.route("/postdata", methods=["POST"])
def postdata():
    # extract json data from the request
    data = request.get_json()

    # decoding base64 taken image and saving it in taken img folder
    for img in data["taken_imgs"]:
        decode64_and_save_img(f"img/taken img/{img}.jpg", data["taken_imgs"][img])

    # getting attendance
    attendance = recognition()

    # clear folders from images
    clear_folder("img/taken img")

    # return attendace as JSON
    return json.dumps(attendance)
    # return {'text':"kk"}
    # return json.dumps({'hello': 'there'})

@views.route("/test", methods=["POST"])
def test():

    return json.dumps({'hello': 'world!'})