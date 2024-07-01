from PIL import Image

def process_image(image: Image.Image):
    # Exemplo básico de processamento: redimensionar a imagem
    resized_image = image.resize((224, 224))
    return resized_image

def process_images(images):
    return [process_image(image) for image in images]
