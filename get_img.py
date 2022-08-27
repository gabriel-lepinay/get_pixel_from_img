from PIL import Image

def get_img(img_path):
    try:
        img = Image.open(img_path)
    except:
        print("Error: Image path is invalid !")
        exit(84)
    converted_img = img.convert("RGB")
    return converted_img