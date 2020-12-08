import io
import os
import zipfile
import base64


def zip_font():
    '''
    '''

    with io.BytesIO() as bio:
        with zipfile.ZipFile(bio, 'w') as zf:
            zf.write('./assets/shs-cn-b.ttf', 'shs-cn-b.ttf')
        d = os.path.dirname(__file__)
        p = os.path.join(d, 'font.py')
        r = base64.b64encode(bio.getbuffer())
        with open(p, 'w', encoding='utf8') as writer:
            writer.write(f'zip={r}')


def unzip_font(name):
    '''
    获取字体
    '''

    from . import font
    b = base64.b64decode(font.zip)
    with io.BytesIO(b) as bio:
        with zipfile.ZipFile(bio, 'r') as zf:
            return io.BytesIO(zf.read(name))
