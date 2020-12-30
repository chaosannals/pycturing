import math
from PIL import Image, ImageFont
from ran import pkg
from ..asset import unzip_font
from .util import draw_char
from ..util import roll_point, roll_text, roll_rgba, vague_float


class TextPycturing:
    '''
    文本型的验证码
    '''

    def __init__(self, **kws):
        '''
        '''

        self.length = kws.get('length', 6)
        self.font_size = kws.get('font_size', 28)
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

    def draw(self):
        '''
        绘制。
        '''

        height = math.ceil(self.font_size * 2)
        width = math.ceil(self.length * height * 0.6)
        size = (width, height)
        image = Image.new(mode="RGBA", size=size, color=(243, 251, 254, 255))
        image = self.noise.draw(image)
        color = roll_rgba(255)
        text = roll_text(self.length)
        for i, code in enumerate(text):
            left = int(self.font_size * vague_float(i, 0.2))
            item = draw_char(code, self.font, color)
            temp = Image.new(mode="RGBA", size=image.size)
            temp.paste(item, box=(left, 0))
            image = Image.alpha_composite(image, temp)
        return image, text

    def save(self, path):
        '''
        保存
        '''

        with open(path, 'wb') as writer:
            image, text = self.draw()
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
