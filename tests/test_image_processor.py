import unittest
from PIL import Image
from io import BytesIO
import requests
from src.components.image_processor import process_image

class TestImageProcessor(unittest.TestCase):
    def test_process_image(self):
        url = "https://sonhodospes.vtexassets.com/assets/vtex.file-manager-graphql/images/e5db0805-e350-4bcd-97b8-0471e93bbbff___5dc008d8285a053a4b6180a4d82ed82d.jpg"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        processed_image = process_image(image)
        self.assertEqual(processed_image.size, (224, 224))

if __name__ == '__main__':
    unittest.main()
