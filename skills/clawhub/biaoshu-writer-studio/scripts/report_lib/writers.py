"""HTML and DOCX writer primitives for report generation."""

import io
import zipfile
from xml.sax.saxutils import escape as _esc

from .common import _DOCX_RISK_COLOR

def esc(s):
    return _esc(str(s if s is not None else ""))


def esc_ml(s):
    return esc(s).replace("\n", "<br>")


def _toc_label(t):
    """目录文案：去掉章节标题里的「一、二、…」前缀（目录另有序号）。"""
    t = str(t)
    if len(t) > 1 and t[0] in "一二三四五六七八九十" and "、" in t[:4]:
        return t.split("、", 1)[1]
    return t

# block = (kind, text, opts)
_HEAD_SZ = {"title": 44, "subtitle": 21, "h2": 30, "h3": 25, "issue": 24}


def _run(text, *, bold=False, italic=False, color=None, sz=21):
    rpr = []
    if bold:
        rpr.append("<w:b/>")
    if italic:
        rpr.append("<w:i/>")
    if color:
        rpr.append(f'<w:color w:val="{color}"/>')
    rpr.append(f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>')
    runs = []
    for i, seg in enumerate(_esc(str(text)).split("\n")):
        if i:
            runs.append("<w:br/>")
        runs.append(f'<w:t xml:space="preserve">{seg}</w:t>')
    return f"<w:r><w:rPr>{''.join(rpr)}</w:rPr>{''.join(runs)}</w:r>"


def _ppr(*, before=0, after=80, ind=0, shade=None, border=None):
    p = []
    if shade:
        p.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>')
    if border:
        p.append(f'<w:pBdr><w:left w:val="single" w:sz="18" w:space="6" w:color="{border}"/></w:pBdr>')
    if ind:
        p.append(f'<w:ind w:left="{ind}"/>')
    p.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="276" w:lineRule="auto"/>')
    return f"<w:pPr>{''.join(p)}</w:pPr>"


def _para(block):
    kind, text, opts = block
    risk = opts.get("risk", "")
    if kind == "title":
        return f'<w:p>{_ppr(before=0, after=60)}{_run(text, bold=True, sz=44, color="1F3A8A")}</w:p>'
    if kind == "subtitle":
        return f'<w:p>{_ppr(after=200)}{_run(text, sz=20, color="647084")}</w:p>'
    if kind == "h2":
        return (f'<w:p>{_ppr(before=240, after=100, border="2563EB")}'
                f'{_run(text, bold=True, sz=30, color="1F3A8A")}</w:p>')
    if kind == "h3":
        return f'<w:p>{_ppr(before=140, after=60)}{_run(text, bold=True, sz=25, color="1F2933")}</w:p>'
    if kind == "issue":
        c = _DOCX_RISK_COLOR.get(risk, "475569")
        return (f'<w:p>{_ppr(before=140, after=40, border=c)}'
                f'{_run(text, bold=True, sz=24, color=c)}</w:p>')
    if kind == "callout":
        return (f'<w:p>{_ppr(before=80, after=120, ind=120, shade="EEF4FF")}'
                f'{_run(text, bold=True, sz=22, color="1E3A8A")}</w:p>')
    if kind == "muted":
        return f'<w:p>{_ppr(after=40, ind=120)}{_run(text, sz=18, color="647084")}</w:p>'
    if kind == "bullet":
        return f'<w:p>{_ppr(after=40, ind=300)}{_run("▪  " + str(text), sz=21)}</w:p>'
    if kind == "tender":
        return f'<w:p>{_ppr(after=30, ind=300, shade="F3F6FB")}{_run(text, sz=20, color="475569")}</w:p>'
    if kind == "bid":
        return f'<w:p>{_ppr(after=30, ind=300, shade="FFF7ED")}{_run(text, sz=20, color="9A3412")}</w:p>'
    if kind == "sug":
        return f'<w:p>{_ppr(after=80, ind=300, shade="ECFDF5")}{_run(text, sz=20, color="047857")}</w:p>'
    return f'<w:p>{_ppr()}{_run(text, sz=21)}</w:p>'


def build_docx(blocks) -> bytes:
    body = "".join(_para(b) for b in blocks)
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}<w:sectPr><w:pgMar w:top=\"1200\" w:right=\"1200\" w:bottom=\"1200\" "
        'w:left="1200" w:header="720" w:footer="720"/></w:sectPr></w:body></w:document>'
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/></Relationships>'
    )
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)
    return buf.getvalue()

_HTML_CSS = """
:root{
--paper:#f7f5f0;--card:#fffefb;--ink:#222530;--ink2:#5c6270;--line:#e7e1d5;
--side:#23262e;--side2:#2d313c;--sink:#c8cdd7;--smut:#838a98;
--gold:#bd9a5f;--gold2:#d8b878;--accent:#a9763f;
--high:#b23b2c;--review:#c07f22;--tip:#2f7572;--ok:#3a7d57;
--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Songti SC","STSong",serif;
--sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-size:14.5px;line-height:1.7;font-family:var(--sans)}
.shell{display:flex;min-height:100vh}
/* ---- 左侧目录 ---- */
.toc{width:228px;flex:none;background:linear-gradient(168deg,#23262e,#2c313c);color:var(--sink);
position:sticky;top:0;height:100vh;overflow:auto;padding:26px 18px 22px}
.toc .brand{font-size:10px;letter-spacing:3.5px;color:var(--gold);font-weight:700}
.toc .bt{font-family:var(--serif);font-size:18px;color:#fff;line-height:1.32;margin:9px 0 16px;
padding-bottom:15px;border-bottom:1px solid rgba(255,255,255,.1)}
.toc nav a{display:flex;gap:9px;color:var(--sink);text-decoration:none;font-size:12.5px;line-height:1.45;
padding:7px 9px;border-radius:5px;margin:1px 0;border-left:2px solid transparent;transition:.18s}
.toc nav a:hover{background:rgba(255,255,255,.06);color:#fff}
.toc nav a.on{background:rgba(189,154,95,.16);color:var(--gold2);border-left-color:var(--gold);font-weight:600}
.toc nav a .i{color:var(--smut);font-variant-numeric:tabular-nums}
.toc nav a.on .i{color:var(--gold)}
.toc .sfoot{margin-top:20px;padding-top:14px;border-top:1px solid rgba(255,255,255,.08);font-size:10.5px;color:var(--smut);letter-spacing:.5px}
/* ---- 内容区 ---- */
.content{flex:1;min-width:0}
.accent{display:flex;height:4px}.accent i{flex:1}
.accent .a{background:var(--high)}.accent .b{background:var(--review)}.accent .c{background:var(--tip)}
.inner{max-width:760px;margin:0 auto;padding:0 34px 72px}
/* ---- 封面 ---- */
.cover{padding:34px 0 20px;border-bottom:2px solid var(--ink);margin-bottom:6px}
.kicker{font-size:11px;letter-spacing:4px;color:var(--accent);font-weight:700;text-transform:uppercase;margin-bottom:11px}
.cover h1{font-family:var(--serif);font-weight:600;font-size:34px;line-height:1.16;letter-spacing:.5px;margin:0 0 15px;color:var(--ink)}
.meta{display:flex;flex-wrap:wrap;gap:7px 9px}
.meta .pill{font-size:12px;color:var(--ink2);background:#fff;border:1px solid var(--line);border-radius:2px;padding:3px 10px}
.meta .pill b{color:var(--accent);font-weight:700;margin-right:4px}
/* ---- 章节 ---- */
h2{font-family:var(--serif);font-weight:600;font-size:20px;color:var(--ink);scroll-margin-top:14px;
margin:34px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line);display:flex;align-items:baseline;gap:11px}
h2:before{content:"§";color:var(--gold);font-size:17px;font-weight:700}
h3{font-size:14.5px;margin:15px 0 6px;color:var(--ink);font-weight:700}
p{margin:6px 0;color:#2c3038}
/* ---- 风险条 ---- */
.riskbar{display:flex;height:11px;border-radius:2px;overflow:hidden;margin:4px 0 9px;border:1px solid var(--line)}
.riskbar span{display:block}.riskbar .high{background:var(--high)}.riskbar .review{background:var(--review)}
.riskbar .tip{background:var(--tip)}.riskbar .none{background:#ddd6c8;flex:1}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--ink2);margin-bottom:4px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:-1px}
/* ---- 指标 ---- */
.metrics{display:grid;grid-template-columns:repeat(5,1fr);gap:11px;margin:14px 0 6px}
.metric{position:relative;background:var(--card);border:1px solid var(--line);border-radius:3px;padding:15px 10px 12px;text-align:center;overflow:hidden}
.metric:before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:var(--ink2)}
.metric.high:before{background:var(--high)}.metric.review:before{background:var(--review)}
.metric.tip:before{background:var(--tip)}.metric.ok:before{background:var(--ok)}
.metric .n{font-family:var(--serif);font-size:33px;font-weight:600;line-height:1;color:var(--ink)}
.metric.high .n{color:var(--high)}.metric.review .n{color:var(--review)}.metric.tip .n{color:var(--tip)}
.metric .l{font-size:11px;color:var(--ink2);margin-top:7px;letter-spacing:.5px}
/* ---- 摘要 ---- */
.callout{position:relative;background:var(--card);border:1px solid var(--line);border-left:3px solid var(--gold);
border-radius:3px;padding:13px 18px;margin:14px 0;font-size:15px;color:var(--ink);font-weight:500}
.callout:before{content:"摘要";position:absolute;top:-9px;left:15px;background:var(--paper);font-size:10.5px;letter-spacing:2px;color:var(--accent);padding:0 6px;font-weight:700}
/* ---- 问题卡 ---- */
.issue{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--ink2);border-radius:3px;padding:14px 18px;margin:11px 0;break-inside:avoid}
.issue.high{border-left-color:var(--high)}.issue.review{border-left-color:var(--review)}.issue.tip{border-left-color:var(--tip)}
.ihead{display:flex;align-items:center;gap:10px;margin-bottom:2px}
.tag{font-size:10.5px;letter-spacing:1.5px;font-weight:700;padding:1px 8px;border-radius:2px;border:1px solid currentColor;white-space:nowrap}
.tag.high{color:var(--high)}.tag.review{color:var(--review)}.tag.tip{color:var(--tip)}.tag.other{color:var(--ink2)}
.issue h3{margin:0;font-size:15px;font-weight:700}
.fname{font-size:11.5px;color:var(--ink2);margin:1px 0 7px}
.issue p{margin:5px 0;color:#33373f;font-size:14px}
.evi{display:grid;gap:6px;margin:9px 0 3px}
.evi .row{padding:8px 12px;border-radius:2px;font-size:13px;line-height:1.58}
.evi .tender{background:#f2efe6;border-left:2px solid #9a9482}
.evi .bid{background:#f8efe3;border-left:2px solid #c98a4e}
.evi .lbl{display:block;font-size:10px;letter-spacing:1.5px;color:var(--ink2);font-weight:700;margin-bottom:2px}
.sug{margin-top:8px;padding:8px 12px;background:#edf2ee;border-left:2px solid var(--ok);border-radius:2px;font-size:13px;color:#234b35}
.sug b{color:var(--ok)}
/* ---- 通用 ---- */
.bullet{position:relative;margin:5px 0;padding-left:18px;color:#2c3038}
.bullet:before{content:"";position:absolute;left:3px;top:10px;width:5px;height:5px;background:var(--gold);transform:rotate(45deg)}
.muted{color:var(--ink2);font-size:12px;margin:2px 0}
.foot{margin-top:44px;padding-top:14px;border-top:1px solid var(--line);display:flex;justify-content:space-between;font-size:11px;color:var(--ink2);letter-spacing:.5px}
.foot .mark{font-family:var(--serif);color:var(--accent);font-weight:600}
@media(prefers-reduced-motion:no-preference){
.cover,h2,.issue,.metric,.callout{animation:rise .45s both}
.metric:nth-child(2){animation-delay:.04s}.metric:nth-child(3){animation-delay:.08s}
.metric:nth-child(4){animation-delay:.12s}.metric:nth-child(5){animation-delay:.16s}}
@keyframes rise{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}
@media print{.toc{display:none}.content{flex:none}*{animation:none!important}.issue,.metric,.callout{break-inside:avoid}}
@media(max-width:820px){.shell{flex-direction:column}.toc{width:auto;height:auto;position:static}
.toc nav{display:flex;flex-wrap:wrap;gap:4px}.toc nav a{margin:0}.metrics{grid-template-columns:repeat(3,1fr)}}
"""


class Report:
    """同时累积 HTML 片段与 docx blocks。"""

    def __init__(self, title):
        self.title = title
        self.html = []
        self.blocks = []
        self.sections = []
        self._sec = 0

    def _d(self, kind, text, **opts):
        self.blocks.append((kind, text, opts))

    def cover(self, kicker, title, meta):
        """meta: [(label, value)]"""
        pills = "".join(f"<span class='pill'><b>{esc(l)}</b> {esc(v)}</span>" for l, v in meta if v)
        self.html.append(
            f"<header class='cover'><div class='kicker'>{esc(kicker)}</div>"
            f"<h1>{esc(title)}</h1><div class='meta'>{pills}</div></header>")
        self._d("title", title)
        self._d("subtitle", "　·　".join(f"{l}：{v}" for l, v in meta if v))

    def h2(self, t):
        self._sec += 1
        sid = f"s{self._sec}"
        self.sections.append((sid, t))
        self.html.append(f"<h2 id='{sid}'>{esc(t)}</h2>")
        self._d("h2", t)

    def h3(self, t):
        self.html.append(f"<h3>{esc(t)}</h3>")
        self._d("h3", t)

    def p(self, t):
        self.html.append(f"<p>{esc_ml(t)}</p>")
        self._d("p", t)

    def bullet(self, t):
        self.html.append(f"<div class='bullet'>{esc_ml(t)}</div>")
        self._d("bullet", t)

    def callout(self, t):
        self.html.append(f"<div class='callout'>{esc_ml(t)}</div>")
        self._d("callout", t)

    def metrics(self, items):
        """items: [(label, value, cls)]"""
        cells = "".join(
            f"<div class='metric {c}'><div class='n'>{esc(v)}</div><div class='l'>{esc(l)}</div></div>"
            for l, v, c in items)
        self.html.append(f"<div class='metrics'>{cells}</div>")
        self._d("p", "　".join(f"{l} {v}" for l, v, _ in items))

    def risk_bar(self, high, review, tip):
        total = max(high + review + tip, 1)
        segs = ""
        for cls, n in (("high", high), ("review", review), ("tip", tip)):
            if n:
                segs += f"<span class='{cls}' style='flex:{n}'></span>"
        if not segs:
            segs = "<span class='none'></span>"
        legend = (f"<span><i style='background:var(--high)'></i>高风险 {high}</span>"
                  f"<span><i style='background:var(--review)'></i>待复核 {review}</span>"
                  f"<span><i style='background:var(--tip)'></i>提示 {tip}</span>")
        self.html.append(f"<div class='riskbar'>{segs}</div><div class='legend'>{legend}</div>")

    def signal_card(self, risk_cls, badge, title, body, note=""):
        h = [f"<div class='issue {risk_cls}'>",
             f"<div class='ihead'><span class='tag {risk_cls}'>{esc(badge)}</span>"
             f"<h3>{esc(title)}</h3></div>"]
        if body:
            h.append(f"<p>{esc_ml(body)}</p>")
        if note:
            h.append(f"<div class='muted'>{esc_ml(note)}</div>")
        h.append("</div>")
        self.html.append("".join(h))
        self._d("issue", f"[{badge}] {title}", risk=risk_cls)
        if body:
            self._d("p", body)
        if note:
            self._d("muted", note)

    def issue_card(self, risk_cls, badge, title, meta, desc, tender, bid, suggestion):
        h = [f"<div class='issue {risk_cls}'>",
             f"<div class='ihead'><span class='tag {risk_cls}'>{esc(badge)}</span>"
             f"<h3>{esc(title)}</h3></div>"]
        if meta:
            h.append(f"<div class='fname'>📄 {esc(meta)}</div>")
        if desc:
            h.append(f"<p>{esc_ml(desc)}</p>")
        if tender or bid:
            h.append("<div class='evi'>")
            if tender:
                h.append(f"<div class='row tender'><span class='lbl'>招标要求</span>{esc_ml(tender)}</div>")
            if bid:
                h.append(f"<div class='row bid'><span class='lbl'>标书现状</span>{esc_ml(bid)}</div>")
            h.append("</div>")
        if suggestion:
            h.append(f"<div class='sug'><b>建议 ▸</b> {esc_ml(suggestion)}</div>")
        h.append("</div>")
        self.html.append("".join(h))
        self._d("issue", f"[{badge}] {title}", risk=risk_cls)
        if meta:
            self._d("muted", meta)
        if desc:
            self._d("p", desc)
        if tender:
            self._d("tender", "招标要求：" + tender)
        if bid:
            self._d("bid", "标书现状：" + bid)
        if suggestion:
            self._d("sug", "建议：" + suggestion)

    def render_html(self):
        nav = "".join(
            f"<a href='#{sid}'><span class='i'>{i:02d}</span><span>{esc(_toc_label(t))}</span></a>"
            for i, (sid, t) in enumerate(self.sections, 1))
        foot = (f"<div class='foot'><span>本报告由「百炼®标书」skill 自动生成</span>"
                f"<span class='mark'>百炼®标书 · {esc(self.title)}</span></div>")
        js = ("<script>(function(){var L=[].slice.call(document.querySelectorAll('.toc nav a'));"
              "var S=L.map(function(a){return document.querySelector(a.getAttribute('href'));});"
              "function spy(){var idx=0;for(var j=0;j<S.length;j++){"
              "if(S[j]&&S[j].getBoundingClientRect().top<=130)idx=j;}"
              "L.forEach(function(a,j){a.classList.toggle('on',j===idx);});}"
              "document.addEventListener('scroll',spy,{passive:true});"
              "window.addEventListener('resize',spy);spy();})();</script>")
        return (f"<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'>"
                f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
                f"<title>{esc(self.title)}</title><style>{_HTML_CSS}</style></head>"
                f"<body><div class='shell'>"
                f"<aside class='toc'><div class='brand'>百炼®标书</div>"
                f"<div class='bt'>{esc(self.title)}</div><nav>{nav}</nav>"
                f"<div class='sfoot'>「百炼®标书」skill</div></aside>"
                f"<main class='content'><div class='accent'>"
                f"<i class='a'></i><i class='b'></i><i class='c'></i></div>"
                f"<div class='inner'>{''.join(self.html)}{foot}</div></main>"
                f"</div>{js}</body></html>")
