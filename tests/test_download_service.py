import unittest
from src.services.download_service import download_image

class TestDownloadService(unittest.TestCase):
    def test_download_image(self):
        url = "https://sonhodospes.vtexassets.com/assets/vtex.file-manager-graphql/images/e5db0805-e350-4bcd-97b8-0471e93bbbff___5dc008d8285a053a4b6180a4d82ed82d.jpg"
        image = download_image(url)
        self.assertIsNotNone(image)
        self.assertEqual(image.format, 'JPEG')

if __name__ == '__main__':
    unittest.main()
