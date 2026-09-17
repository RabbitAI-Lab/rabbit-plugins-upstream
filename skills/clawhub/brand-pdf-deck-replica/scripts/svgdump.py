"""SVG/PDF 矢量图形取数器 —— 把 pdftocairo 出的 SVG 解析成几何元素。

坐标系统一说明：
  pdftocairo -svg 的元素常带 transform="matrix(1,0,0,-1,0,594)"（y 翻转）。
  本模块把元素自身 + 所有 <g> 祖先的 transform 依次复合，
  得到与 pdftotext -bbox 完全同源（左上角原点、单位 pt）的坐标。
"""
import re

NUM = r'-?\d+(?:\.\d+)?(?:e-?\d+)?'
NUMRE = re.compile(r'-?\d+(?:\.\d+)?(?:e-?\d+)?')


def nums(s):
    return [float(v) for v in NUMRE.findall(s)]


def pairs(s):
    v = nums(s)
    return list(zip(v[0::2], v[1::2]))


def hexof(c):
    if not c or not c.startswith('rgb'):
        return c
    m = re.findall(r'([\d.]+)%?', c)
    if len(m) == 3:
        return '#%02X%02X%02X' % tuple(round(float(v) * 2.55) for v in m)
    return c


def parse_matrix(t):
    m = re.findall(NUM, t or '')
    if len(m) == 6:
        return tuple(float(v) for v in m)
    return (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def mul(m1, m2):
    """先应用 m2，再应用 m1。"""
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2
    return (a1 * a2 + c1 * b2, b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2, b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1, b1 * e2 + d1 * f2 + f1)


def apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


TAG_RE = re.compile(r'<(/?)(g|path|rect|polyline|polygon|line|image)\b([^>]*?)(/?)>', re.S)


def parse_svg(path):
    """返回 (elements, viewport)。element = dict(tag, attrs, mat, points, bbox)"""
    s = open(path, encoding='utf-8').read()
    vb = re.search(r'viewBox="([^"]+)"', s)
    vp = tuple(float(v) for v in vb.group(1).split()) if vb else None
    # 去掉 defs 段，避免把 clipPath 里的形状当数据
    body = re.sub(r'<defs>.*?</defs>', '', s, flags=re.S)
    stack = [(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)]
    out = []
    for m in TAG_RE.finditer(body):
        closing, tag, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if tag == 'g':
            if closing:
                if len(stack) > 1:
                    stack.pop()
            else:
                tm = re.search(r'transform="([^"]+)"', attrs)
                stack.append(mul(stack[-1], parse_matrix(tm.group(1))) if tm else stack[-1])
            continue
        if closing:
            continue
        mat = stack[-1]
        tm = re.search(r'transform="([^"]+)"', attrs)
        if tm:
            mat = mul(mat, parse_matrix(tm.group(1)))
        d = re.search(r'\sd="([^"]+)"', attrs)
        pts = []
        subs = []
        if d and tag == 'path':
            pts = [apply(mat, x, y) for x, y in pairs(d.group(1))]
            # 同时保留「按 M 分段的子路径」，每段都已应用同一变换，
            # 用于堆叠/分组柱状图按柱取值（务必用变换后的点，否则会踩 flip 不一致的坑）。
            for seg in re.split(r'[Mm]', d.group(1)):
                pr = pairs(seg)
                if len(pr) >= 2:
                    subs.append([apply(mat, x, y) for x, y in pr])
        elif tag in ('polyline', 'polygon'):
            pm = re.search(r'points="([^"]+)"', attrs)
            if pm:
                pts = [apply(mat, x, y) for x, y in pairs(pm.group(1))]
        elif tag == 'rect':
            x = float(re.search(r'\sx="([^"]+)"', attrs).group(1)) if 'x=' in attrs else 0.0
            y = float(re.search(r'\sy="([^"]+)"', attrs).group(1)) if 'y=' in attrs else 0.0
            w = float(re.search(r'width="([^"]+)"', attrs).group(1))
            h = float(re.search(r'height="([^"]+)"', attrs).group(1))
            pts = [apply(mat, x, y), apply(mat, x + w, y + h)]
        elif tag == 'line':
            x1 = float(re.search(r'x1="([^"]+)"', attrs).group(1))
            y1 = float(re.search(r'y1="([^"]+)"', attrs).group(1))
            x2 = float(re.search(r'x2="([^"]+)"', attrs).group(1))
            y2 = float(re.search(r'y2="([^"]+)"', attrs).group(1))
            pts = [apply(mat, x1, y1), apply(mat, x2, y2)]

        st = re.search(r'stroke="([^"]+)"', attrs)
        fi = re.search(r'fill="([^"]+)"', attrs)
        sw = re.search(r'stroke-width="([^"]+)"', attrs)
        el = {
            'tag': tag,
            'stroke': hexof(st.group(1)) if st else None,
            'fill': hexof(fi.group(1)) if fi else None,
            'stroke_width': float(sw.group(1)) if sw else 0.0,
            'n': len(pts),
            'points': pts,
            'subpaths': subs,
            'd_len': len(d.group(1)) if d else 0,
            'd_raw': d.group(1) if d else None,
        }
        if pts:
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            el['bbox'] = (min(xs), min(ys), max(xs), max(ys))
        out.append(el)
    return out, vp


def words_with_boxes(html_path):
    s = open(html_path, encoding='utf-8').read()
    ws = []
    for x0, y0, x1, y1, t in re.findall(
            r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
            s):
        ws.append({'t': t, 'x': (float(x0) + float(x1)) / 2, 'y': (float(y0) + float(y1)) / 2,
                   'x0': float(x0), 'x1': float(x1), 'y0': float(y0), 'y1': float(y1)})
    return ws


if __name__ == '__main__':
    import sys, json
    els, vp = parse_svg(sys.argv[1])
    print('viewport', vp, 'elements', len(els))
    for e in els:
        if e['n'] > 1 and (e['d_len'] > 200 or e['stroke'] not in (None, '#000000')):
            print('%-6s n=%-5d stroke=%-9s fill=%-9s sw=%-4s bbox=%s' % (
                e['tag'], e['n'], e['stroke'], e['fill'], e['stroke_width'],
                tuple(round(v, 1) for v in e['bbox'])))
