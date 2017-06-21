# ModernGL.ext.textools

[ModernGL](https://github.com/cprogrammer1994/ModernGL) extension for handling textures easily

- [Documentation](http://modernglexttextools.readthedocs.io)
- [ModernGL.ext.textools on PyPI](https://pypi.python.org/pypi/ModernGL.ext.textools)

## Usage

```python
import ModernGL
from ModernGL.ext import textools
```

## Functions

```python
def set_default_context(ctx):
def load(filename, convert=None, ctx=None) -> ModernGL.Texture:
def image(texture, modify=None, ctx=None) -> Image:
def show(texture, modify=None, ctx=None) -> None:
```

## Examples

### Simple

```python
texture1 = textools.load('brick.jpg', ctx=ctx)
textools.show(texture1)
```

![Simple](.github/output1.jpg)

### Red Green

```python
texture2 = ctx.texture((256, 256), 2, b'\xFF\x80' * 256 * 256)
textools.show(texture2)
```

![Red Green](.github/output2.png)

### Multisample

```python
texture3 = ctx.texture((256, 256), 3, samples=2)

fbo1 = ctx.framebuffer(texture1)
fbo2 = ctx.framebuffer(texture3)
ctx.copy_framebuffer(fbo2, fbo1)

textools.show(texture3, ctx=ctx)
```

![Multisample](.github/output3.jpg)

### Floats

```python
a = np.array([(x * x + y * y) for x in range(256) for y in range(256)])
a = np.sin(np.sqrt(a) / 10.0).astype('float32')

texture4 = ctx.texture((256, 256), 1, a.tobytes(), floats=True)

textools.show(texture4)
```

![Floats 1](.github/output4.png)

```python
textools.show(texture4, modify=lambda x: x * 0.3 + 0.5)
```

![Floats 2](.github/output5.png)