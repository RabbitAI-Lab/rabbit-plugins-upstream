import zipfile, shutil, os, sys, copy, re
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
def q(t): return f"{{{W}}}{t}"

ET.register_namespace("w", W)

# 支持命令行参数指定待处理 docx；缺省回退到固定文件名
SRC = sys.argv[1] if len(sys.argv) > 1 else "《涉人工智能违法犯罪防范基本要求》修改说明_公文.docx"
TMP = "_fix_tmp"
EASTASIA_DEFAULT = "仿宋_GB2312"
TN = "Times New Roman"

if os.path.exists(TMP): shutil.rmtree(TMP)
os.makedirs(TMP)
with zipfile.ZipFile(SRC) as z:
    z.extractall(TMP)

def fix_rfonts(rf):
    if rf is None: return
    cur = rf.get(q("ascii"))
    if cur:
        rf.set(q("eastAsia"), cur)   # 汉字用对应中文字体
        rf.set(q("ascii"), TN)       # 阿拉伯数字/拉丁字母用 Times New Roman
        rf.set(q("hAnsi"), TN)

# ---------- document.xml：字体 + 缩进双单位化 + 显式左缩进0 ----------
dp = os.path.join(TMP, "word", "document.xml")
t = ET.parse(dp); r = t.getroot()

# 字体
for rf in r.iter(q("rFonts")):
    fix_rfonts(rf)

# ---------- 引号字体修正 ----------
# 中文双/单引号 “ ” ‘ ’（以及全角引号 ＂ ＇）属 Unicode “高 ANSI”码位，Word 会按 hAnsi 字体
# （Times New Roman）渲染，导致引号呈罗马字体而非对应中文字体（黑体/楷体/仿宋）。
# 修复：将含引号的 w:r 拆分为多 run，引号片段单独成 run，其 ascii/hAnsi 也指向当前 run 的
# 中文字体（eastAsia）并设 hint="eastAsia"，使其随上下文用正确中文字体显示；非引号片段保持
# 阿拉伯数字 Times New Roman、汉字用中文字体的设定。
QUOTE_CHARS = set(['“', '”', '‘', '’', '＂', '＇'])

def split_quote_runs(parent):
    kids = list(parent)
    out = []
    changed = False
    for ch in kids:
        if ch.tag != q("r"):
            out.append(ch); continue
        tEl = ch.find(q("t"))
        text = tEl.text if (tEl is not None and tEl.text) else ""
        # 含非文本子节点（tab/br/drawing 等）则不拆分，避免丢内容
        extra = [c for c in ch if c.tag != q("rPr") and c.tag != q("t")]
        if not text or not any(c in QUOTE_CHARS for c in text) or extra:
            out.append(ch); continue
        changed = True
        rPr = ch.find(q("rPr"))
        ea = EASTASIA_DEFAULT
        if rPr is not None:
            rf0 = rPr.find(q("rFonts"))
            if rf0 is not None:
                ea = rf0.get(q("eastAsia")) or EASTASIA_DEFAULT
        # 按是否引号分段
        segs = []
        cur_typ = None; buf = []
        for c in text:
            typ = 'q' if c in QUOTE_CHARS else 'o'
            if typ != cur_typ:
                if buf: segs.append((cur_typ, ''.join(buf)))
                buf = [c]; cur_typ = typ
            else:
                buf.append(c)
        if buf: segs.append((cur_typ, ''.join(buf)))
        for typ, seg in segs:
            nr = ET.Element(q("r"))
            nrPr = ET.SubElement(nr, q("rPr"))
            if rPr is not None:
                for sub in rPr:
                    if sub.tag == q("rFonts"): continue
                    nrPr.append(copy.deepcopy(sub))
            nrf = ET.SubElement(nrPr, q("rFonts"))
            if typ == 'q':
                for a in ("ascii", "hAnsi", "eastAsia", "cs"):
                    nrf.set(q(a), ea)
                nrf.set(q("hint"), "eastAsia")
            else:
                nrf.set(q("ascii"), TN); nrf.set(q("hAnsi"), TN)
                nrf.set(q("eastAsia"), ea); nrf.set(q("cs"), TN)
            nt = ET.SubElement(nr, q("t"))
            nt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            nt.text = seg
            out.append(nr)
    if changed:
        for c in list(parent):
            parent.remove(c)
        for c in out:
            parent.append(c)

# 对所有段落（含表格单元格内的段落）执行引号拆分
for pEl in r.iter(q("p")):
    split_quote_runs(pEl)

# ---------- 中文间多余空格清除 ----------
# 仅当空格两侧均为 CJK 字符或中文标点时才删除该空格；保留“中文+拉丁/数字”之间的空格
# （如“标准 GB/T 9704”“2026 年”）。同时处理 run 内部与跨 run 边界两种情况。
CJK_RE = re.compile(r'[\u3400-\u4DBF\u4E00-\u9FFF\u3001-\u303F\uFF00-\uFFEF\u2018\u2019\u201C\u201D]')
WS_RE = re.compile(r'[ \t\r\n\f\v\u3000]+')
INTRA_RE = re.compile('(' + CJK_RE.pattern + ')' + WS_RE.pattern + '(' + CJK_RE.pattern + ')')

def is_cjk(ch):
    return bool(ch) and bool(CJK_RE.match(ch))

_WS = " \t\r\n\f\v\u3000"
def _is_ws(ch): return ch in _WS
def _first_cjk(text):
    for ch in text:
        if not _is_ws(ch):
            return is_cjk(ch)
    return False
def _last_cjk(text):
    for ch in reversed(text):
        if not _is_ws(ch):
            return is_cjk(ch)
    return False

def normalize_spacing(root):
    total = 0
    # 1) 跨 run 边界：只看“有效的首个/末个非空白字符”是否为 CJK，
    #    忽略 run 自身首尾已夹带的空白（引号拆分后常出现“前导/尾随空格”落在相邻 run）。
    for pEl in root.iter(q("p")):
        runs = [c for c in pEl if c.tag == q("r")]
        for i, rEl in enumerate(runs):
            tEl = rEl.find(q("t"))
            if tEl is None or not tEl.text: continue
            before = len(tEl.text)
            if i > 0:
                pv = runs[i-1].find(q("t"))
                if pv is not None and pv.text and _last_cjk(pv.text) and _first_cjk(tEl.text):
                    tEl.text = re.sub(r'^[ \t\r\n\f\v\u3000]+', '', tEl.text)
            if i < len(runs) - 1:
                nx = runs[i+1].find(q("t"))
                if nx is not None and nx.text and _first_cjk(nx.text) and _last_cjk(tEl.text):
                    tEl.text = re.sub(r'[ \t\r\n\f\v\u3000]+$', '', tEl.text)
            total += before - len(tEl.text)
    # 2) run 内部：删除两侧均为 CJK 的空格（含表格/跨段落）
    for tEl in root.iter(q("t")):
        if not tEl.text: continue
        before = len(tEl.text)
        tEl.text = INTRA_RE.sub(r'\1\2', tEl.text)
        total += before - len(tEl.text)
    return total

space_total = normalize_spacing(r)

# 星号清洗：清除所有残留 markdown 星号（* 与 **），批量替换为空（双保险，对应“公文不保留 markdown 标记”）
asterisk_total = 0
for tEl in r.iter(q("t")):
    if tEl.text and "*" in tEl.text:
        asterisk_total += tEl.text.count("*")
        tEl.text = tEl.text.replace("*", "")

# 缩进：所有段落必须显式声明 firstLine/firstLineChars/left，防止继承用户模板
for pPr in r.iter(q("pPr")):
    ind = pPr.find(q("ind"))
    if ind is None:
        ind = ET.SubElement(pPr, q("ind"))
    flc = ind.get(q("firstLineChars"))
    fl  = ind.get(q("firstLine"))
    # 缺省补 0（无缩进）
    if flc is None and fl is None:
        ind.set(q("firstLineChars"), "0")
        ind.set(q("firstLine"), "0")
    elif flc is not None and fl is None:
        # 只有字符单位，补齐 twips 单位（firstLineChars 单位是 1/100 字符）
        try:
            chars = int(flc) / 100.0
        except ValueError:
            chars = 0
        ind.set(q("firstLine"), str(int(round(chars * 320))))   # 1字符≈320 twips
    elif fl is not None and flc is None:
        # 只有 twips，补齐字符单位
        try:
            twips = int(fl)
        except ValueError:
            twips = 0
        ind.set(q("firstLineChars"), str(round(twips / 320) * 100))
    # 显式左缩进=0，防止继承模板左缩进
    if ind.get(q("left")) is None and ind.get(q("leftChars")) is None:
        ind.set(q("left"), "0")
        ind.set(q("leftChars"), "0")

t.write(dp, xml_declaration=True, encoding="UTF-8")

# ---------- styles.xml：显式创建 Normal 样式 + docDefaults 无缩进 ----------
sp = os.path.join(TMP, "word", "styles.xml")
st = ET.parse(sp); sr = st.getroot()

def make_noindent_pPr(parent):
    """在 parent 下创建/更新 pPr，显式声明 首行缩进=0、左缩进=0。"""
    pPr = parent.find(q("pPr"))
    if pPr is None:
        pPr = ET.SubElement(parent, q("pPr"))
    ind = pPr.find(q("ind"))
    if ind is None:
        ind = ET.SubElement(pPr, q("ind"))
    ind.set(q("firstLine"), "0")
    ind.set(q("firstLineChars"), "0")
    ind.set(q("left"), "0")
    ind.set(q("leftChars"), "0")
    return pPr

def make_font_rPr(parent):
    """在 parent 下创建/更新 rPr，设置中英文字体。"""
    rpr = parent.find(q("rPr"))
    if rpr is None:
        rpr = ET.SubElement(parent, q("rPr"))
    rf = rpr.find(q("rFonts"))
    if rf is None:
        rf = ET.SubElement(rpr, q("rFonts"))
    rf.set(q("ascii"), TN)
    rf.set(q("hAnsi"), TN)
    rf.set(q("eastAsia"), EASTASIA_DEFAULT)
    rf.set(q("cs"), TN)
    return rpr

# 处理 docDefaults
dd = sr.find(q("docDefaults"))
if dd is None:
    dd = ET.Element(q("docDefaults"))
    sr.insert(0, dd)
rpd = dd.find(q("rPrDefault"))
if rpd is None:
    rpd = ET.SubElement(dd, q("rPrDefault"))
make_font_rPr(rpd)
ppd = dd.find(q("pPrDefault"))
if ppd is None:
    ppd = ET.SubElement(dd, q("pPrDefault"))
make_noindent_pPr(ppd)

# 查找或创建 Normal 样式
normal_style = None
for style in sr.iter(q("style")):
    sid = style.get(q("styleId"))
    name = style.find(q("name"))
    nm = name.get(q("val")) if name is not None else ""
    if sid == "Normal" or nm == "Normal":
        normal_style = style
        break
if normal_style is None:
    normal_style = ET.SubElement(sr, q("style"))
    normal_style.set(q("type"), "paragraph")
    normal_style.set(q("default"), "1")
    normal_style.set(q("styleId"), "Normal")
    nm = ET.SubElement(normal_style, q("name"))
    nm.set(q("val"), "Normal")
make_font_rPr(normal_style)
make_noindent_pPr(normal_style)

st.write(sp, xml_declaration=True, encoding="UTF-8")

# ---------- footer：同样确保缩进双单位、左缩进0 ----------
for n in os.listdir(os.path.join(TMP, "word")):
    if n.lower().startswith("footer") and n.endswith(".xml"):
        fp = os.path.join(TMP, "word", n)
        ft = ET.parse(fp); fr = ft.getroot()
        for rf in fr.iter(q("rFonts")):
            fix_rfonts(rf)
        # 页脚引号字体修正（与正文一致）
        for pEl in fr.iter(q("p")):
            split_quote_runs(pEl)
        # 页脚中文间多余空格清除（与正文一致）
        space_total += normalize_spacing(fr)
        # 页脚星号清洗（兜底）
        for tEl in fr.iter(q("t")):
            if tEl.text and "*" in tEl.text:
                asterisk_total += tEl.text.count("*")
                tEl.text = tEl.text.replace("*", "")
        for pPr in fr.iter(q("pPr")):
            ind = pPr.find(q("ind"))
            if ind is None:
                ind = ET.SubElement(pPr, q("ind"))
            if ind.get(q("firstLine")) is None:
                ind.set(q("firstLine"), "0")
            if ind.get(q("firstLineChars")) is None:
                ind.set(q("firstLineChars"), "0")
            if ind.get(q("left")) is None:
                ind.set(q("left"), "0")
            if ind.get(q("leftChars")) is None:
                ind.set(q("leftChars"), "0")
        ft.write(fp, xml_declaration=True, encoding="UTF-8")

# 重新打包
if os.path.exists(SRC): os.remove(SRC)
with zipfile.ZipFile(SRC, "w", zipfile.ZIP_DEFLATED) as z:
    for base, _, files in os.walk(TMP):
        for f in files:
            full = os.path.join(base, f)
            z.write(full, os.path.relpath(full, TMP))
shutil.rmtree(TMP)
print("后处理完成：字体 + 双单位缩进 + 显式 Normal 样式 + 引号中文字体修正 + 中文间空格清除；清除残留星号共 %d 处（替换为空），清除中文间多余空格共 %d 处" % (asterisk_total, space_total))
