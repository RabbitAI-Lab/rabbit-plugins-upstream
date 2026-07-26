"""
common.py — xhs-* 脚本共享的工具函数

被 xhs-fetch.py / xhs-harvest.py / xhs-keepalive.py 共同 import。
不要在这里 import 任何 xhs-* 特定模块 (会形成循环 import)。

提供:
  1. err() / ok()          - 人类可读输出
  2. err_struct()          - 人类可读 + 结构化错误码输出 (harvest 自动解析)
  3. parse_struct_error()  - 从 stderr 解析 error_code=XXX
  4. run()                 - subprocess 封装
  5. safe_int()            - 宽松 int 解析 (处理 '1.2万' / '3,456' / '10w+' / '')
  6. strip_author_suffix() - 清理 author 字段尾部的 '2天前/05-31/昨天' 等后缀
  7. author_matches()      - 判断 author 跟 query 是不是同一个人
"""

import re
import subprocess
import sys


# 标准错误码(harvest 解析后用 ERROR_CODES.get(code, code) 拿人类描述)
ERROR_CODES = {
    '300012': 'IP风控',
    '300011': '账号异常',
    '300031': '笔记不可见',
    '300017': 'url_invalid_xsec_token不匹配',
    'parse_fail': '解析失败',
    'author_mismatch': 'author不匹配',
    'author_not_found': 'author未找到',
    'captcha': '滑块验证',
    'blocked': '页面被风控',
    'unknown': '未知错误',
}


# ─────────────────────────────────────────────────────────────
# 基础输出
# ─────────────────────────────────────────────────────────────

def err(msg):
    """标准错误输出 (人类可读)"""
    print(f"❌ {msg}", file=sys.stderr)


def ok(msg):
    """标准成功输出"""
    print(f"✅ {msg}")


# ─────────────────────────────────────────────────────────────
# 结构化错误输出 (v1.4.0 改造)
# ─────────────────────────────────────────────────────────────

def err_struct(code, msg, hint=''):
    """结构化错误输出 — harvest 会自动解析 error_code=XXX 走对应分支

    stderr 输出格式:
        ❌ {msg}
           {hint}              (可选)
        [ERR] error_code={code},msg={msg}

    前两行人类可读,最后一行机器可读。
    harvest 用 parse_struct_error() 抓最后一行。
    """
    print(f"❌ {msg}", file=sys.stderr)
    if hint:
        print(f"   {hint}", file=sys.stderr)
    print(f"[ERR] error_code={code},msg={msg}", file=sys.stderr)


_STRUCT_RE = re.compile(r'\[ERR\] error_code=([^,\n]+),msg=(.*)$', re.MULTILINE)


def parse_struct_error(stderr):
    """从 stderr 解析结构化错误码,返 (code, msg) 或 (None, None)

    用法:
        code, msg = parse_struct_error(r.stderr)
        if code == '300012':
            return False, f"IP 风控 (300012)"
    """
    if not stderr:
        return None, None
    m = _STRUCT_RE.search(stderr)
    if not m:
        return None, None
    return m.group(1).strip(), m.group(2).strip()


# ─────────────────────────────────────────────────────────────
# subprocess / 解析 helper
# ─────────────────────────────────────────────────────────────

def run(cmd, timeout=30, check=True):
    """subprocess 封装,带超时和错误信息打印"""
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode != 0:
        print(f"  stdout: {r.stdout[:300]}", file=sys.stderr)
        print(f"  stderr: {r.stderr[:300]}", file=sys.stderr)
    return r


def safe_int(s, default=0):
    """宽松 int 解析: '1.2万' / '3,456' / '10w+' / '' / None 都能吃

    例子:
        safe_int('1.2万')    -> 12000
        safe_int('3,456')    -> 3456
        safe_int('10w+')     -> 100000
        safe_int('')         -> default
        safe_int(None)       -> default
    """
    try:
        s = str(s) if s is not None else ''
        s = s.replace(',', '').replace('+', '').replace('万', '0000').replace('赞', '').strip()
        return int(s) if s else default
    except (ValueError, TypeError):
        return default


# ─────────────────────────────────────────────────────────────
# author 解析 helper
# ─────────────────────────────────────────────────────────────

_AUTHOR_SUFFIX_RE = re.compile(
    r'(\d+\s*(秒|分钟|小时|天|周|月)前|\d{1,2}-\d{1,2}|\d{1,2}月\d{1,2}日|昨天|今天|编辑于.*|分钟前来|小时前来)$'
)


def strip_author_suffix(author: str) -> str:
    """清理 author 字段尾部的 '2天前/05-31/昨天' 等时间后缀,只留昵称

    例: '影视飓风2天前' → '影视飓风'
        'Yonna语歌'     → 'Yonna语歌'  (无后缀不变)
        '改名了1天前'   → '改名了'
    """
    if not author:
        return ''
    s = author.strip()
    # 最多剥 2 次后缀(防止奇怪拼接)
    for _ in range(2):
        m = _AUTHOR_SUFFIX_RE.search(s)
        if m and m.start() > 0:
            s = s[:m.start()].strip()
        else:
            break
    return s


def author_matches(query: str, author: str) -> bool:
    """判断 search 命中的 author 是否就是 query 想要的那个用户

    规则(任一命中即可):
      - 完全相等
      - author 以 query 开头
      - query 以 author 开头(允许 query 比 author 更长)
    """
    a = strip_author_suffix(author)
    q = (query or '').strip()
    if not a or not q:
        return False
    return a == q or a.startswith(q) or q.startswith(a)
