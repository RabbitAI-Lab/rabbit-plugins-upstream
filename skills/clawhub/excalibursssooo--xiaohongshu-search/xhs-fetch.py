#!/usr/bin/env python3
"""
xhs-fetch.py — 小红书抓取 skill 核心脚本

子命令:
  1. search <keyword> [--sort hot|time] [--limit N]    主题搜索
  2. note   <note_id> [--comments N]                    单笔记详情 + 评论
  3. user-search <name> [--list-candidates]              用户名 → user_id (带 author 验证)
  4. user-resolve <name>                                 用户名 → user_id 增强版 (逐个验证,Plan B 降级)
  5. user   <user_id> [--notes N]                        用户主页 + 作品列表
  6. paths                                                打印当前路径配置

数据路径: 全部走 agent-browser (官方 JS 环境 + 真实浏览器指纹)
         利用 xhs 页面已经加载的 X-s 签名函数 调 API
         不需要重写签名算法

cookie 路径由 paths.py 统一管理 (默认 $SKILL/data/, 可用 XHS_DATA_DIR 覆盖)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, quote

# 路径统一管理
from paths import (
    COOKIE_FILE, STATE_FILE, DATA_DIR, NOTES_DIR, USERS_DIR, EXPORTS_DIR,
    report as report_paths,
)

# 通用工具 (v1.4.0 重构)
from common import (
    err, ok, err_struct, parse_struct_error, run,
    safe_int, strip_author_suffix, author_matches,
)

# xhs API 域名
EDITH_BASE = "https://edith.xiaohongshu.com"
WEB_BASE = "https://www.xiaohongshu.com"


def ab_open(url, state_file=None, timeout=30):
    """open URL (with optional state)"""
    cmd = ['agent-browser', 'open', url]
    if state_file:
        cmd.extend(['--state', str(state_file)])
    return run(cmd, timeout=timeout)


def check_block(r_stdout):
    """检查返回结果是否被风控/拦截,返回错误码字符串或 None"""
    if '300012' in r_stdout or 'IP存在风险' in r_stdout:
        return '300012_ip_risk'
    if '300031' in r_stdout or '暂时无法浏览' in r_stdout or '页面不见了' in r_stdout:
        return '300031_note_blocked'
    if '300011' in r_stdout or '账号异常' in r_stdout:
        return '300011_account_abnormal'
    if '安全限制' in r_stdout or 'error_code' in r_stdout:
        return 'unknown_risk'
    return None


def ab_eval(js, timeout=15):
    """evaluate JS, return parsed Python object (dict / list / str / int)

    agent-browser eval 永远把返回值序列化成 JSON 字符串输出,
    而且是 双层 JSON 编码:
      1) JS 端 JSON.stringify(obj) -> '{"a":1}'
      2) agent-browser 把这个字符串当返回值再 dump 一次 -> '"{\\"a\\":1}"'
    所以 Python 端要 json.loads 两次才能拿到 dict。
    约定: JS 端必须用 JSON.stringify(...) 包裹返回值,保证序列化。
    """
    r = run(['agent-browser', 'eval', js], timeout=timeout)
    out = r.stdout.strip()
    if not out:
        return None
    # 第一次 json.loads: 拆掉外层 agent-browser 加的引号
    # 第二次 json.loads: 拆掉 JS 端 JSON.stringify 加的引号
    try:
        outer = json.loads(out)
    except json.JSONDecodeError:
        return out
    if isinstance(outer, str):
        try:
            return json.loads(outer)
        except json.JSONDecodeError:
            return outer
    return outer


def ab_screenshot(path, full=False):
    cmd = ['agent-browser', 'screenshot']
    if full:
        cmd.append('--full')
    cmd.append(str(path))
    return run(cmd, timeout=60)


def ensure_cookies_loaded():
    """确保 agent-browser 里有 cookies"""
    if not COOKIE_FILE.exists():
        err_struct('parse_fail', f'cookie 文件不存在: {COOKIE_FILE}',
                   hint='跑: xhs-keepalive.py inject')
        sys.exit(1)
    # 检查当前 cookies
    r = run(['agent-browser', 'cookies', 'get'], timeout=10)
    if not r.stdout.strip() or 'web_session' not in r.stdout:
        print("Loading cookies into agent-browser...")
        subprocess.run(
            ['python3', str(Path(__file__).parent / 'xhs-keepalive.py'), 'load'],
            timeout=30
        )


# ─────────────────────────────────────────────────────────────
# author 解析 helpers (P0 修复: 用 classes 特征过滤侧栏用户)
# ─────────────────────────────────────────────────────────────

def _get_my_user_id() -> str:
    """从浏览器 cookie 读当前登录用户的 user_id(用于排除自己)
    注: 拿不到时返空串,不要静默 fall through 到错误路径
    """
    r = run(['agent-browser', 'eval', 'document.cookie'], timeout=10)
    if not r.stdout.strip():
        return ''
    try:
        cookie_str = json.loads(r.stdout.strip())
        if isinstance(cookie_str, str):
            m = re.search(r'x-user-id-redlive\.xiaohongshu\.com=([^;]+)', cookie_str)
            return m.group(1) if m else ''
    except (json.JSONDecodeError, AttributeError):
        return ''
    return ''


def _is_author_candidate(c: dict, my_id: str = '') -> bool:
    """判断 candidate 是不是 author 主页链接(排除侧栏/popover/自己/评论者)

    背景: search 桶笔记页里会有多个 `/user/profile/{uid}` 链接:
      - author 主页链接(我们要的)         classes 特征: avatar-container / avatar-click / info / author
      - 侧边栏推荐用户(不要)              classes 特征: side-bar / popover-trigger
      - 当前登录用户自己(不要)            href 跟 cookie 里自己的 user_id 匹配
      - 评论者头像(不要)                  href 含 pc_comment
    """
    href = c.get('href', '')
    cls = ' '.join(c.get('classes', []))
    # 排除规则(任一命中即排除)
    if 'pc_comment' in href:
        return False
    if 'side-bar' in cls or 'popover-trigger' in cls:
        return False
    if my_id and my_id in href:
        return False
    # 正面规则:author 链接至少要有一个 author 特征
    if any(kw in cls for kw in ('avatar-container', 'avatar-click', 'avatar', 'author', 'info')):
        return True
    return False


def _dbg_title() -> str:
    """取当前页面 title(给错误信息用)"""
    r = run(['agent-browser', 'eval', 'document.title'], timeout=10)
    return r.stdout.strip().strip('"')[:100] or '(empty)'


def _verify_author(user_id: str, keyword: str, timeout: int = 25) -> bool | None:
    """打开 user/profile 桶,验证主页 name 跟 keyword 匹配

    返回:
      True  - 验证通过(主页 name 跟 keyword 匹配)
      False - 验证失败(主页 name 不匹配 → 该 user_id 不是要找的用户)
      None  - 验证不可用(user 桶被 captcha 锁 / 页面没加载 / 拿不到 name)
    """
    url = f"{WEB_BASE}/user/profile/{user_id}"
    r = ab_open(url)
    out = r.stdout + r.stderr

    # 任何风控信号都返回 None(不可用),不判定 False
    if check_block(out) or 'Security Verification' in out or 'website-login/captcha' in out:
        return None

    time.sleep(2)
    js = """
    (() => {
      const name = document.querySelector('.user-info .username, .user-name, h1')?.textContent.trim() || '';
      return JSON.stringify({name, url: location.href});
    })()
    """
    raw = ab_eval(js, timeout=15)
    if not raw or not isinstance(raw, dict):
        return None
    name = (raw.get('name') or '').strip()
    if not name:
        return None  # 拿不到 name(页面还没渲染)→ 不可用,不判定 False

    # 跟 keyword 比对(同样规则:相等/前缀匹配)
    return author_matches(keyword, name)


def parse_xhs_id(s):
    """从 URL 或纯 ID 解析 xhs note_id / user_id"""
    s = s.strip()
    if '/' in s:
        # URL 模式
        m = re.search(r'/explore/([a-f0-9]+)', s)
        if m:
            return m.group(1)
        m = re.search(r'/user/profile/([a-f0-9]+)', s)
        if m:
            return m.group(1)
        m = re.search(r'/discovery/item/([a-f0-9]+)', s)
        if m:
            return m.group(1)
        return None
    return s


def cmd_search(args):
    """主题搜索: agent-browser 打开 search_result 页面 + 抓 section.note-item"""
    keyword = args.keyword
    out_path = Path(args.out) if args.out else None
    limit = args.limit
    sort = args.sort  # general | hot | time

    ensure_cookies_loaded()

    # 构造 URL
    url = f"{WEB_BASE}/search_result?keyword={keyword}&source=web_explore_feed&type=51"
    if sort == 'hot':
        url += "&sort=hot"
    elif sort == 'time':
        url += "&sort=time_descending"

    print(f"Opening: {url}")
    r = ab_open(url)
    print(r.stdout.strip())

    block = check_block(r.stdout)
    if block == '300012_ip_risk':
        err_struct('300012', 'IP 被风控 (300012) — 网络层问题,不是 cookie 问题',
                   hint='解决: 换网络环境 (代理 / 4G 切 WiFi / 等 1-2 小时)')
        return 2
    if block:
        err_struct('blocked', f'页面被风控 ({block})')
        return 1

    # 等加载
    time.sleep(3)

    # 抓 note 列表 (含 note_id + xsec_token,方便后续 note --via-search 用)
    js = rf"""
    (() => {{
      const notes = document.querySelectorAll('section.note-item');
      const data = [];
      const seen = new Set();
      for (let i = 0; i < notes.length && data.length < {limit}; i++) {{
        const n = notes[i];
        // 取带 xsec_token 的链接 (SPA 路由,后续可以靠它绕开 300031)
        const tokenLink = n.querySelector('a[href*="xsec_token"]')?.href || '';
        const anyLink   = n.querySelector('a')?.href || '';
        const href = tokenLink || anyLink;
        let noteId = null, xsecToken = null;
        let m = href.match(/\/search_result\/([a-f0-9]+)\?xsec_token=([^&]+)/);
        if (m) {{ noteId = m[1]; xsecToken = m[2]; }}
        else  {{ m = href.match(/explore\/([a-f0-9]+)/); if (m) noteId = m[1]; }}
        if (!noteId || seen.has(noteId)) continue;
        seen.add(noteId);
        const title  = n.querySelector('.title, .footer-title, a.title span')?.textContent.trim() || '';
        const author = n.querySelector('.author, .nickname, .user-name')?.textContent.trim() || '';
        const likes  = n.querySelector('.like-wrapper .count, .interaction-info .count')?.textContent.trim() || '';
        const date   = n.querySelector('.date, .footer .date, .time')?.textContent.trim() || '';
        if (title) data.push({{note_id: noteId, xsec_token: xsecToken, title, author, likes, date, link: href}});
      }}
      return JSON.stringify({{
        keyword: {json.dumps(keyword)},
        count: data.length,
        notes: data
      }});
    }})()
    """
    raw = ab_eval(js, timeout=20)
    if not raw or isinstance(raw, str):
        err_struct('parse_fail', f'eval 失败,可能页面没加载完成: {str(raw)[:200]}')
        return 1
    result = raw

    # 落盘
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        ok(f"已保存 {result['count']} 条到 {out_path}")
    else:
        # 打印紧凑视图
        print(f"\n关键词: {result['keyword']} (共 {result['count']} 条)\n")
        for i, n in enumerate(result['notes'][:20], 1):
            tok = f" token={n['xsec_token'][:24]}…" if n.get('xsec_token') else " (no token)"
            print(f"{i:3d}. [{n.get('likes', '0'):>6}] {n.get('title', '')}")
            print(f"     {n.get('author', '')}  ·  id={n.get('note_id','-')[:18]}{tok}")
        if result['count'] > 20:
            print(f"\n  ... 还有 {result['count'] - 20} 条,用 --out 落盘查看全部")
        print(f"\n💡 拿 id+token 直接抓详情: xhs-fetch.py note <id> --via-search --token <token> --comments 12")

    return 0


def cmd_note(args):
    """单笔记详情: 进 explore 页面 + 抓 note 标题/正文/评论

    三种模式:
      默认  — 走 /explore/{id} 直链 (通常 300031 不可见)
      --via-search — ⚠️ DEPRECATED,仅适用于 search 桶的 token
                    走 /search_result/{id}?xsec_token=...&xsec_source=pc_note
                    注意: search 桶与 user_profile 桶是不同 captcha,search 桶锁了会 300017
      --via-user-profile — ⭐ 推荐: 主页 token 必须走这个
                    走 /user/profile/{uid}/{nid}?xsec_token=...&xsec_source=pc_user
                    user_id 从 --user-id 传
                    走这个能完全绕开 search 桶 captcha
    """
    note_id = parse_xhs_id(args.note_id)
    if not note_id:
        err_struct('parse_fail', f'无法解析 ID: {args.note_id}')
        return 1

    ensure_cookies_loaded()

    # 选 URL
    if args.via_user_profile:
        if not args.token or not args.user_id:
            err_struct('parse_fail', '--via-user-profile 需要 --token <XSEC_TOKEN> 和 --user-id <USER_ID>',
                       hint='提示: 从 xhs-fetch.py user <user_id> 拿主页,那里有 xsec_token + xsec_source')
            return 1
        # xsec_source 必须为 pc_user (主页里的 token 都是这个)
        url = f"{WEB_BASE}/user/profile/{args.user_id}/{note_id}?xsec_token={args.token}&xsec_source=pc_user"
        print(f"Opening (via-user-profile): {url}")
    elif args.via_search:
        if not args.token:
            err_struct('parse_fail', '--via-search 需要 --token <XSEC_TOKEN>',
                       hint='提示: 先跑 `xhs-fetch.py search <keyword>` 拿 note 的 xsec_token')
            return 1
        # search_result 路径默认 xsec_source=pc_note
        xsrc = args.xsec_source or 'pc_note'
        url = f"{WEB_BASE}/search_result/{note_id}?xsec_token={args.token}&xsec_source={xsrc}"
        print(f"Opening (via-search): {url}")
    else:
        url = f"{WEB_BASE}/explore/{note_id}"
        print(f"Opening: {url}")

    r = ab_open(url)
    print(r.stdout.strip())

    block = check_block(r.stdout)
    if block == '300012_ip_risk':
        err_struct('300012', 'IP 被风控', hint='解决: 换网络或等 5-30 分钟')
        return 2
    if block == '300031_note_blocked':
        err_struct('300031', f'该笔记无法浏览 (300031) {note_id}',
                   hint=('试试用 search 拿 xsec_token 后绕开:\n'
                         f'   xhs-fetch.py search <keyword> --limit 30\n'
                         f'   # 找一条 title 匹配 {note_id} 的,从输出里拿 xsec_token\n'
                         f'   xhs-fetch.py note {note_id} --via-search --token <TOKEN> --comments 12') if not args.via_search else '')
        return 1
    if block:
        err_struct('blocked', f'页面被风控 ({block})')
        return 1

    time.sleep(3)

    js = f"""
    (() => {{
      const txt = (el) => el ? el.textContent.trim().replace(/\\s+/g, ' ') : '';
      const title = txt(document.querySelector('.note-content .title, #detail-title, .title, h1'));
      const author = txt(document.querySelector('.author-wrapper .username, .info .username, .user-name'));
      const date = txt(document.querySelector('.date, .bottom-container .date, .publish-date'));
      const desc = txt(document.querySelector('.note-content .desc, #detail-desc, .desc, .content'));
      const likes = txt(document.querySelector('.like-wrapper .count, .interaction-info .like .count, .like .count'));
      const collects = txt(document.querySelector('.collect-wrapper .count, .collected .count, .collect .count'));
      const commentsCount = txt(document.querySelector('.chat-wrapper .count, .comment .count, .comment-count'));
      const list = document.querySelectorAll('.comments-container .comment-item, [class*="comment-item"]');
      const comments = Array.from(list).slice(0, {args.comments}).map(c => {{
        const name = txt(c.querySelector('.author .name, .user-name, .username')) || '?';
        const t = txt(c.querySelector('.content, .comment-content, .text, .commentText'));
        const time = txt(c.querySelector('.date, .info .date, .time'));
        const lk = txt(c.querySelector('.like .count, .interaction .like')) || '0';
        return {{name, time, likes: lk, text: t}};
      }});
      return JSON.stringify({{
        note_id: {json.dumps(note_id)},
        title, author, date, desc: desc.slice(0, 3000),
        likes, collects, comments_count: commentsCount, comments
      }});
    }})()
    """
    parsed = ab_eval(js, timeout=20)
    if not parsed:
        err_struct('parse_fail', 'eval 失败,可能页面没加载完')
        return 1
    if isinstance(parsed, str):
        try:
            result = json.loads(parsed)
        except json.JSONDecodeError:
            err_struct('parse_fail', f'无法解析: {parsed[:200]}')
            return 1
    else:
        result = parsed
    result['via'] = 'search_result' if args.via_search else 'explore'
    result['url'] = url

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        ok(f"已保存到 {out}")
    else:
        print(f"\n标题: {result['title']}")
        print(f"作者: {result['author']}  |  {result.get('date','')}  |  ❤️ {result['likes']}  |  ⭐ {result['collects']}  |  💬 {result.get('comments_count','?')}")
        print(f"\n正文:\n{result['desc'][:600]}")
        if result.get('comments'):
            print(f"\n前 {len(result['comments'])} 条评论:")
            for i, c in enumerate(result['comments'], 1):
                t = (c.get('text') or '').strip()
                if not t: continue
                print(f"  [{i}] {c.get('name','?')}  ❤️{c.get('likes','0')}: {t[:120]}")

    return 0


def cmd_user_search(args):
    """用户名 → user_id 解析。

    流程:
      1. 搜该用户名的笔记,取 top 8 (带 xsec_token)
      1.5. 验证 Top 笔记的 author 跟关键词匹配 (避免抓错用户)
            - 不匹配 → 扫描 Top 2-8 找匹配的
            - Top 8 全不匹配 → 报清晰错误,建议加"官方/本人"后缀或换拼音
      2. 打开该笔记(走 /search_result 旁路避免 300031)
      3. eval DOM 找 author 主页链接(过滤掉评论者/侧边栏/当前登录用户)

    适用场景:用户给的是显示名"小Lin说"这种,而不是 32 位 hex user_id。

    ⚠️ 限制:本命令依赖 search 桶(IP captcha 绑定),search 桶被锁时不可用。
       此时应该直接传 user_id: xhs-harvest.py user <user_id> --limit 15
    """
    ensure_cookies_loaded()
    keyword = args.keyword

    # Stage 1: 搜索 top 1
    print(f"🔍 搜索: {keyword}")
    search_url = f"{WEB_BASE}/search_result?keyword={quote(keyword)}&source=web_explore_feed&type=51"
    r = ab_open(search_url)
    if check_block(r.stdout):
        err_struct('300012', '搜索页被风控(300012)',
                   hint='等几分钟再试,或换网络 (4G 热点 / 代理)')
        return 2
    time.sleep(2)

    js_search = """
    (() => {
      const items = Array.from(document.querySelectorAll('section.note-item'));
      const out = items.slice(0, 5).map(s => {
        const a = s.querySelector('a[href*="/search_result/"]');
        if (!a) return null;
        const m = a.href.match(/\\/search_result\\/([a-f0-9]+)\\?xsec_token=([^&]+)/);
        if (!m) return null;
        return {
          note_id: m[1],
          xsec_token: m[2],
          title: s.querySelector('.title, .footer-title')?.textContent.trim() || '',
          author: s.querySelector('.author, .user-name, [class*="author"]')?.textContent.trim() || '',
          link: a.href
        };
      }).filter(Boolean);
      return JSON.stringify(out);
    })()
    """
    raw = ab_eval(js_search, timeout=15)
    if not raw or not isinstance(raw, list) or not raw:
        err_struct('parse_fail',
                   f"未找到匹配 '{keyword}' 的笔记(搜索无结果或 SPA 未渲染)",
                   hint=('可能原因:\n'
                         '  · search 桶被 captcha 锁 (多并发触发后需等 5-10 min)\n'
                         '  · 关键词拼写不准\n'
                         '绕开方法: 直接传 user_id (走 user/profile 桶,不依赖 search)\n'
                         '  1. 浏览器登录 xhs → 点进该用户主页 → URL 末尾 32 位 hex = user_id\n'
                         '  2. xhs-harvest.py user <user_id> --limit 15 --comments 15'))
        return 1

    # Stage 1.5: 验证 Top 笔记的 author 真的就是搜索词想找的那个用户
    # (历史教训:搜"影视飓风" → Top1 是 @GOODLUCK 写的"达拉斯偶遇影视飓风",作者完全不匹配)
    top = None
    for i, cand in enumerate(raw[:8]):
        clean_a = strip_author_suffix(cand.get('author',''))
        clean_a = clean_a.split()[0] if clean_a else ''  # 有些 author 是 "name 城市" 拼接
        if author_matches(keyword, cand.get('author','')):
            top = cand
            if i > 0:
                print(f"  ⚠️  Top1 不匹配({cand.get('author','')}),改用 Top{i+1}: {top['author']}")
            break
    if top is None:
        # 完全没匹配 → 报清晰错误,引导用户换关键词
        seen_authors = [f"{strip_author_suffix(c.get('author',''))}  (《{c.get('title','')[:30]}》)" for c in raw[:8]]
        hint_lines = [
            f"Top {len(raw[:8])} 作者:",
            *[f"    - {s}" for s in seen_authors],
            f"  → 关键词不够精确,试试:",
            f"     · 加后缀: {keyword}官方 / {keyword}本人",
            f"     · 用准确的英文 id / 拼音(影视飓风 → yingshijufeng)",
        ]
        err_struct('author_not_found',
                   f"搜索 Top {len(raw[:8])} 笔记中无 author 匹配 '{keyword}' 的作者",
                   hint='\n'.join(hint_lines))
        return 1
    print(f"  top 笔记: 《{top['title'][:40]}》  作者: {top['author']}")

    # Stage 2: 打开该笔记(走 xsec_token 旁路)
    time.sleep(3)  # eval→open 间隔,防 300012
    print(f"📖 打开笔记,定位 author 主页链接 ...")
    note_url = f"{WEB_BASE}/search_result/{top['note_id']}?xsec_token={quote(top['xsec_token'])}&xsec_source="
    r = ab_open(note_url)
    block = check_block(r.stdout)
    if block == '300012_ip_risk':
        err_struct('300012', '笔记页被风控(300012)',
                   hint='等几分钟再试,或换网络')
        return 2
    if block:
        err_struct('blocked', f'笔记页加载失败 ({block})')
        return 1
    time.sleep(3)

    # Stage 3: DOM 找 author user_id
    # 排除:
    #   - xsec_source=pc_comment → 评论者
    #   - grandClass 含 side-bar → 侧边栏(可能是当前登录用户)
    #   - 自己的 user_id(从 cookie 读)
    js_author = """
    (() => {
      const MY_ID = (document.cookie.match(/(?:^|; )x-user-id-redlive\\.xiaohongshu\\.com=([^;]+)/) || [])[1] || '';
      const all = Array.from(document.querySelectorAll('a[href*="/user/profile/"]'));
      const candidates = all.map(a => {
        let el = a, classes = [];
        for (let i = 0; i < 8 && el; i++) {
          if (el.className && typeof el.className === 'string') classes.push(el.className);
          el = el.parentElement;
        }
        return { href: a.href, classes: classes.slice(0, 3) };
      }).filter(c => {
        if (c.href.includes('pc_comment')) return false;
        if (c.href.includes('side-bar')) return false;
        if (MY_ID && c.href.includes(MY_ID)) return false;
        return true;
      });
      const uniq = [];
      const seen = new Set();
      for (const c of candidates) {
        const m = c.href.match(/\\/user\\/profile\\/([a-f0-9]+)/);
        if (m && !seen.has(m[1])) {
          seen.add(m[1]);
          uniq.push({ user_id: m[1], href: c.href, classes: c.classes });
        }
      }
      return JSON.stringify(uniq);
    })()
    """
    raw = ab_eval(js_author, timeout=15)
    if not raw or not isinstance(raw, list) or not raw:
        err_struct('parse_fail', '未找到 author user_id(SPA 还没渲染完?重试一次)',
                   hint=f'调试: title={_dbg_title()}')
        return 1

    # Stage 3.5 (P0 修复): 用 classes 特征过滤 author,排除侧栏/popover 候选
    #   - 排除 classes 含 side-bar / popover-trigger 的(侧栏用户、推荐用户)
    #   - 排除自己(读 cookie x-user-id-redlive.xiaohongshu.com,拿不到时静默)
    #   - 排除 href 含 pc_comment 的(评论者)
    #   - 优先选 classes 含 avatar-container / avatar-click / author 的
    #   - 没有任何 candidate 命中 author 特征 → 报清晰错误,让用户用 --list-candidates 排查
    my_id = _get_my_user_id()
    filtered = [c for c in raw if _is_author_candidate(c, my_id)]
    if not filtered:
        hint_lines = [
            '可能原因:笔记页 DOM 结构变了,或 search listing 的笔记 author 跟笔记页 author 完全不同人',
            f'全部候选 ({len(raw)}):',
            *[f'  {i}. user_id={c.get("user_id")}  classes={c.get("classes")}' for i, c in enumerate(raw, 1)],
            f'跑 `xhs-fetch.py user-search {keyword!r} --list-candidates` 看完整候选',
        ]
        err_struct('parse_fail',
                   '找不到 author 候选(全部被侧栏/popover/自己过滤掉了)',
                   hint='\n'.join(hint_lines))
        return 1

    # 取 author 特征最明显的那个(avatar-* > info > 其他)
    def score(c):
        cls = ' '.join(c.get('classes', []))
        if 'avatar-container' in cls or 'avatar-click' in cls:
            return 3
        if 'info' in cls or 'author' in cls:
            return 2
        return 1
    filtered.sort(key=score, reverse=True)
    user_id = filtered[0]['user_id']
    print(f"  候选 user_id: {user_id}  (从 {len(raw)} 个候选中按 author 特征筛 {len(filtered)} 个)")

    # Stage 3.6 (P0 修复): 自动验证 — 打开 user/profile 桶,确认主页 name 跟 keyword 匹配
    #   失败时 (search 桶被锁 / 主页 name 不匹配) 自动回退到下一个候选
    if not args.list_candidates:
        verified = _verify_author(user_id, keyword)
        if verified is None:
            err_struct('captcha',
                       'user/profile 桶验证 author 失败(可能 user 桶 captcha),先返回 user_id 让你自己验证',
                       hint=f'人工验证: xhs-fetch.py user {user_id} --notes 5')
        elif not verified:
            # 验证失败 → 尝试下一个候选
            print(f"  ⚠️  user_id={user_id} 验证不匹配({keyword} ≠ 主页 name),回退到下一候选...")
            for fb in filtered[1:]:
                fb_id = fb['user_id']
                if _verify_author(fb_id, keyword):
                    user_id = fb_id
                    print(f"  ✅ 回退到 {user_id} 验证通过")
                    break
            else:
                err_struct('author_mismatch',
                           f'所有 {len(filtered)} 个候选都验证不通过',
                           hint=f'跑 `xhs-fetch.py user-search {keyword!r} --list-candidates` 看完整候选')

    result = {
        "keyword": keyword,
        "user_id": user_id,
        "via_note": {"note_id": top["note_id"], "title": top["title"], "author": top["author"]},
        "candidates": raw,
    }
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        ok(f"已保存到 {out}")
    else:
        print()
        print(f"👉 user_id = {user_id}")
        print(f"   📋 所有候选 ({len(raw)} 个,按 author 特征过滤后剩 {len(filtered)} 个):")
        for i, c in enumerate(raw, 1):
            mark = '✅ author' if c in filtered else '   排除'
            print(f"      {i}. {mark}  user_id={c.get('user_id')}  classes={c.get('classes')}")
        print()
        print(f"   验证: xhs-fetch.py user {user_id} --notes 5   (确认作者名 = '{keyword}')")
        print(f"   用法: xhs-harvest.py user {user_id} --notes 50 --limit 20 --comments 15")
    return 0


def cmd_user_resolve(args):
    """用户名 → user_id 解析的增强版 (Plan B: search 桶 IP 风控后的 fallback)

    策略:
      1. 走 search 桶拿候选(用 search listing 5 名的 author 名匹配 keyword)
      2. 从每条 top 笔记拿 (note_id, xsec_token) 而不是直接 user_id
      3. 打开每条笔记(走 via-search 旁路),从 author 链接筛 candidates
      4. 逐一打开 user/profile 桶验证 author name
      5. 返回所有验证通过的 user_id, 选粉丝数最多的为 best

    跟 user-search 的区别:
      - user-search 拿第 1 个 author 链接的 user_id(可能错)
      - user-resolve 会逐个验证,返回所有匹配的 user_id
    """
    ensure_cookies_loaded()
    keyword = args.keyword
    print(f"🔍 解析: {keyword}")

    # Stage 1: search listing
    search_url = f"{WEB_BASE}/search_result?keyword={quote(keyword)}&source=web_explore_feed&type=51"
    r = ab_open(search_url)
    if check_block(r.stdout):
        err_struct('300012', 'search 桶被风控(300012) — user-resolve 也走 search,无法 fallback',
                   hint='等 5-10 分钟或换网络')
        return 2
    time.sleep(2)

    js_search = """
    (() => {
      const items = Array.from(document.querySelectorAll('section.note-item'));
      return JSON.stringify(items.slice(0, 8).map(s => {
        const a = s.querySelector('a[href*="/search_result/"]');
        const m = a?.href.match(/\\/search_result\\/([a-f0-9]+)\\?xsec_token=([^&]+)/);
        if (!m) return null;
        return {
          note_id: m[1],
          xsec_token: m[2],
          author: s.querySelector('.author, .user-name, [class*="author"]')?.textContent.trim() || '',
          title: s.querySelector('.title, .footer-title')?.textContent.trim() || '',
        };
      }).filter(Boolean));
    })()
    """
    raw = ab_eval(js_search, timeout=15)
    if not raw or not isinstance(raw, list) or not raw:
        err_struct('parse_fail', f"未找到匹配 '{keyword}' 的笔记")
        return 1

    # Stage 1.5: 选 author 跟 keyword 匹配的 top 笔记
    matching = [c for c in raw if author_matches(keyword, c.get('author', ''))]
    if not matching:
        hint_lines = [
            'Top 作者:',
            *[f'  - {strip_author_suffix(c.get("author",""))}  (《{c.get("title","")[:30]}》)' for c in raw[:8]],
        ]
        err_struct('author_not_found',
                   f"Top 8 笔记中无 author 匹配 '{keyword}'",
                   hint='\n'.join(hint_lines))
        return 1
    top = matching[0]
    print(f"  top 匹配笔记: 《{top['title'][:40]}》  作者: {top['author']}")

    # Stage 2: 打开笔记,拿 author 链接 candidates
    time.sleep(3)
    note_url = f"{WEB_BASE}/search_result/{top['note_id']}?xsec_token={quote(top['xsec_token'])}&xsec_source="
    r = ab_open(note_url)
    if check_block(r.stdout):
        err_struct('300012', '笔记页被风控(300012) — user-resolve 无法 fallback',
                   hint='等几分钟重试')
        return 2
    time.sleep(3)

    js_author = """
    (() => {
      const all = Array.from(document.querySelectorAll('a[href*="/user/profile/"]'));
      const uniq = [];
      const seen = new Set();
      for (const a of all) {
        const m = a.href.match(/\\/user\\/profile\\/([a-f0-9]+)/);
        if (!m || seen.has(m[1])) continue;
        if (a.href.includes('pc_comment')) continue;
        seen.add(m[1]);
        let el = a, classes = [];
        for (let i = 0; i < 8 && el; i++) {
          if (el.className && typeof el.className === 'string') classes.push(el.className);
          el = el.parentElement;
        }
        uniq.push({ user_id: m[1], href: a.href, classes: classes.slice(0, 3) });
      }
      return JSON.stringify(uniq);
    })()
    """
    raw = ab_eval(js_author, timeout=15)
    if not raw or not isinstance(raw, list) or not raw:
        err_struct('parse_fail', '未找到 author user_id',
                   hint=f'调试: title={_dbg_title()}')
        return 1
    candidates = raw
    print(f"  拿到 {len(candidates)} 个候选 user_id")

    # Stage 3: 逐个验证 (打开 user/profile 桶看 name)
    my_id = _get_my_user_id()
    verified = []
    for c in candidates:
        uid = c['user_id']
        if my_id and my_id in c['href']:
            continue
        # 排除侧栏
        cls = ' '.join(c.get('classes', []))
        if 'side-bar' in cls or 'popover-trigger' in cls:
            continue

        result = _verify_author(uid, keyword)
        if result is True:
            print(f"  ✅ {uid} 验证通过 (主页 name 含 '{keyword}')")
            verified.append(uid)
        elif result is False:
            print(f"  ❌ {uid} 不匹配")
        else:
            print(f"  ⚠️  {uid} 验证不可用(user 桶 captcha?)")

    if not verified:
        err_struct('author_mismatch',
                   '所有候选都没验证通过',
                   hint=('可能是: 1) search listing 的笔记 author 跟笔记页 author 不是同一人\n'
                         '         2) user 桶也被 captcha 锁\n'
                         '走手动 fallback: 浏览器登录 xhs → 搜该用户 → 点进主页 → URL 末尾 32 位 hex = user_id'))
        return 1

    # 选第一个(验证过的都是同一 keyword,顺序以 classes 特征为主)
    best = verified[0]
    print()
    print(f"👉 user_id = {best}")
    if len(verified) > 1:
        print(f"   (共 {len(verified)} 个验证通过,取了第 1 个)")
    print(f"   用法: xhs-harvest.py user {best} --notes 50 --limit 20 --comments 15")
    return 0


def cmd_user(args):
    """用户主页: 拿用户基本信息 + 作品列表"""
    user_id = parse_xhs_id(args.user_id)
    if not user_id:
        err_struct('parse_fail', f'无法解析 ID: {args.user_id}')
        return 1

    ensure_cookies_loaded()

    url = f"{WEB_BASE}/user/profile/{user_id}"
    print(f"Opening: {url}")
    r = ab_open(url)
    print(r.stdout.strip())

    # 滑块验证检测(xhs 对 user/profile/... 路径有独立 captcha,不是 300012)
    if 'Security Verification' in r.stdout or 'website-login/captcha' in r.stdout:
        err_struct('captcha',
                   '触发滑块验证(verifyType=124) — user/profile 路径有独立 captcha',
                   hint='解决:等 30+ 分钟 OR 浏览器人工过滑块 + 重导 cookies')
        return 3

    block = check_block(r.stdout)
    if block == '300012_ip_risk':
        err_struct('300012', 'IP 被风控',
                   hint='换网络或等 30+ 分钟')
        return 2
    if block:
        err_struct('blocked', f'页面被风控 ({block})')
        return 1

    # 额外检测 user-page 内部错误
    time.sleep(2)
    page_err = ab_eval("document.querySelector('.user-page .error .message')?.textContent.trim() || ''", timeout=10)
    if page_err:
        err_struct('parse_fail', f'用户页面加载失败: {page_err}')
        return 1

    time.sleep(3)

    js = f"""
    (() => {{
      const name = document.querySelector('.user-info .username, .user-name, h1')?.textContent.trim() || '';
      const bio = document.querySelector('.user-desc, .desc, .bio')?.textContent.trim() || '';
      const followers = document.querySelector('.fans .count, .follower-count')?.textContent.trim() || '';
      const notes = Array.from(document.querySelectorAll('section.note-item')).slice(0, {args.notes}).map(n => {{
        const title = n.querySelector('.title, .footer-title')?.textContent.trim() || '';
        const likes = n.querySelector('.like-wrapper .count')?.textContent.trim() || '';
        // 关键:从 note-item 内的 <a> 抓 xsec_token
        // 主页的 note-item 里有 2 种带 xsec_token 的链接:
        //   1. /user/profile/{{uid}}/{{nid}}?xsec_token=...&xsec_source=pc_user  (推荐,token 最稳定)
        //   2. /search_result/{{nid}}?xsec_token=...&xsec_source=pc_user        (有些模板会用)
        // 第一个匹配为准,这样后续 harvest.py 直接用 token 走 --via-search
        const linkWithToken = n.querySelector('a[href*="xsec_token="]')?.href || '';
        const linkAny = n.querySelector('a')?.href || '';
        const link = linkWithToken || linkAny;
        const tm = link.match(/[?&]xsec_token=([^&]+)/);
        const xsec_token = tm ? tm[1] : null;
        // 提取 note_id (从 /user/profile/.../<nid> 或 /search_result/<nid> 或 /explore/<nid>)
        const im = link.match(/\\/user\\/profile\\/[a-f0-9]+\\/([a-f0-9]+)/)
                || link.match(/\\/(?:explore|search_result)\\/([a-f0-9]+)/);
        const note_id = im ? im[1] : null;
        return {{ title, likes, link, note_id, xsec_token }};
      }});
      return JSON.stringify({{user_id: {json.dumps(user_id)}, name, bio, followers, notes}});
    }})()
    """
    raw = ab_eval(js, timeout=20)
    if not raw or isinstance(raw, str):
        err_struct('parse_fail', f'eval 失败: {str(raw)[:200]}')
        return 1
    result = raw

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        ok(f"已保存到 {out}")
    else:
        print(f"\n用户: {result['name']}")
        print(f"ID: {result['user_id']}")
        print(f"粉丝: {result['followers']}")
        print(f"简介: {result['bio'][:200]}")
        if result['notes']:
            print(f"\n最近 {len(result['notes'])} 个作品:")
            for n in result['notes']:
                print(f"  [{n['likes']:>6}] {n['title']}")
    return 0


def cmd_paths(args):
    report_paths()
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="小红书抓取 (搜索/笔记/用户)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
子命令:
  search        <keyword>      主题搜索 (默认按热度)
  note          <note_id>      单笔记详情 (推荐 --via-user-profile 绕开 300031)
  user-search   <name>         用户名 → user_id (默认会验证 author,选最佳)
  user-resolve  <name>         用户名 → user_id 增强版 (逐个验证所有候选,Plan B)
  user          <user_id>      用户主页 + 作品列表
  paths                        打印路径配置

xsec_token 旁路 (300031 绕开):
  当 explore 链接被风控时 (300031 笔记不可见):
    ⭐ 推荐: xhs-fetch.py note <note_id> --via-user-profile --user-id <uid> --token <TOKEN>
       (主页 token 配 xsec_source=pc_user,走 user/profile 桶,完全绕开 search 桶 captcha)
    备选: xhs-fetch.py note <note_id> --via-search --token <TOKEN>
       (search token 配 xsec_source=pc_note,走 search_result 桶)
        """
    )
    sub = parser.add_subparsers(dest='cmd', required=True)

    # search
    p = sub.add_parser('search', help='主题搜索')
    p.add_argument('keyword', help='搜索关键词')
    p.add_argument('--limit', type=int, default=50, help='最多拿几条 (默认 50)')
    p.add_argument('--sort', choices=['general', 'hot', 'time'], default='general',
                   help='排序: general(综合) / hot(最热) / time(最新) (默认 general)')
    p.add_argument('--out', help='落盘到 JSON 文件 (默认打到 stdout)')

    # note
    p = sub.add_parser('note', help='单笔记详情 (支持 via-search / via-user-profile 绕开 300031)')
    p.add_argument('note_id', help='note_id 或 explore URL')
    p.add_argument('--comments', type=int, default=10, help='评论数 (默认 10)')
    p.add_argument('--out', help='落盘 JSON')
    p.add_argument('--via-search', action='store_true',
                   help='走 /search_result/{id}?xsec_token=...&xsec_source=pc_note 路径 (需要 --token)')
    p.add_argument('--via-user-profile', action='store_true',
                   help='走 /user/profile/{uid}/{nid}?xsec_token=...&xsec_source=pc_user 路径 (推荐,需要 --token + --user-id)')
    p.add_argument('--token', help='xsec_token (配合 --via-search / --via-user-profile 使用)')
    p.add_argument('--user-id', help='user_id (配合 --via-user-profile 使用)')
    p.add_argument('--xsec-source', help='覆盖默认 xsec_source (默认 search: pc_note, user_profile: pc_user)')

    # user-search (用户名 → user_id 解析)
    p = sub.add_parser('user-search', help='用户名 → user_id (搜→note DOM→user_profile 链接)')
    p.add_argument('keyword', help='用户显示名(中文/英文均可)')
    p.add_argument('--out', help='落盘 JSON')
    p.add_argument('--list-candidates', action='store_true',
                   help='只打印所有候选 user_id + classes,不验证不选最佳 (调试用)')

    # user
    p = sub.add_parser('user', help='用户主页')
    p.add_argument('user_id', help='user_id 或 profile URL')
    p.add_argument('--notes', type=int, default=20, help='拿几个作品 (默认 20)')
    p.add_argument('--out', help='落盘 JSON')

    # user-resolve (用户名 → user_id 增强版,逐个验证,Plan B 降级)
    p = sub.add_parser('user-resolve', help='用户名 → user_id 增强版 (逐个验证候选,推荐用于 search 桶 captcha 后)')
    p.add_argument('keyword', help='用户显示名(中文/英文均可)')

    # paths
    sub.add_parser('paths', help='打印路径配置')

    args = parser.parse_args()
    fn = globals().get(f"cmd_{args.cmd.replace('-', '_')}")
    if not fn:
        err_struct('parse_fail', f'未知子命令: {args.cmd}')
        return 1
    return fn(args) or 0


if __name__ == '__main__':
    sys.exit(main())
