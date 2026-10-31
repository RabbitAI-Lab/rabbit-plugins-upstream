"""把所有 skill 里的 CJK 版思源黑体换成 TrueType 版（Noto Sans CJK SC → Noto Sans SC）。

背景：CFF 轮廓的中文字体嵌进 PDF 是 CID Type 0C，部分手机渲染不出字形（中文乱码）。
Noto Sans SC 是同一套设计的 TrueType 打包，换格式不换样子（渲染像素 99.68% 相同）。

用法：
  python3 replace_cjk_fonts.py --dry-run    # 只看会改什么
  python3 replace_cjk_fonts.py             # 真的改（每处打印一行）
"""
import argparse
import os
import re

SKILLS = ['cn-word-card', 'wise-exam', 'daniel-exam', 'daniel-typeset',
          'daniel-reading', 'book-to-learn', 'my-pptx']
ROOT = '/root/.skills'

# 字体族名（带引号的三种写法）
FAMILY_SUBS = [
    ('"Noto Sans CJK SC"', '"Noto Sans SC"'),
    ("'Noto Sans CJK SC'", "'Noto Sans SC'"),
    ('"Noto Sans CJK JP"', '"Noto Sans SC"'),
    ('"Noto Sans CJK TC"', '"Noto Sans SC"'),
    ('"Noto Sans CJK HK"', '"Noto Sans SC"'),
]
# 字体文件路径（.ttc 的 CJK 版 → .ttf 的 SC 版）
PATH_SUBS = [
    ('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
     '/usr/local/share/fonts/custom/NotoSansSC-Regular.ttf'),
    ('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
     '/usr/local/share/fonts/custom/NotoSansSC-Bold.ttf'),
    ('NotoSansCJK-Regular.ttc', 'NotoSansSC-Regular.ttf'),
    ('NotoSansCJK-Bold.ttc', 'NotoSansSC-Bold.ttf'),
]

SKIP_EXT = ('.pyc', '.zip', '.ttf', '.otf', '.ttc', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.md')


def iter_files(skill_dir):
    for dirpath, _dirnames, filenames in os.walk(skill_dir):
        if '__pycache__' in dirpath:
            continue
        for fn in filenames:
            if fn.lower().endswith(SKIP_EXT) or (fn.lower().endswith('.md') and not os.environ.get('RF_INCLUDE_MD')):
                continue
            yield os.path.join(dirpath, fn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--skills', nargs='*', default=SKILLS)
    ap.add_argument('--include-md', action='store_true', help='连 .md 文档一起改（默认跳过，文档语义需人工核对）')
    a = ap.parse_args()

    total_files = 0
    total_hits = 0
    for sk in a.skills:
        d = os.path.join(ROOT, sk)
        if not os.path.isdir(d):
            print(f'[skip] {sk} 不存在')
            continue
        sk_files, sk_hits = 0, 0
        for path in iter_files(d):
            try:
                raw = open(path, 'rb').read()
                s = raw.decode('utf-8')
            except (UnicodeDecodeError, OSError):
                continue
            new = s
            for old, rep in FAMILY_SUBS + PATH_SUBS:
                if old in new:
                    new = new.replace(old, rep)
            if new != s:
                hits = sum(s.count(o) for o, _ in FAMILY_SUBS + PATH_SUBS)
                sk_files += 1
                sk_hits += hits
                rel = os.path.relpath(path, ROOT)
                if a.dry_run:
                    # 打印第一处命中行，便于核对
                    for line in s.splitlines():
                        if 'Noto Sans CJK' in line or 'NotoSansCJK' in line:
                            print(f'   {rel}: {line.strip()[:110]}')
                            break
                else:
                    open(path, 'w', encoding='utf-8').write(new)
                    open(path, 'rb').read().decode('utf-8')       # 编码自检
                    print(f'   ✓ {rel}（{hits} 处）')
        print(f'[{"dry" if a.dry_run else "done"}] {sk}: {sk_files} 个文件 / {sk_hits} 处')
        total_files += sk_files
        total_hits += sk_hits
    print(f'\n合计 {total_files} 个文件 / {total_hits} 处')
    if a.dry_run:
        print('（--dry-run，未改动任何文件）')


if __name__ == '__main__':
    main()
