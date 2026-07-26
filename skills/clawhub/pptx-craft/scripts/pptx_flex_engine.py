# -*- coding: utf-8 -*-
"""
方法3 PPTX 出码引擎 (pptx_flex_engine.py)  —  html2ppt 技能核心
===========================================================
解决"手动 PPT 排版永远重叠/截断/没气口"的根因：手算绝对坐标 + 单串行一次性布局
  -> 改成 文本优先多遍架构 (Text-First Multi-Pass)，模拟人类做 PPT 的真实步骤：

  人类工作流（用户给出，本引擎严格遵循）：
    Step1  按尺寸/比例画区域边框          -> Pass0  flex 容器(区域)
    Step2  先放文字(占地最大)，上下左右留白；多文字间留气口；
            放不下则缩字号(不删内容)        -> Pass1 文本优先放置(字体度量测高+pad)
                                            Pass2 字号自适应(溢出按比例缩,保最小字号)+breath
    Step3  再放装饰元素(条/图)填充剩余空间  -> Pass3 装饰按"文字块底部+气口"定位(填空者)
    Step4  初稿->QA->二稿->QA->终稿         -> Pass4-5 迭代(留白不足全局缩字号重排,最多3轮)

架构层：
  ① 设计令牌(TOKENS) + 间距令牌(SP) + 密度(DENSITY) + 数据模型  —— 与 HTML 同源
  ② 虚拟画布 1440×680 (与 HTML 同源) + 均匀缩放+水平居中(气口1:1,不压扁)
  ③ 容器系统 Row/Column+flex权重 (仅用于区域框, 区域内部改文本优先)
  ④ 组件库 KpiCard/CompareCard/BarChart (内部文本优先, 装饰填空)
  ⑤ 校验层 越界+跨组重叠+留白下限; 不过则拒绝产出(终稿轮)
  ⑥ QA迭代器 初稿->二稿->终稿, 用留白提示驱动全局字号缩放

运行: python pptx_flex_engine.py  ->  migration-dashboard-m3-v3.pptx (+ .preview.svg)
"""

from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ----------------------------------------------------------------------------
# ① 设计令牌 (Design Tokens) —— 单一来源，三端(画布/HTML/PPT)共用
# ----------------------------------------------------------------------------
TOKENS = {
    "color": {
        "bg":      "F4F5F8",  # 页面底
        "ink":     "0F172A",  # 主文字/深底
        "muted":   "64748B",  # 次级文字
        "sub":     "94A3B8",  # 辅助文字
        "border":  "E2E8F0",  # 描边
        "card":    "FFFFFF",  # 卡片底
        "blue":    "2563EB",  # 主色(电光蓝)
        "green":   "16A34A",  # 成功
        "amber":   "D97706",  # 警示
        "greenBg": "DCFCE7",  # 状态芯片底
        "greenTx": "86EFAC",  # 状态芯片字
        "bar":     "CBD5E1",  # 灰色条/基线
    },
    "font": "Microsoft YaHei",       # Windows 标准中文，PPT 内可编辑
    "radius": {"sm": 4, "md": 10, "lg": 12, "pill": 14},
}

# ----------------------------------------------------------------------------
# 间距令牌 (Spacing Tokens) —— 阶梯化，所有间距只能从这里取
# ----------------------------------------------------------------------------
SP_RAW = {"xs": 4, "sm": 8, "md": 12, "lg": 16, "xl": 20, "2xl": 28}

# 密度系数：调"气口"的总旋钮。1.0=紧凑 1.2=舒适 1.4=宽松
DENSITY = 1.20

def sp(k):
    """间距令牌 -> 经密度系数放大的虚拟像素值"""
    return round(SP_RAW[k] * DENSITY)

PAD_CARD    = sp("lg")   # 卡片内边距 ≈19 (KPI/对比卡)
PAD_CARD_LG = sp("xl")   # 主卡片内边距 ≈24 (进度/历史/图表卡)

# 全局文本缩放（QA 迭代器驱动；1.0=不缩, <1=整体缩字号增气口）
G_TS = 1.0

# ----------------------------------------------------------------------------
# ② 虚拟画布 + 坐标映射 (与 HTML 1440×680 同源)
#    均匀缩放：X/Y 同比例 + 水平居中 -> 气口 1:1, 不压扁纵向
#    目标尺寸：标准 16:9 宽屏 (与用户模板一致，复制粘贴无缩放偏差)
# ----------------------------------------------------------------------------
VW, VH = 1440, 680
SLIDE_W_EMU = int(33.867 * 360000)   # 标准 16:9 宽度 ≈ 33.87 cm
SLIDE_H_EMU = int(19.05 * 360000)     # 标准 16:9 高度 ≈ 19.05 cm
SCALE = min(SLIDE_W_EMU / VW, SLIDE_H_EMU / VH)
OFFX = (SLIDE_W_EMU - VW * SCALE) / 2
OFFY = 0

def X(v): return int(round(OFFX + v * SCALE))
def Y(v): return int(round(OFFY + v * SCALE))
def W_(v): return int(round(v * SCALE))
def H_(v): return int(round(v * SCALE))
def FS(px): return Pt(px * 0.75)        # px -> pt (@96dpi)

def rgb(h): return RGBColor.from_string(h.replace("#", ""))

# ----------------------------------------------------------------------------
# 字体度量（估算）—— 不需真实渲染，用保守近似保证"宁多勿少"，文字绝不裁切
#   CJK 全角字符宽 ≈ fs*0.98；拉丁 ≈ fs*0.55；空格 ≈ fs*0.30
#   行高 ≈ fs*1.25（含行内上下留白，模拟 PPT 真实包络）
# ----------------------------------------------------------------------------
def _char_w(ch, fs):
    o = ord(ch)
    if o > 0x2E7F:                 # CJK + 全角标点
        return fs * 0.98
    if ch == ' ':
        return fs * 0.30
    return fs * 0.55

def text_w(s, fs):
    return sum(_char_w(c, fs) for c in s)

def text_h(s, fs, max_w):
    if max_w <= 0:
        return fs * 1.25
    cur = 0.0
    lines = 1
    for ch in s:
        cw = _char_w(ch, fs)
        if cur + cw > max_w and cur > 0:
            lines += 1
            cur = cw
        else:
            cur += cw
    return lines * fs * 1.25

# ----------------------------------------------------------------------------
# Box —— 虚拟坐标矩形
# ----------------------------------------------------------------------------
class Box:
    __slots__ = ("x", "y", "w", "h")
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

# ----------------------------------------------------------------------------
# ③ 容器系统 (flex) —— 仅用于"区域框"层级
# ----------------------------------------------------------------------------
def hbox(deck, box, items, gap=16, pad=0):
    ix, iw = box.x + pad, box.w - 2 * pad
    n = len(items)
    tg = gap * (n - 1) if n > 1 else 0
    fixed = sum(it.get("size") or 0 for it in items)
    flex_total = sum(it.get("flex") or 0 for it in items)
    unit = (iw - tg - fixed) / flex_total if flex_total else 0
    cx = ix
    for it in items:
        cw = it["flex"] * unit if it.get("flex") else it.get("size", 0)
        cb = Box(cx, box.y + pad, cw, box.h - 2 * pad)
        it["build"](deck, cb, it.get("group", "g"))
        cx += cw + gap

def vbox(deck, box, items, gap=16, pad=0):
    iy, ih = box.y + pad, box.h - 2 * pad
    n = len(items)
    tg = gap * (n - 1) if n > 1 else 0
    fixed = sum(it.get("size") or 0 for it in items)
    flex_total = sum(it.get("flex") or 0 for it in items)
    unit = (ih - tg - fixed) / flex_total if flex_total else 0
    cy = iy
    for it in items:
        ch = it["flex"] * unit if it.get("flex") else it.get("size", 0)
        cb = Box(box.x + pad, cy, box.w - 2 * pad, ch)
        it["build"](deck, cb, it.get("group", "g"))
        cy += ch + gap

# ----------------------------------------------------------------------------
# Deck —— 渲染 + 校验登记
# ----------------------------------------------------------------------------
class VRec:
    __slots__ = ("x", "y", "w", "h", "group", "kind")
    def __init__(self, x, y, w, h, group, kind):
        self.x, self.y, self.w, self.h, self.group, self.kind = x, y, w, h, group, kind

class Deck:
    def __init__(self):
        self.ops = []
        self.recs = []
    def rect(self, b, fill, line=None, radius=0, group="g"):
        self.ops.append(("rect", b, fill, line, radius, group))
        self.recs.append(VRec(b.x, b.y, b.w, b.h, group, "rect"))
    def ellipse(self, b, fill, group="g"):
        self.ops.append(("ellipse", b, fill, group))
        self.recs.append(VRec(b.x, b.y, b.w, b.h, group, "ellipse"))
    def text(self, b, content, fs, color, bold=False, align="left", group="g"):
        self.ops.append(("text", b, content, fs, color, bold, align, group))
        self.recs.append(VRec(b.x, b.y, b.w, b.h, group, "text"))
    def render(self, slide):
        for op in self.ops:
            if op[0] == "rect":
                _, b, fill, line, radius, _ = op
                sp_ = slide.shapes.add_shape(
                    MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
                    X(b.x), Y(b.y), W_(b.w), H_(b.h))
                sp_.fill.solid(); sp_.fill.fore_color.rgb = rgb(fill)
                if line:
                    sp_.line.color.rgb = rgb(line[0]); sp_.line.width = Pt(line[1])
                else:
                    sp_.line.fill.background()
                sp_.shadow.inherit = False
            elif op[0] == "ellipse":
                _, b, fill, _ = op
                sp_ = slide.shapes.add_shape(MSO_SHAPE.OVAL, X(b.x), Y(b.y), W_(b.w), H_(b.h))
                sp_.fill.solid(); sp_.fill.fore_color.rgb = rgb(fill); sp_.line.fill.background()
                sp_.shadow.inherit = False
            elif op[0] == "text":
                _, b, content, fs, color, bold, align, _ = op
                tb = slide.shapes.add_textbox(X(b.x), Y(b.y), W_(b.w), H_(b.h))
                tf = tb.text_frame
                tf.word_wrap = True
                tf.vertical_anchor = MSO_ANCHOR.MIDDLE
                tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
                p = tf.paragraphs[0]
                p.alignment = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}[align]
                r = p.add_run(); r.text = content
                r.font.size = FS(fs); r.font.bold = bold
                r.font.color.rgb = rgb(color); r.font.name = TOKENS["font"]

# ----------------------------------------------------------------------------
# ⑤ 校验层 (Validator)
# ----------------------------------------------------------------------------
MIN_BREATH = 10   # 跨组最小间隙（虚拟px），低于即报"拥挤"

def _overlap(a, b, tol=1):
    return not (a.x + a.w <= b.x + tol or b.x + b.w <= a.x + tol or
                a.y + a.h <= b.y + tol or b.y + b.h <= a.y + tol)

def _contains(o, i, tol=1):
    return (i.x >= o.x - tol and i.y >= o.y - tol and
            i.x + i.w <= o.x + o.w + tol and i.y + i.h <= o.y + o.h + tol)

def _gap_between(a, b):
    ox = min(a.x + a.w, b.x + b.w) - max(a.x, b.x)
    oy = min(a.y + a.h, b.y + b.h) - max(a.y, b.y)
    if ox <= 0 and oy <= 0:
        return max(ox, oy)
    if ox <= 0:
        return ox
    if oy <= 0:
        return oy
    return min(ox, oy)

def validate(recs):
    errors, warnings = [], []
    for r in recs:
        if r.x < -1 or r.y < -1 or r.x + r.w > VW + 1 or r.y + r.h > VH + 1:
            errors.append(f"[越界:{r.group}] ({r.x:.0f},{r.y:.0f},{r.w:.0f},{r.h:.0f}) 超出 1440x680")
    for i in range(len(recs)):
        for j in range(i + 1, len(recs)):
            a, b = recs[i], recs[j]
            if a.group == b.group:
                continue
            if _contains(a, b) or _contains(b, a):
                continue
            if _overlap(a, b):
                errors.append(f"[重叠:{a.group}↔{b.group}] 几何相交 -> 元素重复/错位")
    for i in range(len(recs)):
        for j in range(i + 1, len(recs)):
            a, b = recs[i], recs[j]
            if a.group == b.group:
                continue
            if _contains(a, b) or _contains(b, a):
                continue
            g = _gap_between(a, b)
            if 0 <= g < MIN_BREATH:
                warnings.append(f"[拥挤:{a.group}↔{b.group}] 间隙 {g:.0f}px < {MIN_BREATH}px")
    return errors, warnings

# ============================================================================
# 文本优先布局核心  (Pass1 + Pass2)
# ============================================================================
def layout_texts(deck, items, box, pad, breath, align="left", group="g", ts=None):
    """
    在 box 内"文本优先"放置一组文字（纵栈）：
      - 上下左右留 pad 气口；多文字间留 breath 气口
      - 若总高超出 box.h，按比例缩所有字号（各自保 min_fs，绝不删内容）
    返回 leftover：文字块下方剩余空间 Box（供 Pass3 装饰填充）
    """
    ts = G_TS if ts is None else ts
    avail_w = max(1, box.w - 2 * pad)

    def block_h(scale):
        h = 2 * pad
        for it in items:
            fs = max(it.get("min_fs", 9), it["fs"] * ts * scale)
            h += text_h(it["content"], fs, avail_w)
            h += breath
        return h - breath

    scale = 1.0
    if block_h(1.0) > box.h:
        lo, hi = 0.40, 1.0
        for _ in range(22):
            mid = (lo + hi) / 2
            if block_h(mid) > box.h:
                hi = mid
            else:
                lo = mid
        scale = lo

    y = box.y + pad
    for it in items:
        fs = max(it.get("min_fs", 9), it["fs"] * ts * scale)
        th = text_h(it["content"], fs, avail_w)
        tb = Box(box.x + pad, y, avail_w, th)
        deck.text(tb, it["content"], fs, it["color"], bold=it.get("bold", False),
                  align=align, group=group)
        y += th + breath
    used = (y - breath) - box.y
    leftover = Box(box.x, y - breath, box.w, max(0, box.y + box.h - (y - breath)))
    return leftover, scale

# ============================================================================
# ④ 组件库 (Components) —— 内部文本优先, 装饰填空
# ============================================================================
def KpiCard(deck, box, group, kpi):
    C = TOKENS["color"]
    deck.rect(box, C["card"], line=(C["border"], 1), radius=TOKENS["radius"]["lg"], group=group)
    items = [
        {"content": kpi["label"], "fs": 13, "min_fs": 10, "color": C["muted"]},
        {"content": kpi["value"], "fs": 30, "bold": True, "min_fs": 20, "color": kpi["color"]},
        {"content": kpi["sub"],   "fs": 12, "min_fs": 9,  "color": C["sub"]},
    ]
    layout_texts(deck, items, box, pad=PAD_CARD, breath=sp("sm"), align="left", group=group)

def CompareCard(deck, box, group, cmp):
    C = TOKENS["color"]
    deck.rect(box, C["card"], line=(C["border"], 1), radius=TOKENS["radius"]["md"], group=group)
    items = [
        {"content": cmp["label"], "fs": 12, "min_fs": 10, "color": C["muted"]},
        {"content": cmp["value"], "fs": 24, "bold": True, "min_fs": 16, "color": C["ink"]},
        {"content": cmp["sub"],   "fs": 11, "min_fs": 9,  "color": C["green"]},
    ]
    layout_texts(deck, items, box, pad=sp("md"), breath=sp("xs"), align="left", group=group)

# ============================================================================
# 数据模型 (与 HTML DASHBOARD_DATA 同源)
# ============================================================================
KPI = [
    {"label": "切换进度",    "value": "68.3%", "sub": "目标 100% · 预计 3 天后完成", "color": TOKENS["color"]["ink"]},
    {"label": "已切换用户",  "value": "8,420", "sub": "占总用户 68.3%",             "color": TOKENS["color"]["blue"]},
    {"label": "未切换用户",  "value": "3,910", "sub": "待迁移 · 含 4 个批次",         "color": TOKENS["color"]["ink"]},
    {"label": "异常 / 回滚", "value": "23",    "sub": "较昨日 -5 · 已自动恢复",       "color": TOKENS["color"]["amber"]},
]
CMP = [
    {"label": "成功率",   "value": "99.7%", "sub": "较基线 +0.2% · 正常"},
    {"label": "响应时间", "value": "142ms", "sub": "较基线 -8ms · 良好"},
    {"label": "错误率",   "value": "0.03%", "sub": "较基线 -0.01% · 稳定"},
]
BATCHES = [
    ("Batch A", 480, TOKENS["color"]["green"]),
    ("Batch B", 496, TOKENS["color"]["green"]),
    ("Batch C", 384, TOKENS["color"]["blue"]),
    ("Batch D", 320, TOKENS["color"]["blue"]),
    ("Batch E", 128, TOKENS["color"]["bar"]),
    ("Batch F", 64,  TOKENS["color"]["bar"]),
]
MAXBW = 512
DAYS = [
    ("D1", 9200, 9000), ("D2", 9400, 9400), ("D3", 9600, 9800), ("D4", 9500, 9600),
    ("D5", 8900, 10200), ("D6", 8700, 10800), ("D7", 8500, 11200), ("D8", 8400, 11500),
]
CHART_MAX = 12000

# ============================================================================
# 区块构建器 (builders)
# ============================================================================
def build_header(deck, box, _):
    C = TOKENS["color"]
    deck.rect(box, C["ink"], group="header")
    # 左侧文字块（标题+副标题），文本优先 + 上下气口 + 两行间气口
    left = Box(box.x + 32, box.y, 420, box.h)
    items = [
        {"content": "系统升级切换进度监控", "fs": 18, "bold": True, "min_fs": 14, "color": "#FFFFFF"},
        {"content": "实时反映用户在线数据驱动的切换进展", "fs": 13, "min_fs": 11, "color": C["sub"]},
    ]
    layout_texts(deck, items, left, pad=sp("md"), breath=sp("xs"), align="left", group="header")
    # 右侧：时间文字(右对齐,垂直居中) + 状态芯片
    time_s = "更新于 14:08 · 实时"
    time_fs = 12
    time_h = text_h(time_s, time_fs * G_TS, 160)
    time_x = box.x + box.w - 32 - 160
    time_y = box.y + (box.h - time_h) / 2
    deck.text(Box(time_x, time_y, 160, time_h), time_s, time_fs, C["sub"], align="right", group="header")
    chip_w, chip_h = 84, 26
    chip_x = time_x - 10 - chip_w
    chip_y = box.y + (box.h - chip_h) / 2
    deck.rect(Box(chip_x, chip_y, chip_w, chip_h), C["greenBg"], radius=14, group="header")
    deck.ellipse(Box(chip_x + 10, chip_y + chip_h / 2 - 3.5, 7, 7), C["green"], group="header")
    deck.text(Box(chip_x + 22, chip_y, chip_w - 22, chip_h), "进行中", 12, C["greenTx"], group="header")

def build_kpi_row(deck, box, _):
    items = [{
        "flex": 1, "group": f"kpi-{i}",
        "build": lambda d, cb, g, i=i: KpiCard(d, cb, f"kpi-{i}", KPI[i])
    } for i in range(4)]
    hbox(deck, box, items, gap=sp("lg"))

def build_progress(deck, box, _):
    C = TOKENS["color"]
    deck.rect(box, C["card"], line=(C["border"], 1), radius=12, group="progress")
    p = PAD_CARD_LG
    inner = Box(box.x + p, box.y + p, box.w - 2 * p, box.h - 2 * p)
    # 标题行（左标题 + 右说明，同一基线，文本优先测高）
    title_s, note_s = "切换进度总览", "按用户数统计 · 共 6 个批次"
    row_h = max(text_h(title_s, 15 * G_TS, 300), text_h(note_s, 12 * G_TS, inner.w - 300))
    deck.text(Box(inner.x, inner.y, 300, row_h), title_s, 15, C["ink"], bold=True, group="progress")
    deck.text(Box(inner.x + 300, inner.y, inner.w - 300, row_h), note_s, 12, C["sub"], align="right", group="progress")
    # 堆叠条（置于标题下方 + 气口）
    bar_y = inner.y + row_h + sp("md")
    bar_h = 28
    deck.rect(Box(inner.x, bar_y, inner.w, bar_h), C["bar"], radius=6, group="progress")
    deck.rect(Box(inner.x, bar_y, inner.w * 0.683, bar_h), C["blue"], radius=6, group="progress")
    # 图例（置于条下方 + 气口）
    lg_y = bar_y + bar_h + sp("sm")
    deck.ellipse(Box(inner.x, lg_y + 4, 9, 9), C["blue"], group="progress")
    deck.text(Box(inner.x + 14, lg_y, 130, 16), "已切换 68.3%", 11, C["muted"], group="progress")
    deck.ellipse(Box(inner.x + 150, lg_y + 4, 9, 9), C["bar"], group="progress")
    deck.text(Box(inner.x + 164, lg_y, 130, 16), "未切换 31.7%", 11, C["muted"], group="progress")
    # 批次条（图例下方 + 气口，逐行带气口）
    by = lg_y + 18 + sp("md")
    track_w = inner.w - 64 - 54
    row_bh = 14
    for i, (name, bw, col) in enumerate(BATCHES):
        yy = by + i * (row_bh + sp("xs"))
        deck.text(Box(inner.x, yy, 60, row_bh), name, 11, C["muted"], group="progress")
        bw_px = bw / MAXBW * track_w
        deck.rect(Box(inner.x + 64, yy, bw_px, row_bh), col, radius=4, group="progress")
        pct = round(bw / MAXBW * 100)
        deck.text(Box(inner.x + 64 + bw_px + 6, yy, 48, row_bh), f"{pct}%", 11, C["muted"], group="progress")

def build_history(deck, box, _):
    C = TOKENS["color"]
    deck.rect(box, C["card"], line=(C["border"], 1), radius=12, group="history")
    p = PAD_CARD_LG
    inner = Box(box.x + p, box.y + p, box.w - 2 * p, box.h - 2 * p)
    title_s, note_s = "切换期间历史数据对比", "切换前 7 天基线 vs 切换期间实时"
    row_h = max(text_h(title_s, 15 * G_TS, 320), text_h(note_s, 12 * G_TS, inner.w - 320))
    deck.text(Box(inner.x, inner.y, 320, row_h), title_s, 15, C["ink"], bold=True, group="history")
    deck.text(Box(inner.x + 320, inner.y, inner.w - 320, row_h), note_s, 12, C["sub"], align="right", group="history")
    # 对比卡行（标题下方 + 气口）
    cmp_box = Box(inner.x, inner.y + row_h + sp("md"), inner.w, 80)
    items = [{
        "flex": 1, "group": f"cmp-{j}",
        "build": lambda d, cb, g, j=j: CompareCard(d, cb, f"cmp-{j}", CMP[j])
    } for j in range(3)]
    hbox(deck, cmp_box, items, gap=sp("md"))
    # 图表卡（对比卡下方 + 气口）
    chart_y = inner.y + row_h + sp("md") + 80 + sp("md")
    chart_box = Box(inner.x, chart_y, inner.w, inner.y + inner.h - chart_y)
    build_chart(deck, chart_box, "chart")

def build_chart(deck, box, _):
    C = TOKENS["color"]
    deck.rect(box, C["card"], line=(C["border"], 1), radius=12, group="chart")
    p = PAD_CARD
    inner = Box(box.x + p, box.y + sp("md"), box.w - 2 * p, box.h - 2 * sp("md"))
    title_s = "在线用户数趋势"
    title_h = text_h(title_s, 13 * G_TS, inner.w)
    deck.text(Box(inner.x, inner.y, inner.w, title_h), title_s, 13, C["ink"], bold=True, group="chart")
    # 绘图区（标题下方 + 气口；底部留气口给 x 轴标签）
    plot_top = inner.y + title_h + sp("sm")
    xlab_h = 16
    plot_bottom = inner.y + inner.h - sp("md") - xlab_h
    plot_h = plot_bottom - plot_top
    n = len(DAYS)
    colW = inner.w / n
    baseMaxH = plot_h * 0.80
    bw = colW * 0.30
    for i, (name, base, live) in enumerate(DAYS):
        cx = inner.x + i * colW
        off = (colW - 2 * bw - 3) / 2
        hb = base / CHART_MAX * baseMaxH
        deck.rect(Box(cx + off, plot_bottom - hb, bw, hb), C["bar"], radius=3, group="chart")
        hl = live / CHART_MAX * baseMaxH
        lx = cx + off + bw + 3
        deck.rect(Box(lx, plot_bottom - hl, bw, hl), C["blue"], radius=3, group="chart")
        # 实时数值标签（置于蓝柱顶 + 气口，绝不悬浮重叠）
        lbl = f"{live//1000}.{live%1000//100}k"
        lh = text_h(lbl, 9 * G_TS, bw + 24)
        deck.text(Box(lx - 12, plot_bottom - hl - lh - sp("xs"), bw + 24, lh),
                  lbl, 9, C["blue"], align="center", group="chart")
        # x 轴标签（绘图区下方 + 气口）
        deck.text(Box(cx - 12, plot_bottom + sp("xs"), colW + 24, xlab_h), name, 9, C["sub"], align="center", group="chart")

def build_footer(deck, box, _):
    C = TOKENS["color"]
    note_l = "数据来源：用户在线心跳上报 · 每 30 秒聚合一次 · 仅供切换指挥参考"
    note_r = "切换指挥看板 v1.0 · 标准16:9 (33.87×19.05cm)"
    lh = text_h(note_l, 11 * G_TS, box.w * 0.7)
    fy = box.y + (box.h - lh) / 2
    deck.text(Box(box.x, fy, box.w * 0.7, lh), note_l, 11, C["sub"], group="footer")
    deck.text(Box(box.x + box.w * 0.7, fy, box.w * 0.3, lh), note_r, 11, C["sub"], align="right", group="footer")

# ============================================================================
# 主流程
# ============================================================================
def build_dashboard():
    deck = Deck()
    root = Box(20, 10, 1400, 660)   # 收紧边距: 内容占虚拟画布 97%+，填满标准16:9
    vbox(deck, root, [
        {"size": 64,   "build": build_header},
        {"size": 116,  "build": build_kpi_row},
        {"flex": 1,    "build": build_main},
        {"size": 36,   "build": build_footer},
    ], gap=sp("xl"))
    return deck

def build_main(deck, box, _):
    items = [
        {"size": 560, "group": "progress", "build": build_progress},
        {"flex": 1,   "group": "history",  "build": build_history},
    ]
    hbox(deck, box, items, gap=sp("xl"))

def main():
    global G_TS
    MAX_ROUNDS = 3
    best = None
    print(f"▶ 文本优先多遍架构启动 (DENSITY={DENSITY}, 最多 {MAX_ROUNDS} 轮 QA 迭代)")
    for rnd in range(MAX_ROUNDS):
        # Pass4-5: 留白不足则全局缩字号(增气口)重排 —— 初稿->二稿->终稿
        G_TS = 1.0 - 0.06 * rnd
        deck = build_dashboard()
        errors, warnings = validate(deck.recs)
        n_err, n_warn = len(errors), len(warnings)
        if errors:
            print(f"  轮{rnd+1} (TS={G_TS:.2f}): ✗ 越界/重叠 {n_err} 处 -> 缩小文本重排")
            best = (deck, errors, warnings)
            continue
        if warnings and rnd < MAX_ROUNDS - 1:
            print(f"  轮{rnd+1} (TS={G_TS:.2f}): ✓ 无越界/重叠, ⚠ 留白提示 {n_warn} 处 -> 缩字号增气口")
            best = (deck, errors, warnings)
            continue
        print(f"  轮{rnd+1} (TS={G_TS:.2f}): ✓ 校验通过 (无越界/重叠, 留白提示 {n_warn} 处)")
        best = (deck, errors, warnings)
        break
    deck, errors, warnings = best

    if errors:
        print("✗ 三轮迭代后仍越界/重叠，拒绝生成 PPT：")
        for it in errors[:10]:
            print("   -", it)
        raise SystemExit(1)
    print(f"✓ 终稿：{len(deck.recs)} 个元素，无越界、无跨组重叠")
    if warnings:
        print(f"⚠ 终稿留白提示 {len(warnings)} 处（已尽量压缩，可再上调 DENSITY）：")
        for it in warnings[:8]:
            print("   -", it)
    else:
        print(f"✓ 留白校验通过：所有跨组间隙 ≥ {MIN_BREATH}px")

    emit_svg(deck, "migration-dashboard-m3-preview.svg")

    prs = Presentation()
    prs.slide_width = Emu(SLIDE_W_EMU)
    prs.slide_height = Emu(SLIDE_H_EMU)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(TOKENS["color"]["bg"])
    deck.render(slide)

    out = "migration-dashboard-m3-v4.pptx"
    prs.save(out)
    print(f"✓ 已生成可编辑 PPT：{out}  (标准16:9 {33.867:.2f}×{19.05:.2f}cm, 单页, 文本优先多遍架构)")

# ----------------------------------------------------------------------------
# SVG 预览
# ----------------------------------------------------------------------------
def emit_svg(deck, path):
    C = TOKENS["color"]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW} {VH}" font-family="{TOKENS["font"]}">']
    parts.append(f'<rect x="0" y="0" width="{VW}" height="{VH}" fill="#{C["bg"]}"/>')
    for op in deck.ops:
        if op[0] == "rect":
            _, b, fill, line, radius, _ = op
            r = radius if radius else 0
            stroke = f' stroke="#{line[0]}" stroke-width="{line[1]}"' if line else ''
            parts.append(f'<rect x="{b.x:.0f}" y="{b.y:.0f}" width="{b.w:.0f}" height="{b.h:.0f}" rx="{r}" fill="#{fill}"{stroke}/>')
        elif op[0] == "ellipse":
            _, b, fill, _ = op
            cx, cy, rx, ry = b.x + b.w/2, b.y + b.h/2, b.w/2, b.h/2
            parts.append(f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="#{fill}"/>')
        elif op[0] == "text":
            _, b, content, fs, color, bold, align, _ = op
            anc = {"left": "start", "center": "middle", "right": "end"}[align]
            tx = {"left": b.x, "center": b.x + b.w/2, "right": b.x + b.w}[align]
            ty = b.y + b.h/2 + fs*0.35
            wt = ' font-weight="700"' if bold else ''
            parts.append(f'<text x="{tx:.0f}" y="{ty:.0f}" font-size="{fs}" fill="#{color}" text-anchor="{anc}"{wt}>{content}</text>')
    parts.append('</svg>')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"✓ 已导出布局预览：{path}  （虚拟坐标 1:1，可在浏览器/聊天中直接查看气口效果）")

if __name__ == "__main__":
    main()
