""""""
from PIL import Image

import numpy

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

PALETTE_TEXT = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

PALETTE_EMOJIS = {
    "🔴": (255, 0, 0),
    "🟠": (255, 165, 0),
    "🟡": (255, 255, 0),
    "🟣": (128, 0, 128),
    "🟢": (0, 128, 0),
    "🔵": (0, 0, 255),
    "⚪": (255, 255, 255),
    "⚫": (0, 0, 0)
}

PALETTE = PALETTE_EMOJIS

# Numpy version patch for colormath:
# AttributeError: module 'numpy' has no attribute 'asscalar'. Did you mean: 'isscalar'?
def patch_asscalar(a): return a.item()
setattr(numpy, "asscalar", patch_asscalar)


def euclidian_color_distance(rgb1, rgb2):
    return ((rgb1[0] - rgb2[0]) ** 2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) ** 2) ** 0.5



def color_distance(rgb1, rgb2):
    # Convert each (R,G,B) to a Lab color
    # is_upscaled=True -> 0-255 range
    color1 = sRGBColor(rgb1[0], rgb1[1], rgb1[2], is_upscaled=True)
    color2 = sRGBColor(rgb2[0], rgb2[1], rgb2[2], is_upscaled=True)

    lab1 = convert_color(color1, LabColor)
    lab2 = convert_color(color2, LabColor)

    # Delta E 2000 is a decent measure of "human perceived" difference
    # See also: zschuessler.github.io/DeltaE/learn/
    return delta_e_cie2000(lab1, lab2)



def closest_palette_color(rgb):
    """
    Given an (R, G, B) tuple, find the closest color from our PALETTE.
    Returns the palette color name (e.g. "red" [or the associated color dot emoji]) or (name, distance) if needed.
    """
    best_name = None
    best_dist = float('inf')
    for name, palette_rgb in PALETTE.items():
        dist = color_distance(rgb, palette_rgb)
        if dist < best_dist:
            best_dist = dist
            best_name = name
    return best_name


def reduce_image_to_palette(input_path, output_width=40, output_height=30):
    if input_path.startswith("http"):
        import requests
        from io import BytesIO
        response = requests.get(input_path)
        img = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        img = Image.open(input_path).convert("RGB")
        img = img.resize((output_width, output_height), Image.Resampling.LANCZOS)

    color_grid = []
    for y in range(output_height):
        row_colors = []
        for x in range(output_width):
            r, g, b = img.getpixel((x, y))
            row_colors.append(closest_palette_color((r, g, b)))
        color_grid.append(row_colors)

    return color_grid



def conv(img_path: str, width: int = 40, height: int = 30):
    return reduce_image_to_palette(img_path, width, height)

