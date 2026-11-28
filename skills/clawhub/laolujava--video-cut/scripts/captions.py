"""Read, remap and draw prepared SubRip cues on the final frame grid."""
import re
from fractions import Fraction
from pathlib import Path

# Burn-in looks. Stroke and shadow sizes are fractions of the font size, so a style
# looks the same at every frame width; stroke counts toward the width that must fit.
STYLES = {
    'box': {'fill': (255, 255, 255), 'box': (16, 18, 20, 205)},
    'white-box': {'fill': (20, 20, 20), 'box': (255, 255, 255, 235)},
    'yellow-box': {'fill': (20, 20, 20), 'box': (255, 214, 0, 255)},
    'outline': {'fill': (255, 255, 255), 'stroke': (0, 0, 0), 'stroke_width': .07},
    'yellow-outline': {'fill': (255, 222, 0), 'stroke': (0, 0, 0), 'stroke_width': .07},
    'shadow': {'fill': (255, 255, 255), 'stroke': (0, 0, 0), 'stroke_width': .03,
               'shadow': (0, 0, 0, 200)},
}


def read_srt(path, fps):
    def frame(code):
        match = re.fullmatch(r'(\d+):(\d{2}):(\d{2})[,.](\d{3})', code)
        if not match:
            raise ValueError(f"Invalid SRT time: {code}")
        h, m, s, ms = map(int, match.groups())
        return round((3600*h + 60*m + s + Fraction(ms, 1000)) * fps)

    result = []
    for block in re.split(r'\n[ \t]*\n', path.read_text(encoding='utf-8-sig').strip()):
        _, times, text = block.split('\n', 2)
        start, end = map(frame, times.strip().split(' --> '))
        if end <= start or (result and result[-1][1] > start):
            raise ValueError(f"Empty or overlapping subtitle: {times}")
        result.append((start, end, text))
    return result


def remap(cues, spans):
    result = []
    offset = 0
    for start, end in spans:
        for left, right, text in cues:
            a, b = max(left, start), min(right, end)
            if a >= b:
                continue
            at, stop = offset + a-start, offset + b-start
            if result and result[-1][1:] == (at, text):
                result[-1] = (result[-1][0], stop, text)
            else:
                result.append((at, stop, text))
        offset += end-start
    return result


def retime(cues, speed):
    """Move cues onto the frame grid of a cut played at this speed."""
    scaled = ((round(a/speed), round(b/speed), text) for a, b, text in cues)
    return [cue for cue in scaled if cue[0] < cue[1]]


def write_srt(path, cues, fps):
    def stamp(frame):
        ms = round(frame*1000/fps)
        return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
    path.write_text('\n\n'.join(
        f'{i}\n{stamp(a)} --> {stamp(b)}\n{text}'
        for i, (a, b, text) in enumerate(cues, 1))+'\n', encoding='utf-8')


def missing_glyphs(font_path, font_index, cues):
    """Characters the font would draw as its missing-glyph box."""
    from PIL import Image, ImageDraw, ImageFont

    font = ImageFont.truetype(str(font_path), 48, index=font_index)

    def shape(char):
        image = Image.new('L', (96, 96))
        ImageDraw.Draw(image).text((24, 24), char, font=font, fill=255)
        return image.tobytes()

    # No font maps this private-use code point, so it draws the missing-glyph shape.
    blank = shape('\U0010fffd')
    return sorted({c for _, _, text in cues for c in text if not c.isspace() and shape(c) == blank})


def strip_top(width, height):
    """Top of the caption strip: below the face on portrait, near the bottom on landscape."""
    if width > height:
        return height-max(12, round(height*.15))-round(height*.02)
    return int(height*.695)


def overlays(folder, cues, first, last, fps, font_path, font_index, width, height, style='box'):
    from PIL import Image, ImageDraw, ImageFilter, ImageFont

    look = STYLES[style]
    folder.mkdir()
    strip = max(12, round(height*.15))
    # Type is sized from the width, or on landscape from the height, so a wide frame
    # gets subtitles of about 5% of its height rather than outsized ones.
    span = min(width, height*25/24)
    listing = ['ffconcat version 1.0']
    position = first
    index = 0

    def card(text, duration):
        nonlocal index
        if duration <= 0:
            return
        image = Image.new('RGBA', (width, strip))
        if text:
            d = ImageDraw.Draw(image)
            for size in range(max(12, round(span*.048)), 6, -1):
                font = ImageFont.truetype(str(font_path), size, index=font_index)
                stroke = round(size*look.get('stroke_width', 0))
                # Pillow spaces lines by the glyphs alone, so stroked lines would touch.
                spacing = 4+2*stroke
                b = d.multiline_textbbox((0, 0), text, font=font, spacing=spacing,
                                         stroke_width=stroke)
                w, h = b[2]-b[0], b[3]-b[1]
                if w < width*.82 and h < strip*.84:
                    break
            if size < max(7, round(span*.035)):
                raise ValueError(f'Split the cue for mobile readability: {text}')

            # Centre each line on its visible pixels. Pillow centres advance widths, so a
            # line ending in full-width punctuation such as “。” would sit left of centre.
            def ink(line):
                l, t, r, bottom = font.getbbox(line, stroke_width=stroke)
                probe = Image.new('L', (r-l+2, bottom-t+2))
                ImageDraw.Draw(probe).text((1-l, 1-t), line, font=font, fill=255,
                                           stroke_width=stroke, stroke_fill=255)
                box = probe.getbbox()
                return (box[0]+l-1, box[2]+l-1) if box else (0, 0)

            y = (strip-h)//2
            pitch = font.getbbox('A', stroke_width=stroke)[3]+stroke+spacing  # as Pillow
            lines = []
            for i, line in enumerate(text.split('\n')):
                left, right = ink(line)
                x = round((width-left-right)/2)
                lines.append((x, y-b[1]+i*pitch, line, x+left, x+right))
            if 'box' in look:
                px, py = max(2, size//3), max(2, size//5)
                x0, x1 = min(e[3] for e in lines), max(e[4] for e in lines)
                d.rounded_rectangle((x0-px, y-py, x1+px, y+h+py), radius=py, fill=look['box'])

            def write(draw, fill, stroke_fill, shift=0):
                for x, top, line, *_ in lines:
                    draw.text((x+shift, top+shift), line, font=font, fill=fill,
                              stroke_width=stroke, stroke_fill=stroke_fill)

            if 'shadow' in look:
                shade = Image.new('RGBA', image.size)
                write(ImageDraw.Draw(shade), look['shadow'], look['shadow'], max(1, round(size*.06)))
                image.alpha_composite(shade.filter(ImageFilter.GaussianBlur(size*.08)))
            write(d, look['fill'], look.get('stroke'))
        name = f'cue{index}.png'
        image.save(folder/name)
        listing.extend([f"file '{name}'", f'option framerate {fps}',
                        f'duration {float(duration/fps):.9f}'])
        index += 1

    for start, end, text in cues:
        a, b = max(first, start), min(last, end)
        if a < b:
            card('', a-position)
            card(text, b-a)
            position = b
    card('', last-position)
    listing.extend([f"file 'cue{index-1}.png'", f'option framerate {fps}'])
    manifest = folder/'captions.ffconcat'
    manifest.write_text('\n'.join(listing)+'\n')
    return manifest
