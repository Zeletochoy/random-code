from setuptools import find_packages, setup


setup(
    name='random_code',
    description='Random stuff',
    url='https://github.com/zeletochoy/random-code.git',
    author='Antoine Lecubin',
    author_email='antoinelecubin@msn.com',
    packages=find_packages(),
    license="beerware",
    install_requires=[
        'click',
    ],
    entry_points={
        "console_scripts": [
            "emoji-flag=random_code.emoji_flag:cli",
        ],
    },
)
