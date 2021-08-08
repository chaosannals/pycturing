# [pycturing](https://github.com/chenshenchao/pycturing)

## 安装

```bash
pip install pycturing
```

## 使用

```python
from pycturing.util import roll_text
from pycturing.text import TextPycturing

tp = TextPycturing()

# 随机地生成图像和答案
p1 = './debug/a.png'
r1 = tp.save(p1)
print(f'result 1: {r1} => {p1}')

# 把答案写到文件名里面
r2 = roll_text(length=5)
p2 = f'./debug/{r2}.png'
tp.save(p2, text=r2)
print(f'result 2: {r2} => {p2}')

```
