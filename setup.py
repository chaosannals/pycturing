import setuptools
from pycturing.asset import zip_font

def load_content(path):
    with open(path, 'r', encoding='utf8') as reader:
        return reader.read()

zip_font()

setuptools.setup(
    name='pycturing',
    version='0.0.1',
    description='yet a captcha library',
    long_description=load_content('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/chenshenchao/pycturing',
    keywords='pycturing captcha',
    license='MIT',
    author='chenshenchao',
    author_email='chenshenchao@outlook.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'pillow>=8.0.1',
    ]
)
