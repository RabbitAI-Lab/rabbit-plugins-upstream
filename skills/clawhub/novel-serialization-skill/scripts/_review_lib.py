# -*- coding: utf-8 -*-
"""
审稿脚本公共库（内部模块，不直接执行）

为 scripts/ 下各 review_*.py 提供统一能力：
  - 项目根判定与章节索引（兼容 `第NNN章 标题.md` 与 `ch-NNN-title.md` 两种命名）
  - 正文抽取（去 YAML frontmatter / 元数据引用行 / 代码块）与中文字数口径
  - Issue / Result 数据结构、等级汇总与 Markdown 报告渲染

等级约定（与 humanizer_check.py 一致）：
    FAIL —— 必须修改，不得进定稿
    WARN —— 需人工复核确认（综合结论记 REVISE）
    PASS —— 达标
"""
import os
import re
import sys
import glob
import datetime
from collections import namedtuple

sys.stdout.reconfigure(encoding='utf-8')

LEVEL_ORDER = {"PASS": 0, "WARN": 1, "FAIL": 2}

# 章节文件名识别：`第001章 xxx.md`（子项目口径）优先，其次 `ch-001-xxx.md`（通用口径）
PAT_CN_CHAPTER = re.compile(r'第(\d+)章')
PAT_EN_CHAPTER = re.compile(r'^ch[-_]?(\d+)', re.I)
# 草稿/大纲中的章节标题行：`## 第001章 xxx` 或 `## Chapter 001 xxx`
PAT_HEAD_CN = re.compile(r'^(?:#{1,3}\s*)?第(\d+)章\s*(.*)$')
PAT_HEAD_EN = re.compile(r'^(?:#{1,3}\s*)?ch(?:apter)?[-_ ]?(\d+)\s*[—\-:：]?\s*(.*)$', re.I)

CN_RE = re.compile(r'[\u4e00-\u9fff]')

Issue = namedtuple('Issue', ['level', 'category', 'detail', 'where'])
Result = namedtuple('Result', ['name', 'path', 'issues', 'stats'])
Item = namedtuple('Item', ['num', 'name', 'path', 'text'])


# ---------- 项目根与文件定位 ----------

def find_root(root=''):
    """项目根：默认当前工作目录，须含 chapters/ 或 notes-personal/"""
    r = os.path.abspath(root) if root else os.getcwd()
    if not (os.path.isdir(os.path.join(r, 'chapters')) or os.path.isdir(os.path.join(r, 'notes-personal'))):
        raise SystemExit('根目录异常（未找到 chapters/ 或 notes-personal/）：%s\n'
                         '请在子项目根目录执行，或用 --root 指定。' % r)
    return r


def chapter_index(root='', pattern='chapters/**/*.md'):
    """{章号(int): 路径}，跳过 `_幕导语.md` 一类非章节文件"""
    root = root or os.getcwd()
    idx = {}
    for p in sorted(glob.glob(os.path.join(root, pattern), recursive=True)):
        name = os.path.basename(p)
        m = PAT_CN_CHAPTER.search(name) or PAT_EN_CHAPTER.match(name)
        if not m:
            continue
        if os.path.basename(os.path.dirname(p)).startswith('_'):
            continue
        idx[int(m.group(1))] = p
    return idx


def draft_blocks(path):
    """解析 notes-personal/ 单文件草稿：{章号(int): (标题, 正文块)}"""
    if not os.path.exists(path):
        return {}
    lines = open(path, encoding='utf-8').read().split('\n')
    heads = [(i, l) for i, l in enumerate(lines) if PAT_HEAD_CN.match(l) or PAT_HEAD_EN.match(l)]
    out = {}
    for k, (i, l) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        m = PAT_HEAD_CN.match(l) or PAT_HEAD_EN.match(l)
        out[int(m.group(1))] = (l.strip(), '\n'.join(lines[i + 1:end]).strip('\n'))
    return out


def chapter_title(text):
    """取文本中的章标题（去 `#` 前缀）"""
    for ln in text.split('\n'):
        m = PAT_HEAD_CN.match(ln) or PAT_HEAD_EN.match(ln)
        if m:
            return m.group(2).strip()
    return ''


# ---------- 正文处理 ----------

def strip_frontmatter(text):
    lines = text.split('\n')
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return '\n'.join(lines[i + 1:])
    return text


def strip_code(text):
    return re.sub(r'```.*?```', '', text, flags=re.S)


def body_lines(text):
    """正文行：去 frontmatter、代码块、元数据引用行"""
    text = strip_code(strip_frontmatter(text))
    return [ln for ln in text.split('\n') if not ln.lstrip().startswith('>')]


def cn(text):
    """中文字数（脚本口径）：去元数据行与标题行后的中文字符数"""
    return len(CN_RE.findall('\n'.join(
        l for l in body_lines(text) if not l.startswith('#'))))


def paragraphs(text):
    """正文段落（非空、非标题）"""
    return [p.strip() for p in '\n'.join(body_lines(text)).split('\n')
            if p.strip() and not p.lstrip().startswith('#')]


def narr(text):
    """剔除引号内对话后的叙述文本"""
    return re.sub(r'“[^”]*”', '', '\n'.join(body_lines(text)))


# ---------- 结果处理 ----------

def make_result(name, path, issues, stats=None):
    return Result(name=name, path=path, issues=issues, stats=stats or {})


def level_of(issues):
    lv = 'PASS'
    for i in issues:
        if LEVEL_ORDER.get(i.level, 0) > LEVEL_ORDER[lv]:
            lv = i.level
    return lv


def verdict(results):
    """综合判定：FAIL > REVISE(WARN) > PASS"""
    lv = 'PASS'
    for r in results:
        l = level_of(r.issues)
        if l == 'FAIL':
            return 'FAIL'
        if l == 'WARN':
            lv = 'REVISE'
    return lv


def count_levels(results):
    c = {'PASS': 0, 'WARN': 0, 'FAIL': 0}
    for r in results:
        c[level_of(r.issues)] += 1
    return c


# ---------- 报告渲染 ----------

def render(title, results, intro=None, extra_sections=None, obj_label='审查对象'):
    """渲染 Markdown 报告；extra_sections: [(小节标题, 文本)]"""
    c = count_levels(results)
    lines = ['# %s' % title, '',
             '> 生成时间：%s ｜ 判定口径：FAIL 必须修改，WARN 需人工复核，PASS 达标'
             % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')]
    if intro:
        lines += [''] + intro
    lines += ['', '## 一、结论', '',
              '- %s：%d' % (obj_label, len(results)),
              '- **PASS %d ｜ WARN(REVISE) %d ｜ FAIL %d**' % (c['PASS'], c['WARN'], c['FAIL']),
              '- 综合判定：**%s**' % verdict(results), '',
              '| 对象 | 判定 | 问题数 | 主要问题 |', '|---|---|---|---|']
    for r in results:
        main = '；'.join('%s(%s)' % (i.category, i.detail) for i in r.issues[:3]) or '—'
        lines.append('| `%s` | **%s** | %d | %s |' % (r.name, level_of(r.issues), len(r.issues), main))
    lines += ['', '## 二、问题明细', '']
    for r in results:
        if not r.issues:
            continue
        lines.append('### %s（%s）' % (r.name, level_of(r.issues)))
        for i in r.issues:
            loc = ' —— %s' % i.where if i.where else ''
            lines.append('- [%s] **%s**：%s%s' % (i.level, i.category, i.detail, loc))
        lines.append('')
    if not any(r.issues for r in results):
        lines.append('无。全部达标。')
    cn_num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    n = 2
    for head, txt in (extra_sections or []):
        n += 1
        lines += ['', '## %s、%s' % (cn_num[n - 1], head), '', txt]
    n += 1
    lines += ['', '---', '',
              '## %s、签字栏' % cn_num[n - 1], '',
              '- [ ] 主编复核：__________ ｜ 日期：__________',
              '- [ ] 复核结论：PASS / REVISE / FAIL', '']
    return '\n'.join(lines)


def emit(md, out=None):
    if out:
        d = os.path.dirname(os.path.abspath(out))
        if d:
            os.makedirs(d, exist_ok=True)
        open(out, 'w', encoding='utf-8').write(md)
        print('报告已写入：%s' % out)
    print(md)


def collect_items(root, chapters=(), draft=''):
    """统一采集审查对象：优先 --draft 草稿分章，否则 chapters/ 定稿分章"""
    items = []
    if draft:
        p = draft if os.path.isabs(draft) else os.path.join(root, draft)
        for n, (head, body) in sorted(draft_blocks(p).items()):
            items.append(Item(num=n, name=head.lstrip('#').strip() or ('第%03d章' % n),
                              path=p, text=body))
    else:
        idx = chapter_index(root)
        for n in select_chapters(idx, chapters):
            p = idx[n]
            items.append(Item(num=n, name=os.path.basename(p), path=p,
                              text=open(p, encoding='utf-8').read()))
    return items


def add_common_args(ap):
    """通用 CLI 参数"""
    ap.add_argument('--root', default='', help='项目根（默认当前工作目录，须含 chapters/ 或 notes-personal/）')
    ap.add_argument('--chapters', nargs='*', default=[], help='只审指定章号，如 031 034')
    ap.add_argument('--draft', default='', help='草稿文件路径（审查草稿而非 chapters/ 定稿）')
    ap.add_argument('--out', default='', help='Markdown 报告输出路径')
    return ap


def select_chapters(idx, nums):
    if not nums:
        return sorted(idx)
    want = set()
    for n in nums:
        want.add(int(re.sub(r'\D', '', n) or 0))
    return [n for n in sorted(idx) if n in want]
