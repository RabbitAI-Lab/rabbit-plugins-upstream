"""Place the picture as a rounded card with a soft shadow on a decorative background."""
import random
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

# Mesh gradients. Each blob is a centre (x as a fraction of the width, y of the height),
# a radius as a fraction of the width and an sRGB colour.
PRESETS = {
    'sunset': [(.0, .0, .55, '#ff6a3d'), (1., .15, .5, '#ff4f8b'),
               (.15, 1., .6, '#7b3fe4'), (.95, .9, .5, '#ffb347'), (.5, .5, .35, '#ff7a6b')],
    'spring': [(.0, .0, .55, '#c6f36b'), (1., .1, .5, '#3fd8a2'),
               (.1, .95, .55, '#1fa38a'), (.95, 1., .55, '#f7e463'), (.5, .5, .3, '#8ee08a')],
    'ocean': [(.5, .45, .45, '#9fd8ff'), (.0, .0, .6, '#2d6cdf'),
              (1., 1., .6, '#1b2f8a'), (1., .0, .5, '#4aa3ff'), (.0, 1., .5, '#3a3fb8')],
    'dusk': [(.0, .0, .6, '#2a1559'), (1., .2, .5, '#5b2bd6'),
             (.2, 1., .6, '#0f1b4d'), (.9, .95, .45, '#c2378f'), (.5, .5, .4, '#1d1440')],
}
# Converts a still RGBA layer to the picture's BT.709 limited-range YUV. Left to FFmpeg,
# the conversion would use BT.601 and shift the background's colours.
TO_VIDEO = 'scale=out_color_matrix=bt709:out_range=tv,format=yuva420p'


def resolve(spec):
    """Return the kind and value a --background argument names."""
    from PIL import ImageColor

    if spec == 'blur':
        return 'blur', None
    if spec == 'random':
        spec = random.choice(sorted(PRESETS))
        print(f'Background preset: {spec}', file=sys.stderr)
    if spec in PRESETS:
        return 'preset', spec
    path = Path(spec).expanduser()
    if path.is_file():
        return 'image', path.resolve()
    try:
        return 'colour', ImageColor.getrgb(spec)[:3]
    except ValueError:
        raise ValueError(f'Unknown background {spec!r}. Use a preset ({", ".join(PRESETS)} or '
                         'random), a colour such as #efe9df, an image file or blur.') from None


def card(width, height, padding, radius):
    """Left, top, width, height and corner radius of the card, all even except the radius.

    Padding and radius are percentages of the frame's short side, so a portrait and a
    landscape frame get the same margin."""
    side = min(width, height)
    margin = side*padding/100
    scale = min((width-2*margin)/width, (height-2*margin)/height)
    w, h = 2*round(width*scale/2), 2*round(height*scale/2)
    return (width-w)//4*2, (height-h)//4*2, w, h, round(side*radius/100)


def mesh(blobs, width, height):
    from PIL import Image, ImageColor

    # Blending on a coarse grid and enlarging it keeps the gradient smooth.
    sw, sh = max(2, width//8), max(2, height//8)
    y, x = np.mgrid[0:sh, 0:sw]
    x, y = x/(sw-1), y/(sh-1)*height/width
    acc, total = np.zeros((sh, sw, 3)), np.zeros((sh, sw, 1))
    for bx, by, r, colour in blobs:
        weight = np.exp(-((x-bx)**2+(y-by*height/width)**2)/(2*(r*.6)**2))[..., None]+1e-6
        acc += weight*np.array(ImageColor.getrgb(colour))
        total += weight
    small = Image.fromarray(np.uint8(np.clip(acc/total, 0, 255)))
    big = np.asarray(small.resize((width, height), Image.BICUBIC), dtype=float)
    # Grain breaks up the 8-bit steps that H.264 would otherwise turn into visible bands.
    grain = np.random.default_rng(0).normal(0, 1.6, (height, width, 1))
    return Image.fromarray(np.uint8(np.clip(big+grain, 0, 255)))


def picture(kind, value, width, height, work):
    from PIL import Image, ImageOps, UnidentifiedImageError

    if kind == 'preset':
        return mesh(PRESETS[value], width, height)
    if kind == 'colour':
        return Image.new('RGB', (width, height), value)
    try:
        image = Image.open(value)
    except UnidentifiedImageError:
        # Pillow cannot read HEIC, the format of the macOS wallpapers.
        converted = shutil.which('sips') and subprocess.run(
            ['sips', '-s', 'format', 'png', str(value), '--out', str(work/'wallpaper.png')],
            capture_output=True).returncode == 0
        if not converted:
            raise ValueError(f'Cannot read {value.name} as an image; convert it to PNG or JPEG.') from None
        image = Image.open(work/'wallpaper.png')
    return ImageOps.fit(ImageOps.exif_transpose(image).convert('RGB'), (width, height), Image.LANCZOS)


def prepare(kind, value, width, height, box, work):
    """Write the still layers into work and return their names with the filter chain.

    The chain continues the picture's chain and leaves the composed frame open. {0} and
    {1} stand for the input indices of the stills, which loop for the whole run."""
    from PIL import Image, ImageDraw, ImageFilter

    x, y, w, h, r = box
    side = min(width, height)
    mask = Image.new('L', (w*4, h*4))
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w*4-1, h*4-1), r*4, fill=255)
    mask = mask.resize((w, h), Image.LANCZOS)
    drop = round(side*.018)
    shade = Image.new('L', (width, height))
    ImageDraw.Draw(shade).rounded_rectangle((x, y+drop, x+w, y+h+drop), r, fill=150)
    shade = shade.filter(ImageFilter.GaussianBlur(side*.03))
    if kind == 'blur':
        # The picture itself, blurred at a quarter size and darkened, fills the frame.
        # Only the corners and shadow need stills here, as the background moves.
        shadow = Image.new('RGBA', (width, height))
        shadow.putalpha(shade)
        shadow.save(work/'shadow.png')
        mask.save(work/'mask.png')
        qw, qh = 2*max(1, round(width/8)), 2*max(1, round(height/8))
        return ['shadow.png', 'mask.png'], (
            f',split[bgpic][bgsrc];[bgsrc]scale={qw}:{qh},gblur=sigma={side*.05/4:.2f},'
            f'scale={width}:{height},lutyuv=y=16+(val-16)*0.75:u=128+(val-128)*0.75:'
            f'v=128+(val-128)*0.75[bgblur];[{{0}}:v]{TO_VIDEO}[bgshade];'
            '[bgblur][bgshade]overlay=shortest=1[bgback];'
            f'[bgpic]scale={w}:{h}[bgcard];[{{1}}:v]format=gray[bgmask];'
            f'[bgcard][bgmask]alphamerge[bgfront];[bgback][bgfront]overlay={x}:{y}:shortest=1')
    # A still background goes on top as one layer, with the shadow drawn in and a
    # transparent card-shaped hole that the padded picture shows through.
    layer = picture(kind, value, width, height, work)
    layer.paste((0, 0, 0), (0, 0), shade)
    hole = Image.new('L', (width, height), 255)
    hole.paste(0, (x, y), mask)
    layer.putalpha(hole)
    layer.save(work/'background.png')
    return ['background.png'], (
        f',scale={w}:{h},pad={width}:{height}:{x}:{y}[bgcard];'
        f'[{{0}}:v]{TO_VIDEO}[bglayer];[bgcard][bglayer]overlay=shortest=1')
