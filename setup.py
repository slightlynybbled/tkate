from setuptools import setup
from tkmats import __version__

# read the long description
with open('readme.md', 'r') as f:
    long_description = f.read()

# read the requirements.txt
with open('requirements.txt', 'r') as f:
    requirements = [s.strip() for s in f.readlines()]
    requirements = [r for r in requirements if r]

setup_attributes = {
    'name': 'tkate',
    'version': __version__,
    'description': 'A tkinter-based front-end GUI for trigger and monitoring hardware tests based on the ATE package',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/slightlynybbled/tkate',
    'author': 'Jason R. Jones',
    'author_email': 'slightlynybbled@gmail.com',
    'license': 'MIT',
    'packages': ['tkate'],
    'python_requires': '>=3.6.0',
    'install_requires': requirements,
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    'zip_safe': False
}

setup(**setup_attributes)
