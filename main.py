import sys
from get_img import get_img
from get_pixel import get_pixel_color

def main(img_path):
    img = get_img(img_path)
    img_width = img.size[0]
    img_height = img.size[1]

    get_pixel_color(img_width, img_height, img)
    print("image size: {}x{}".format(img_width, img_height))
    
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        print("Error: You must have one argument\n\tpy main.py [img_path]")
        exit(84)
    main(args[1])
    exit(0)


