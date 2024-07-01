import tensorflow as tf # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np

# Carregar o modelo MobileNetV2 pré-treinado
model = MobileNetV2(weights='imagenet')

def classify_image(img):
    # Pré-processar a imagem
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Fazer a previsão
    preds = model.predict(img_array)
    # Decodificar as previsões
    decoded_preds = decode_predictions(preds, top=3)[0]
    return decoded_preds

def classify_images(images):
    return [classify_image(img) for img in images]
