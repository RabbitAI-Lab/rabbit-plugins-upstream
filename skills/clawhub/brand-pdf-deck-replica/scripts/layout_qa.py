# -*- coding: utf-8 -*-
"""版面体检：逐页检测右侧/底部出血带是否有内容越界，并统计墨迹与彩色覆盖率。"""
import glob
import os
import subprocess
import sys

from PIL import Image

PDF = sys.argv[1] if len(sys.argv) > 1 else 'out/blackrock_bii_2026_outlook.pdf'
OUT = 'out/prev2'
os.makedirs(OUT, exist_ok=True)
for f in glob.glob(os.path.join(OUT, '*.png')):
    os.remove(f)
subprocess.run(['pdftoppm', '-r', '130', '-png', PDF, os.path.join(OUT, 'p')], check=True)


def ink_rect(px, w, h, x0, y0, x1, y1):
    sx, sy = w / 792.0, h / 594.0
    c = 0
    for y in range(int(y0 * sy), min(int(y1 * sy), h)):
        for x in range(int(x0 * sx), min(int(x1 * sx), w)):
            r, g, b = px[x, y]
            if r < 245 or g < 245 or b < 245:
                c += 1
    return c


print('%-10s %8s %8s %8s %8s   %s' % ('page', 'ink%', 'color%', 'right', 'bottom', 'verdict'))
for p in sorted(glob.glob(os.path.join(OUT, 'p-*.png'))):
    im = Image.open(p).convert('RGB')
    w, h = im.size
    px = im.load()
    tot = n_ink = n_col = 0
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            r, g, b = px[x, y]
            tot += 1
            if r < 250 or g < 250 or b < 250:
                n_ink += 1
            if max(r, g, b) - min(r, g, b) > 28:
                n_col += 1
    right = ink_rect(px, w, h, 774, 0, 792, 594)
    bottom = ink_rect(px, w, h, 0, 580, 792, 594)
    verdict = []
    if right > 60:
        verdict.append('R-BLEED')
    if bottom > 900:
        verdict.append('B-OVERFLOW')
    print('%-10s %7.2f %8.2f %8d %8d   %s'
          % (os.path.basename(p), 100.0 * n_ink / tot, 100.0 * n_col / tot,
             right, bottom, ' '.join(verdict) or 'ok'))
