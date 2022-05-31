from flask import Flask ,render_template,request,jsonify
import base64
import io
from PIL import Image 
import tensorflow as tf
import numpy as np
app = Flask(__name__)
model_instance = tf.keras.models.load_model("./Model")
labels = ['biryani', 'gulab_jamun', 'karahi', 'samosa', 'shami_kabab', 'tikka']
isloading = False
print("Model Ready To Test.")

@app.route("/")
def hello_world():
     return render_template('index.html', isloading=isloading)


def decode_img(imageString):
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img

@app.route('/detect',methods=['POST'])
def detect_image():
    isloading = True
    imagesFile = request.files
    pilImage = Image.open(imagesFile['webcam'])
    imgdata = np.expand_dims(np.asarray(pilImage.resize([224,224])),0)/255
    isloading = False
    return jsonify({"result":labels[np.argmax(model_instance.predict(imgdata))]}) 