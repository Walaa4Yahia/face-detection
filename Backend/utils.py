import base64
from PIL import Image
from io import BytesIO
import os

def decode64_and_save_img(path, data):
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(data))


def open_and_encode64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read())

def save_faces(data):
    for key in data["faces"]:
            value = data["faces"][key]
            decode64_and_save_img(f"img/faces/{key}.jpg", value)

def encode_npImage_to_base64(face_image):
    pil_image = Image.fromarray(face_image)
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue())

def clear_folder(path):
     for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                 os.remove(f)