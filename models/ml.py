import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from PIL import Image
import tensorflow as tf
import cv2
import numpy as np
import io

def up_img(contents):
    try:
        content = Image.open(io.BytesIO(contents))
        image = np.array(content)
        return process_img(image)
    except Exception as e:
        print(f'Error up image: {e}')

def process_img(image):
    try:
        resize_img = cv2.resize(image,(150,150))
        resize_img = np.expand_dims(resize_img, axis=0)
        return predict_img(resize_img)
    except Exception as e:
        print(f'Error process img: {e}')


def predict_img(image):
    class_name = {0: "Drawing", 1:"Hentai", 2:"Neutral", 3:"Porn", 4:"Sexy"}
    try:
        model = tf.keras.models.load_model("models/model/resnet50-2.keras")
        predict = model.predict(image)
        predict = np.argmax(predict, axis=1)
        category = [class_name[id] for id in predict]

        return {"Prediksi gambar ini adalah kategori: ": category}

    except Exception as e:
        print(f'Cant predict image: {e}')