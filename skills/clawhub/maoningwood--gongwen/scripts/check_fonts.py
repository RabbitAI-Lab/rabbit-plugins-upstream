#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查公文规范字体是否齐全。零第三方依赖，支持 macOS / Linux / Windows。

用法：
    python3 check_fonts.py              # 扫描系统字体目录
    python3 check_fonts.py /path/dir    # 额外扫描指定目录
    python3 check_fonts.py --only DIR   # 只扫描指定目录（测试用）

全部齐备退出码 0；缺字体退出码 1（agent 可据此中断生成流程）。
"""
import os
import struct
import subprocess
import sys

# 家族名以 docx 中引用的名称为准（含常见英文别名，命中任一即算已安装）。
# 第三个元素是该字体的"近义关键词"：缺失时仅提示名称相近的已装字体（如装了
# 方正黑体简体但缺 黑体），避免把无关的公文字体都列成近似项。
REQUIRED = [
    (['方正小标宋简体', 'FZXiaoBiaoSong-B05S'],
     '大标题（方正小标宋 二号）', ['小标宋', 'xiaobiaosong']),
    (['黑体', 'SimHei'],
     '一级标题、表头（黑体 三号）', ['黑体', 'hei']),
    (['楷体_GB2312', 'KaiTi_GB2312'],
     '副标题、二级标题（楷体_GB2312 三号 不加粗）', ['楷体', 'kaiti']),
    (['仿宋_GB2312', 'FangSong_GB2312'],
     '正文、三级标题加粗、落款（仿宋_GB2312 三号）', ['仿宋', 'fangsong']),
]

CHANNELS = {
    '方正小标宋简体': '方正字库官网 foundertype.com 注册后可免费下载（个人非商业用途）；机关或装过 Office 的电脑通常已预装',
    '黑体': 'Windows/Office 中文版自带（SimHei），可从自有授权的 Windows 电脑复制安装',
    '楷体_GB2312': '随 Windows/Office 中文版附带，可从自有授权的 Windows 电脑复制安装',
    '仿宋_GB2312': '随 Windows/Office 中文版附带，可从自有授权的 Windows 电脑复制安装',
}

FONT_EXTS = ('.ttf', '.ttc', '.otf')


def sfnt_families(path):
    """读 sfnt/TTC 字体文件的家族名（nameID 1、16），返回名称集合。解析失败时退回文件名。"""
    names = set()
    try:
        with open(path, 'rb') as f:
            head = f.read(12)
            if len(head) < 12:
                return names
            if head[:4] == b'ttcf':
                n = struct.unpack('>I', head[8:12])[0]
                offs = struct.unpack('>%dI' % n, f.read(4 * n))
            else:
                offs = (0,)
            for off in offs:
                f.seek(off)
                h = f.read(12)
                if h[:4] not in (b'\x00\x01\x00\x00', b'OTTO', b'true'):
                    continue
                num_tables = struct.unpack('>H', h[4:6])[0]
                f.seek(off + 12)
                recs = f.read(16 * num_tables)
                for i in range(num_tables):
                    tag, _sum, toff, _len = struct.unpack_from('>4sIII', recs, i * 16)
                    if tag != b'name':
                        continue
                    f.seek(toff)
                    hdr = f.read(6)
                    _fmt, cnt, sofs = struct.unpack('>HHH', hdr)
                    nrec = f.read(12 * cnt)
                    for j in range(cnt):
                        pid, _eid, _lid, nid, ln, o = struct.unpack_from(
                            '>HHHHHH', nrec, j * 12)
                        if nid not in (1, 16):
                            continue
                        f.seek(toff + sofs + o)  # 字符串偏移相对 name 表起点
                        raw = f.read(ln)
                        try:
                            s = raw.decode('utf-16-be') if pid == 3 else raw.decode('mac-roman')
                        except (UnicodeDecodeError, LookupError):
                            continue
                        s = s.strip()
                        if s:
                            names.add(s)
                    break  # 一个子字体只需处理一次 name 表
    except OSError:
        pass
    if not names:
        stem = os.path.splitext(os.path.basename(path))[0]
        if stem:
            names.add(stem)
    return names


def fc_list_families():
    """Linux/装有 fontconfig 的机器上用 fc-list 兜底，覆盖任意自定义字体路径。"""
    try:
        out = subprocess.run(['fc-list', ':', 'family'], capture_output=True,
                             text=True, timeout=60).stdout
    except Exception:
        return set()
    fams = set()
    for ln in out.splitlines():
        for fam in ln.split(','):
            fam = fam.strip()
            if fam:
                fams.add(fam)
    return fams


def system_font_dirs():
    home = os.path.expanduser('~')
    if sys.platform == 'darwin':
        dirs = [os.path.join(home, 'Library/Fonts'), '/Library/Fonts',
                '/System/Library/Fonts']
    elif os.name == 'nt':
        windir = os.environ.get('WINDIR', r'C:\Windows')
        dirs = [os.path.join(windir, 'Fonts'),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Microsoft', 'Windows', 'Fonts')]
    else:
        dirs = [os.path.join(home, '.fonts'), os.path.join(home, '.local/share/fonts'),
                '/usr/share/fonts', '/usr/local/share/fonts']
    return [d for d in dirs if d and os.path.isdir(d)]


def scan(dirs):
    """返回 {家族名: 来源路径或'(fc-list)'}"""
    found = {}
    for d in dirs:
        for root, _dirs, files in os.walk(d):
            for fn in files:
                if not fn.lower().endswith(FONT_EXTS):
                    continue
                p = os.path.join(root, fn)
                for fam in sfnt_families(p):
                    found.setdefault(fam, p)
    return found


def main(argv):
    only_mode = '--only' in argv
    args = [a for a in argv if a != '--only']
    dirs = [d for d in args if os.path.isdir(d)]
    if not only_mode:
        dirs = system_font_dirs() + dirs
    found = scan(dirs)
    if not only_mode:
        for fam in fc_list_families():
            found.setdefault(fam, '(fc-list)')

    print('公文规范字体检查' + ('（仅指定目录）' if only_mode else '') + '\n')
    missing = []
    for aliases, role, kws in REQUIRED:
        hit = next((a for a in aliases if a in found), None)
        if hit:
            print(f'  [OK]   {aliases[0]:<10} — {found[hit]}')
        else:
            missing.append(aliases)
            print(f'  [缺失] {aliases[0]:<10} — 用途: {role}')
            near = [f for f in found
                    if any(k in f.lower() for k in kws) and f not in aliases]
            if near:
                show = '、'.join(sorted(near)[:5])
                print(f'         近似提示: 检测到 [{show}]，但家族名不匹配；'
                      f'docx 中引用的是「{aliases[0]}」，需精确安装该名称的字体')

    if not missing:
        print('\n全部齐备，可以开始生成公文。')
        return 0
    print(f'\n缺 {len(missing)} 款字体。请用户自行安装后重跑本脚本（不可用其他字体替代）：')
    for aliases in missing:
        print(f'  · {aliases[0]}（或其别名 {"/".join(aliases[1:])}）: {CHANNELS.get(aliases[0], "")}')
    print('  注意: 规范字体均为商业版权（方正/中易/长城），本 skill 不随附也不得再分发字体文件；'
          '\n        下载与安装来源的合规性由使用者自行把握。')
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
