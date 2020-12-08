import random


def roll_point(top, left, right, bottom):
    '''
    位置
    '''

    x = random.randint(left, right)
    y = random.randint(top, bottom)
    return (x, y)


def roll_rgba(alpth=None):
    '''
    随机的 RGBA 颜色。
    '''

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = random.randint(0, 255) if alpth == None else alpth
    return (r, g, b, a)


def roll_text(length=6, charset='2345678abcdefhijkmnpqrstuvwxyz'):
    '''
    随机字符串
    '''

    result = []
    max_index = len(charset) - 1
    for _ in range(length):
        i = random.randint(0, max_index)
        result.append(charset[i])
    return ''.join(result)


def vague_float(value, scope):
    '''
    让数在一定范围内模糊浮动。
    '''

    ps = random.random() * scope
    ns = random.random() * scope
    return value + ps - ns
