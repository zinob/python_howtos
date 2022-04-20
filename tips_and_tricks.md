# Run all cells above current in Jupyter Lab

It is a tad bit clunky to "run all cells above current" in Jypyter Lab and there is no single shortcut key for it. 
The best way I have found is the following sequence:
* `Esc` (to exit edit-mode)
* `Shift` + `Home` (to select all cells to the top) **or** `Ctrl/Command` + `A` (to select all cells)
* `Ctrl/Command` + `Enter` (to run all selected cells)

# Filter an image in PIL / PILLOW by exact pixel values

I some-times need to create a pixel-perfect mask for a particular color (pixel value) in an image. This is the best way I have found so far (yes i'm comparing floats using `==` dont cry, it won't help).

```
from PIL import Image, ImageMath

MASK_COLOR = (251, 242, 54)

im = Image.open('my_image.png')
b = Image.new("RGB", (im.width, im.height), color=MASK_COLOR)
mask = ImageMath.eval("convert(256*(float(a) ==  float(b)) ,'L')",a=im,b=b)
```
