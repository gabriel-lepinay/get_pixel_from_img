def display_snake_pixel(img, height_max, width_max):
    for height in range(0, height_max):
        if (height % 2 == 0):
            for width in range(0, width_max):
                temp_pixel = img.getpixel((width, height))
                print("{}, {}, {}".format(temp_pixel[0], temp_pixel[1], temp_pixel[2]))
        else:
            for width in range(width_max - 1, 0, -1):
                temp_pixel = img.getpixel((width, height))
                print("{}, {}, {}".format(temp_pixel[0], temp_pixel[1], temp_pixel[2]))

def display_pixel(img, height_max, width_max):
    for height in range(height_max):
        for width in range(width_max):
            temp_pixel = img.getpixel((width, height))
            print("{}, {}, {}".format(temp_pixel[0], temp_pixel[1], temp_pixel[2]))
