import sys
from get_img import get_img
from display import display_pixel
from display import display_snake_pixel

def main(img_path, mode):
    img = get_img(img_path)
    img_width = img.size[0]
    img_height = img.size[1]
    if img_height > 16 or img_width > 16:
        print("Error: Image must be 16x16 pixel or less.")
        sys.exit(84)
    if mode == "0":
        print("Normal mode..")
        display_pixel(img, img_height, img_width)
    else:
        print("Snake mode..")
        display_snake_pixel(img, img_height, img_width)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3 or len(args) > 3:
        print("Error: You must have two argument\n"
        "\npy main.py [img_path] [mode]\n"
        "[img_path]:\n\tPath to the image\n"
        "[mode]:\n\t0: Normal mode\n\t1: Snake mode")
        exit(84)
    main(args[1], args[2])
    exit(0)