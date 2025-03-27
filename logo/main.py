""""""
from PIL import Image


def parse_hex_color(color_str):
    """
    Convert a hex color code like '#A020F0' to an (R, G, B) tuple.
    Assumes valid input and no alpha channel.
    """
    color_str = color_str.lstrip('#')
    # Split into (R, G, B) as two hex digits each
    return tuple(int(color_str[i:i + 2], 16) for i in (0, 2, 4))


def generate_pixel_image(pixel_array, scale=1, background="#FFFFFF", output_file="pixel_image.png"):
    """
    Generate a PNG image from a 2D array of color codes.

    :param pixel_array: 2D list of strings (hex codes like '#FF0000') or None
    :param scale: integer factor by which to enlarge each "pixel"
    :param background: hex color code for background (if needed)
    :param output_file: output filename (PNG, JPG, etc.)
    """
    # Determine image dimensions based on array size
    height = len(pixel_array)
    width = max(len(row) for row in pixel_array)

    # Create a new image (RGB) with a background color
    img = Image.new("RGB", (width * scale, height * scale), background)

    # Draw each pixel
    for y, row in enumerate(pixel_array):
        for x, color in enumerate(row):
            if color is not None:
                # Convert hex code to an (R, G, B) tuple
                rgb = parse_hex_color(color)
                # Fill in a block of size (scale x scale) for each pixel
                for dy in range(scale):
                    for dx in range(scale):
                        img.putpixel((x * scale + dx, y * scale + dy), rgb)

    # Save the resulting image
    img.save(output_file)

B = '#F0F0F0'
C = '#D38073'

# Purple
D = '#800080'
# Blue
M = '#0000FF'

D = C
# M will be a very similar color but with a different hue
M = '#' + str(hex(int(C[1:], 16) - 0x000080))[2:]


# Orange
O = '#FFA500'

# Tweak this if you need higher resolution (when zoomed in, even though this is a "low resolution" pixel image, it looks blurry when this value is lower).
SCALE = 100


def rotate_matrix(matrix):
    """
    Rotate a 2D matrix (list of lists) by 90 degrees clockwise.
    """
    return list(zip(*matrix[::-1]))


if __name__ == "__main__":
    file_name = "logo.png"

    original_pixel_array = [
        [None, None, None, None, None, None, None],
        [None, C, None, C, None, C, None],
        [None, C, None, C, None, C, None],
        [None, C, C, None, C, C, None],
        [None, None, None, None, None, None, None],
        [None, None, None, C, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # 7x7 D and M logo...
    dm_logo = [
        [D, D, None, None, None, None, None],
        [D, None, D, None, None, None, None],
        [D, None, D, None, None, None, None],
        [D, D, M, None, None, None, M],
        [None, None, M, M, None, M, M],
        [None, None, M, None, M, None, M],
        [None, None, M, None, M, None, M]
    ]

    pixel_array = [
        [D, O, O, C, O, O, M],
        [D, D, None, C, None, M, M],
        [D, None, D, C, M, None, M],
        [D, None, None, C, None, None, M],
        [D, None, D, C, M, None, M],
        [D, D, None, C, None, M, M],
        [D, O, O, C, O, O, M],
    ]

    #pixel_array = rotate_matrix(pixel_array)

    pixel_array = dm_logo

    # Replace None with background color
    for i in range(len(pixel_array)):
        for j in range(len(pixel_array[i])):
            if not pixel_array[i][j]:
                pixel_array[i][j] = B

    generate_pixel_image(pixel_array, scale=SCALE, background="#FFFFFF", output_file=file_name)
    print(f"Image generated: {file_name}")

