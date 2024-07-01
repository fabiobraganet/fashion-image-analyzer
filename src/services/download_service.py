import json
import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def download_images_from_jsonl(jsonl_path):
    images = []
    json_data = []
    with open(jsonl_path, 'r') as jsonl_file:
        for line in jsonl_file:
            item = json.loads(line.strip())
            json_data.append(item)
            image = download_image(item['url'])
            images.append(image)
    return images, json_data
