import unittest
from PIL import Image
from io import BytesIO
import requests
from src.services.classification_service import classify_image

class TestClassificationService(unittest.TestCase):
    def test_classify_image(self):
        url = "https://sonhodospes.vtexassets.com/assets/vtex.file-manager-graphql/images/e5db0805-e350-4bcd-97b8-0471e93bbbff___5dc008d8285a053a4b6180a4d82ed82d.jpg"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        result = classify_image(image)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
