from distutils.core import setup
import json
import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
info = open('info.json')
data = json.loads(info.read())

setup(
    name=data['name'],
    packages=['banana_cli', 'banana_cli.process'],
    py_modules=["cli"],
    version=data['version'],
    license=data['license'],
    # Give a short description about your library
    description=data['description'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Erik Dunteman',
    author_email='erik@banana.dev',
    url='https://www.banana.dev',
    keywords=['Banana server', 'HTTP server', 'Banana', 'Framework'],
    setup_requires=['wheel'],
    install_requires=[
        "Click",
        "gitpython",
        "termcolor",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'banana = banana_cli:cli',
        ],
    },
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
