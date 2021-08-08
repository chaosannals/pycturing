import os
import math
from PIL import Image, ImageFont
from ran import pkg
from .util import draw_char
from ..util import roll_point, roll_text, roll_rgba, vague_float


class TextPycturing:
    '''
    文本型的验证码
    '''

    def __init__(self, font_size=28):
        '''
        初始化。
        '''

        self.font_size = font_size
        self.font = ImageFont.truetype(
            pkg.load('pycturing.asset.font', 'zip'),
            self.font_size
        )
        self.noise = TextNoise(
            font=ImageFont.truetype(
                pkg.load('pycturing.asset.font', 'zip'),
                math.ceil(self.font_size / 3)
            )
        )

    def draw(self, text=None, length=6):
        '''
        绘制。
        '''

        if isinstance(text, str):
            length = length
        else:
            text = roll_text(length)

        height = math.ceil(self.font_size * 2)
        width = math.ceil(length * height * 0.6)
        size = (width, height)
        image = Image.new(mode="RGBA", size=size, color=(243, 251, 254, 255))
        image = self.noise.draw(image)
        color = roll_rgba(255)
        for i, code in enumerate(text):
            left = int(self.font_size * vague_float(i, 0.2))
            item = draw_char(code, self.font, color)
            temp = Image.new(mode="RGBA", size=image.size)
            temp.paste(item, box=(left, 0))
            image = Image.alpha_composite(image, temp)
        return image, text

    def save(self, path, text=None, length=6):
        '''
        保存
        '''

        d = os.path.dirname(path)
        if not os.path.isdir(d):
            os.makedirs(d)

        with open(path, 'wb') as writer:
            image, text = self.draw(text, length)
            image.save(writer)
            return text


class TextNoise:
    '''
    文本型干扰
    '''

    def __init__(self, **kws):
        '''
        初始化
        '''

        self.font = kws.get('font')
        self.count = kws.get('count', 100)

    def draw(self, image):
        '''
        在图片上绘制干扰文本
        '''

        w = image.size[0] - 1
        h = image.size[1] - 1
        for code in roll_text(self.count):
            ci = draw_char(code, self.font, roll_rgba())
            temp = Image.new(mode="RGBA", size=image.size)
            temp.paste(ci, box=roll_point(0, 0, w, h))
            image = Image.alpha_composite(image, temp)
        return image
