import io
import os.path
from setuptools import setup

"""VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloworld/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()"""

setup(
    name = "convertvideo",        # what you want to call the archive/egg
    # packages=["mp4_to_mp3"],    # top-level python modules you can import like
                                #   'import foo'
    # dependency_links = [],      # custom links to a specific project
    # install_requires=[],
    # extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    # package_data = {"helloworld": ["VERSION.txt"]},
    author="Hello Test",
    author_email = "testing123@gmail.com",
    description = "This is a Test",
    license = "Apache 2.0",
    keywords= "test testing test123",
    url = "http://github.com/X05HUA/Pac-Git-Tests"
)
