import os

if os.environ.get('READTHEDOCS') == 'True':
	from distutils.core import setup

else:
	from setuptools import setup

setup(
	name='ModernGL.ext.textools',
	version='0.2.0',
	author='Szabolcs Dombi',
	author_email='cprogrammer1994@gmail.com',
	description='ModernGL extension for handling textures easily',
	url='https://github.com/cprogrammer1994/ModernGL.ext.textools',
	license='MIT',
	packages=['ModernGL.ext.textools'],
	install_requires=['ModernGL', 'Pillow', 'numpy'],
	platforms=['any'],
)
