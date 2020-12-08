import math
import random
from PIL import Image, ImageDraw


def draw_char(text, font, color):
    '''
    绘制字符。
    '''

    w = int(font.size * 2)
    h = int(font.size * 2)
    size = (w, h)
    position = (
        math.ceil(w * 0.3),
        math.ceil(h * 0.05)
    )
    image = Image.new(mode="RGBA", size=size)
    draw = ImageDraw.Draw(image)
    draw.text(position, text, color, font=font)
    angle = random.randint(-50, 50)
    return image.rotate(angle, expand=1, resample=Image.BILINEAR)
