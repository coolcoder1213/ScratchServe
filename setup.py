from setuptools import setup, find_packages
import codecs




VERSION = '0.8.0'
DESCRIPTION = 'ScratchServe - API Wrapper For scratch.mit.edu'
LONG_DESCRIPTION = DESCRIPTION

setup(name="ScratchServe",
      version=VERSION,
      author="coolcoder1213",
      author_contact="https://scratch.mit.eu/users/coolcoder1213/",
      description=DESCRIPTION,
      long_description_content_type="text/markdown",
      long_description=open('README.md').read(),
      packages=find_packages(),
      install_requires=["websocket-client", "numpy", "requests"],
      keywords=[
          'Scratch API', 'ScratchServe', 'Scratch API Python', 'Scrath Python',
          'Scratch API Wrapper', 'Scratch', 'Scratch Cloud',
          'Scratch Cloud Variables', 'Cloud Variables'
      ],
      url='https://github.com/coolcoder1213/ScratchServe',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ])
