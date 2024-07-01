import logging
import os
import json
from datetime import datetime
from services.download_service import download_images_from_jsonl
from components.image_processor import process_images
from services.classification_service import classify_images

# Suprimir avisos do TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
logging.getLogger('tensorflow').setLevel(logging.ERROR)

import tensorflow as tf # type: ignore

def suppress_tensorflow_warnings():
    import warnings
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    tf.get_logger().setLevel(logging.ERROR)
    tf.autograph.set_verbosity(3)

    logging.getLogger('tensorflow').disabled = True

suppress_tensorflow_warnings()

def main():
    # Caminho para o arquivo JSONL com URLs das imagens
    jsonl_path = 'data/images.jsonl'

    # Verificar se o arquivo JSONL de entrada não está vazio
    if os.path.getsize(jsonl_path) == 0:
        print("O arquivo JSONL de entrada está vazio.")
        return

    # Baixar as imagens
    images, json_data = download_images_from_jsonl(jsonl_path)

    # Processar as imagens
    processed_images = process_images(images)

    # Classificar as imagens
    classifications = classify_images(processed_images)

    # Adicionar classificações aos dados JSON
    for i, classification in enumerate(classifications):
        json_data[i]['classifications'] = [
            {'class_id': class_id, 'class_name': class_name, 'score': float(score)}
            for class_id, class_name, score in classification
        ]

    # Gerar o nome do arquivo de saída com timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    output_jsonl_path = f'data/output_{timestamp}.jsonl'

    # Escrever os dados atualizados no novo arquivo JSONL
    with open(output_jsonl_path, 'w') as jsonl_file:
        for item in json_data:
            jsonl_file.write(json.dumps(item) + '\n')

    print(f"Classificações salvas em {output_jsonl_path}")

if __name__ == '__main__':
    main()
