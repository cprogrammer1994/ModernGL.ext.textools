from setuptools import setup

package = 'ModernGL.ext.textools'
version = '0.1.0'

setup(
	name=package,
	version=version,
	author='Szabolcs Dombi',
	author_email='cprogrammer1994@gmail.com',
	description='ModernGL extension for handling textures easily',
	url='https://github.com/cprogrammer1994/ModernGL.ext.textools',
	license='MIT',
	packages=[package],
	install_requires=['ModernGL', 'Pillow', 'numpy'],
	platforms=['any'],
)
