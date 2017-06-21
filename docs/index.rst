ModernGL.ext.textools
=====================

`ModernGL <https://moderngl.readthedocs.io>`_ extension for loading and debugging textures.

- `ModernGL.ext.textools on Github <https://github.com/cprogrammer1994/ModernGL.ext.textools>`_
- `ModernGL.ext.textools on PyPI <https://pypi.python.org/pypi/ModernGL.ext.textools>`_

Install
-------

.. code-block:: sh

	pip install ModernGL.ext.textools

Usage
-----

.. code-block:: python

	import ModernGL
	from ModernGL.ext import textools

Example
-------

.. code-block:: python

	texture = textools.load('brick.jpg', ctx=ctx)
	textools.show(texture)

.. note::
	Some of the operation does not require a Context.
	For example a context is required to downsample textures before read.

Documentation
-------------

.. currentmodule:: ModernGL.ext.textools

.. autofunction:: set_default_context(ctx)
.. autofunction:: load(filename, convert=None, ctx=None) -> ModernGL.Texture
.. autofunction:: image(texture, modify=None, ctx=None) -> PIL.Image
.. autofunction:: show(texture, modify=None, ctx=None)

.. toctree::
   :maxdepth: 2
