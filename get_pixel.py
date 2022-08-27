def get_pixel_color(img_width, img_height, img):
    for pixel_y in range(img_height):
        for pixel_x in range(img_width):
            temp_pixel = img.getpixel((pixel_x, pixel_y))
            print("{}, {}, {}".format(temp_pixel[0], temp_pixel[1], temp_pixel[2]))