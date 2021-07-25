
from setuptools import setup, find_packages

setup(
    name='q-dungeon-maps',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Dungeon maps with Q-Learning algorithm',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'matplotlib'],
    url='https://github.com/mwebr/QDungeonMaps',
    author='Marian Weber',
    author_email='marian.weber@pm.me'
)
