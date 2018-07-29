import setuptools
from pyholecli._version import __version__ as version
from pyholecli import name


with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author='Patrick Jennings',
    author_email='patrick@jenningsga.com',
    description='Remote management of a pi.hole instance.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    url='https://github.com/patrickjennings/pyholecli',
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['pyholecli = pyholecli.main:program.run']
    },
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
