import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))

import ModernGL
from ModernGL.ext import textools

import numpy as np

ctx = ModernGL.create_standalone_context()

# Simple

texture1 = textools.load('brick.jpg', ctx=ctx)
textools.show(texture1)

# Red Green

texture2 = ctx.texture((256, 256), 2, b'\xFF\x80' * 256 * 256)
textools.show(texture2)

# Multisample

texture3 = ctx.texture((256, 256), 3, samples=2)

fbo1 = ctx.framebuffer(texture1)
fbo2 = ctx.framebuffer(texture3)
ctx.copy_framebuffer(fbo2, fbo1)

textools.show(texture3, ctx=ctx)

# Floats

a = np.array([(x * x + y * y) for x in range(256) for y in range(256)])
a = np.sin(np.sqrt(a) / 10.0).astype('float32')

texture4 = ctx.texture((256, 256), 1, a.tobytes(), floats=True)

textools.show(texture4)
textools.show(texture4, modify=lambda x: x * 0.3 + 0.5)
