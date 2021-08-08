import setuptools
from ran import fs, pkg

pkg.save('pycturing/asset/font.py', zip='assets/shs-cn-b.ttf')

setuptools.setup(
    name='pycturing',
    version='0.0.3',
    description='yet a captcha library',
    long_description=fs.load('readme.md'),
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
        'ran>=0.0.5',
    ]
)
