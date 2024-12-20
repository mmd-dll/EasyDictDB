from setuptools import setup, find_packages

setup(
    name='EasyDictDB', 
    version='1.1.0',
    author='mohammad reza',
    author_email='id.suzuya@gmail.com',
    description='A simple library to save and load Python dictionaries in SQLite.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mmd-dll/EasyDictDB',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
