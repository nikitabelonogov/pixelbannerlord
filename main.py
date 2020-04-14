#!python
from PIL import Image
import argparse

colors = [
    (181, 122, 30, 1),
    (78, 26, 19, 1),
    (40, 78, 25, 1),
    (180, 240, 241, 1),
    (121, 49, 145, 1),
    (252, 222, 144, 1),
    (56, 33, 136, 1),
    (222, 169, 64, 1),
    (89, 22, 69, 1),
    (255, 173, 84, 1),
    (66, 144, 129, 1),
    (239, 201, 144, 1),
    (34, 66, 119, 1),
    (206, 218, 231, 1),
    (141, 41, 26, 1),
    (247, 191, 70, 1),
    (107, 213, 220, 1),
    (238, 214, 144, 1),
    (174, 195, 130, 1),
    (195, 195, 195, 1),
    (213, 215, 212, 1),
    (231, 236, 214, 1),
    (234, 238, 239, 1),
    (127, 107, 96, 1),
    (150, 126, 126, 1),
    (182, 171, 167, 1),
    (231, 211, 186, 1),
    (234, 225, 218, 1),
    (217, 219, 206, 1),
    (223, 214, 205, 1),
    (202, 193, 186, 1),
    (236, 232, 221, 1),
    (224, 220, 217, 1),
    (239, 236, 229, 1),
    (234, 233, 229, 1),
    (245, 245, 245, 1),
    (245, 179, 101, 1),
    (245, 179, 101, 1),
    (230, 140, 54, 1),
    (220, 172, 70, 1),
    (255, 255, 255, 1),
    (238, 231, 212, 1),
    (233, 226, 197, 1),
    (235, 220, 187, 1),
    (240, 224, 165, 1),
    (224, 199, 142, 1),
    (205, 168, 124, 1),
    (249, 213, 117, 1),
    (228, 68, 52, 1),
    (230, 144, 119, 1),
    (231, 156, 125, 1),
    (201, 75, 78, 1),
    (230, 176, 166, 1),
    (228, 200, 199, 1),
    (242, 176, 162, 1),
    (218, 108, 109, 1),
    (226, 188, 175, 1),
    (189, 126, 117, 1),
    (209, 199, 197, 1),
    (151, 91, 67, 1),
    (230, 165, 127, 1),
    (123, 94, 78, 1),
    (172, 145, 136, 1),
    (215, 150, 122, 1),
    (230, 201, 187, 1),
    (147, 65, 101, 1),
    (211, 158, 176, 1),
    (100, 73, 116, 1),
    (127, 101, 138, 1),
    (167, 147, 174, 1),
    (197, 5, 124, 1),
    (113, 0, 131, 1),
    (0, 102, 127, 1),
    (0, 160, 186, 1),
    (83, 183, 198, 1),
    (161, 177, 239, 1),
    (127, 140, 192, 1),
    (89, 96, 168, 1),
    (193, 88, 154, 1),
    (163, 79, 175, 1),
    (208, 142, 84, 1),
    (147, 155, 217, 1),
    (234, 79, 0, 1),
    (210, 45, 51, 1),
    (253, 226, 23, 1),
    (255, 164, 221, 1),
    (203, 131, 213, 1),
    (137, 93, 94, 1),
    (2, 255, 25, 1),
    (1, 150, 120, 1),
    (158, 196, 0, 1),
    (163, 68, 2, 1),
    (113, 66, 20, 1),
    (255, 195, 195, 1),
    (133, 95, 168, 1),
    (126, 110, 74, 1),
    (58, 51, 33, 1),
    (61, 47, 34, 1),
    (66, 44, 46, 1),
    (69, 62, 56, 1),
    (51, 44, 77, 1),
    (81, 82, 103, 1),
    (108, 114, 162, 1),
    (139, 147, 186, 1),
    (166, 213, 219, 1),
    (164, 177, 194, 1),
    (197, 188, 209, 1),
    (216, 174, 197, 1),
    (206, 218, 218, 1),
    (210, 214, 213, 1),
    (202, 204, 203, 1),
    (223, 222, 220, 1),
    (93, 91, 68, 1),
    (114, 107, 61, 1),
    (205, 204, 124, 1),
    (143, 209, 221, 1),
    (11, 12, 17, 1),
    (245, 179, 101, 1),
    (227, 102, 100, 1),
    (69, 109, 255, 1),
    (95, 189, 114, 1),
    (244, 211, 46, 1),
    (169, 116, 53, 1),
    (65, 40, 27, 1),
    (65, 40, 27, 1),
    (169, 116, 53, 1),
    (52, 103, 30, 1),
    (243, 243, 243, 1),
    (243, 243, 243, 1),
    (52, 103, 30, 1),
    (119, 57, 167, 1),
    (241, 194, 50, 1),
    (241, 194, 50, 1),
    (119, 57, 167, 1),
    (90, 164, 173, 1),
    (255, 233, 212, 1),
    (255, 233, 212, 1),
    (90, 164, 173, 1),
    (58, 98, 152, 1),
    (217, 217, 217, 1),
    (217, 217, 217, 1),
    (58, 98, 152, 1),
    (131, 8, 8, 1),
    (244, 202, 20, 1),
    (244, 202, 20, 1),
    (131, 8, 8, 1),
    (44, 77, 134, 1),
    (149, 80, 102, 1),
    (108, 21, 18, 1),
    (33, 31, 31, 1),
    (204, 196, 191, 1),
    (239, 155, 155, 1),
    (181, 208, 253, 1),
    (168, 206, 171, 1),
    (141, 92, 68, 1),
    (233, 167, 77, 1),
    (179, 164, 145, 1),
    (95, 79, 68, 1)]


def figure_string(
        figure=505,
        primary_color=1,
        secondary_color=1,
        width=50,
        height=50,
        x=764,
        y=764,
        stroke=0,
        mirror=0,
        angle=0, ):
    FIGURE_FORMAT = "{figure}.{primary_color}.{secondary_color}.{width}.{height}.{x}.{y}.{stroke}.{mirror}.{angle}"
    return FIGURE_FORMAT.format(
        figure=figure,
        primary_color=primary_color,
        secondary_color=secondary_color,
        width=width,
        height=height,
        x=x,
        y=y,
        stroke=stroke,
        mirror=mirror,
        angle=angle,
    )


def color_distance(left, right):
    r_distance = abs(left[0] - right[0])
    g_distance = abs(left[1] - right[1])
    b_distance = abs(left[2] - right[2])
    return r_distance + g_distance + b_distance


def find_most_similar_color(color):
    similar_color_index = 0
    min_distance = color_distance(color, colors[similar_color_index])
    for existing_color_index, existing_color in enumerate(colors):
        distance = color_distance(color, existing_color)
        if distance <= min_distance:
            min_distance = distance
            similar_color_index = existing_color_index
    return similar_color_index


def image2banner(image_path):
    background_figure = figure_string(width=1500, height=1500, primary_color=116, secondary_color=116)
    figures = [background_figure]

    image = Image.open(image_path)
    pixels = image.load()
    rows_count, columns_count = image.size

    figure_size = 600 / rows_count

    for row_index in range(rows_count):
        for column_index in range(columns_count):
            original_pixel_color = pixels[row_index, column_index]
            if original_pixel_color[3] == 0:
                continue
            x = row_index * figure_size + 764 - 300 + figure_size / 2
            y = column_index * figure_size + 764 - 300 + figure_size / 2
            color = find_most_similar_color(original_pixel_color)
            figures.append(
                figure_string(figure=505, x=x, y=y, width=figure_size, height=figure_size, primary_color=color,
                              secondary_color=0))

    return ".".join(figures)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert an image to the Mount&Blade II Bannerlord banner.')
    parser.add_argument('image_path', type=str, help='path to the image')
    args = parser.parse_args()
    print image2banner(args.image_path)
