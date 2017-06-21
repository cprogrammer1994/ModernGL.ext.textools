'''
    ModernGL extension
'''

import logging
import struct

import ModernGL
from PIL import Image
import numpy as np

__all__ = [
    'set_default_context',
    'load',
    'image',
    'show',
]

log = logging.getLogger('ModernGL.ext.textools')

lookup_components = {
    'L': 1,
    'RGB': 3,
    'RGBA': 4,
}

lookup_mode = {
    1: 'L',
    2: 'RGB',
    3: 'RGB',
    4: 'RGBA',
}

default_context = None


def clampi(x):
    if x < 0:
        return 0

    if x > 255:
        return 255

    return int(x)


def clampf(x):
    if x < 0.0:
        return 0.0

    if x > 1.0:
        return 1.0

    return int(x * 255.0)


def set_default_context(ctx) -> None:
    '''
        Set the default context.

        Args:
            ctx (:py:class:`ModernGL.Context`): The Context to use when needed.

        Examples:

            .. code-block:: python

                import ModernGL
                from ModernGL.ext import textools

                ctx = ModernGL.create_standalone_context()
                # ctx = ModernGL.create_context()

                textools.set_default_context(ctx)

                texture = textools.load('brick.jpg')
                textools.show(texture)
    '''
    global default_context
    default_context = ctx


def load(filename, convert=None, ctx=None) -> ModernGL.Texture:
    '''
        Load a texture. If ctx is ``None`` the default_context is used.

        Args:
            filename (str): The name of the file to load.

        Keyword Args:
            convert (str): Convert the texture before loading. Possible values are: ('L', 'RGB', 'RGBA')
            ctx (:py:class:`ModernGL.Context`): The Context to use for loading the texture.

        Returns:
            :py:class:`ModernGL.Texture`: The texture.

        Examples:

            .. code-block:: python

                import ModernGL
                from ModernGL.ext import textools

                ctx = ModernGL.create_standalone_context()
                # ctx = ModernGL.create_context()

                texture = textools.load('brick.jpg', ctx=ctx)
                texture.use()
    '''

    if ctx is None:
        ctx = default_context
        if ctx is None:
            raise Exception('no context')

    img = Image.open(filename)

    if convert is not None:
        img = img.convert(convert)

    components = lookup_components.get(img.mode, None)

    if not components:
        img = img.convert('RGB')
        components = 3

    return ctx.texture(img.size, components, img.tobytes())


def image(texture, modify=None, ctx=None) -> Image:
    '''
        Read a texture to a Pillow Image. If ctx is ``None`` the default_context is used.

        Args:
            texture (:py:class:`ModernGL.Texture`): The texture to read.

        Keyword Args:
            modify (lambda): Modify the color values before storing them in the Image.
            ctx (:py:class:`ModernGL.Context`): The Context to use for loading the texture.

        Returns:
            :py:class:`Image`: The image.

        Examples:

            .. code-block:: python

                import ModernGL
                from ModernGL.ext import textools

                ctx = ModernGL.create_standalone_context()
                # ctx = ModernGL.create_context()

                texture = textools.load('brick.jpg', ctx=ctx)
                img = textools.image(texture)
                img.save('texture.png')
    '''

    if ctx is None:
        ctx = default_context

    if not texture.samples:

        if modify is None:
            modify = lambda x: x

        mode = lookup_mode[texture.components]

        if texture.floats:
            array = np.frombuffer(texture.read(), 'float32')
            clamp = clampf

        else:
            array = np.frombuffer(texture.read(), 'uint8')
            clamp = clampi

        pixels = np.array([clamp(modify(x)) for x in array], dtype='uint8').tobytes()

        if texture.components == 2:
            pixels = b''.join(pixels[i : i + 2] + b'\x00' for i in range(0, len(pixels), 2))

        return Image.frombytes(mode, texture.size, pixels)

    else:
        if ctx is None:
            raise Exception('no context')

        if texture.depth:
            raise NotImplementedError('not yet implemented')

        new_texture = ctx.texture(texture.size, texture.components, floats=texture.floats)

        fbo1 = ctx.framebuffer(texture)
        fbo2 = ctx.framebuffer(new_texture)

        ctx.copy_framebuffer(fbo2, fbo1)

        result = image(new_texture, modify)

        fbo1.release()
        fbo2.release()

        new_texture.release()

        return result


def show(texture, modify=None, ctx=None) -> None:
    '''
        Show the texture using Pillow. If ctx is ``None`` the default_context is used.

        Args:
            texture (:py:class:`ModernGL.Texture`): The texture to show.

        Keyword Args:
            modify (lambda): Modify the color values before storing them in the Image.
            ctx (:py:class:`ModernGL.Context`): The Context to use for loading the texture.

        Examples:

            .. code-block:: python

                import ModernGL
                from ModernGL.ext import textools

                ctx = ModernGL.create_standalone_context()
                # ctx = ModernGL.create_context()

                texture = textools.load('brick.jpg', ctx=ctx)
                textools.show(texture)
    '''

    image(texture, modify=modify, ctx=ctx).show()
