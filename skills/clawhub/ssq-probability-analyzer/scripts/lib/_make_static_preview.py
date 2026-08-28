# -*- coding: utf-8 -*-
"""把增强版预测报告 strip 成无脚本静态版, 供 WorkBuddy 预览面板 iframe 渲染。

预览面板 iframe 会拦截 <script>, 带脚本的报告在面板里会白屏/内容缺失。
本脚本移除:
  1. 所有 <script>...</script> 块 (含无闭合的残缺块)
  2. 所有 on* 内联事件属性 (onclick/onload/onscroll...)
  3. <noscript> 包裹层保留内部内容 (避免"请开启JS"提示遮挡)
保留: 全部结构/CSS/文本 —— 频率表、专家双栏、ROI、大小比等核心内容不受影响。
"""
import re
import os
import sys
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))


def strip_scripts(html: str):
    stats = {}
    # 1. 完整 script 块 (含属性, 跨行, 大小写不敏感)
    html, n_script = re.subn(r'<script\b[^>]*>.*?</script\s*>', '',
                             html, flags=re.S | re.I)
    # 2. 残缺未闭合的 script 开标签(极端情况) -> 连同其后内容到文件尾? 不安全, 只删标签本身
    html, n_orphan = re.subn(r'</?script\b[^>]*>', '', html, flags=re.I)
    # 3. 外链 script 已被上面覆盖; 处理 on* 事件属性 (双引号/单引号/无引号)
    html, n_ev1 = re.subn(r'\son[a-zA-Z]+\s*=\s*"[^"]*"', '', html)
    html, n_ev2 = re.subn(r"\son[a-zA-Z]+\s*=\s*'[^']*'", '', html)
    html, n_ev3 = re.subn(r'\son[a-zA-Z]+\s*=\s*[^\s>"\']+', '', html)
    # 4. javascript: 伪协议链接 -> 置空锚点
    html, n_js = re.subn(r'href\s*=\s*(["\'])\s*javascript:[^"\']*\1',
                         r'href=\1#\1', html, flags=re.I)
    # 5. noscript 壳去掉, 保留内部内容
    html, n_ns = re.subn(r'</?noscript\s*>', '', html, flags=re.I)
    stats.update(script_blocks=n_script, orphan_tags=n_orphan,
                 on_events=n_ev1 + n_ev2 + n_ev3,
                 js_href=n_js, noscript=n_ns)
    return html, stats


def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    if not os.path.isabs(src):
        src = os.path.join(BASE, src)
    if not os.path.isabs(dst):
        dst = os.path.join(BASE, dst)

    raw = open(src, 'r', encoding='utf-8').read()
    out, stats = strip_scripts(raw)

    # 顶部插入静态版提示条 (紧跟 <body>)
    banner = (
        '<div style="background:#fff3cd;border:1px solid #ffe08a;color:#664d03;'
        'padding:10px 14px;margin:0;font-size:13px;line-height:1.6;'
        'font-family:-apple-system,\'Microsoft YaHei\',sans-serif;text-align:center">'
        '📄 <b>静态预览版</b>（已移除全部脚本以适配预览面板渲染）· '
        '内容与桌面完整交互版一致 · '
        '<b>专家推荐号为未核实观点，无预测力(no_edge)</b>，'
        '双色球任一 6+1 组合中奖概率恒为 1/17,721,088'
        '</div>'
    )
    m = re.search(r'<body[^>]*>', out, flags=re.I)
    if m:
        out = out[:m.end()] + banner + out[m.end():]
    else:
        out = banner + out

    open(dst, 'w', encoding='utf-8').write(out)

    # 校验: 静态版不应残留 script / on* 事件
    left_script = len(re.findall(r'<script\b', out, flags=re.I))
    left_ev = len(re.findall(r'\son[a-zA-Z]+\s*=\s*["\']', out))
    size = os.path.getsize(dst)
    print(f"[SRC ] {src}  ({os.path.getsize(src):,} bytes)")
    print(f"[DST ] {dst}  ({size:,} bytes)")
    print(f"[STRIP] 移除 script块={stats['script_blocks']} 残标签={stats['orphan_tags']} "
          f"on*事件={stats['on_events']} js链接={stats['js_href']} noscript壳={stats['noscript']}")
    print(f"[CHECK] 残留 <script={left_script}  残留 on*事件={left_ev}  "
          f"{'✅ 干净' if left_script == 0 and left_ev == 0 else '❌ 仍有残留'}")

    # 核心内容存在性校验 (防止 strip 误删正文)
    keys = {
        '频率表': ['近30期', '频率'],
        '专家双栏': ['专家', 'no_edge'],
        'ROI/成本': ['ROI'],
        '大小比': ['大小比'],
        '概率诚实声明': ['17,721,088'],
    }
    for label, needles in keys.items():
        hit = [n for n in needles if n in out]
        print(f"[CONTENT] {label:12s} {'✅' if hit else '⚠️ 未检出'} {hit}")
    return 0 if left_script == 0 and left_ev == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
