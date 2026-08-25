#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""blog-mini-yaw-kit — Blog System API (FastAPI) management skill

Capabilities (from OpenAPI spec, 32 endpoints):
  A. health-check — Check API health
  B. list-articles — List articles (paginated, filterable)
  C. create-article — Create a new article
  D. get-article — Get a single article by ID
  E. update-article — Update an article
  F. delete-article — Delete an article (soft/hard)
  G. restore-article — Restore a soft-deleted article
  H. top-articles — Get top articles by heat
  I. list-labels — List all labels (API path: /api/lables)
  J. create-label — Create a label (API path: /api/lables)
  K. list-users — List all users
  L. create-user — Create a user
  M. create-comment — Create a comment on an article
  N. list-comments — List comments for an article
  O. delete-comment — Delete a comment
  P. list-messages — List all guestbook messages
  Q. create-message — Create a guestbook message
  R. reply-message — Reply to a guestbook message
  S. delete-message — Delete a guestbook message
  T. list-moods — List all moods (说说)
  U. create-mood — Create a mood
  V. delete-mood — Delete a mood
  W. upload-file — Upload a single file
  X. upload-files — Upload multiple files
  Y. list-uploads — List uploaded files
  Z. delete-upload — Delete an uploaded file
  AA. admin-login — Admin login (form-based, sets session cookie)
  AB. admin-logout — Admin logout
  AC. admin-delete-articles — Admin batch delete articles (requires session)

Auth: none (public API; admin endpoints use session cookie via admin-login)
Exit codes: 0=success; 2=param error; 3=missing config (base_url); 4=API failure
"""

import argparse
import json
import os
import sys


# ---------------------------------------------------------------------------
# Credentials (prefix derived from skill name: blog-mini-yaw-kit -> BLOG_MINI_YAW_KIT)
# ---------------------------------------------------------------------------

_CRED_PREFIX = "BLOG_MINI_YAW_KIT"
_AUTH_TYPE = "none"
_API_KEY_HEADER = ""
_API_KEY_LOCATION = ""


def _load_credentials():
    """Load credentials — 4-level priority (same as base_url).

    1. Project knowledge: scan .project-info/ JSON files (config.{PREFIX}_BASE_URL)
    2. Environment variables: {PREFIX}_* prefixed vars
    3. Current context: A2A context injected env vars (included in step 2)
    4. Interactive input: prompt user when all above are missing
    """
    creds = {}
    creds.update(_load_from_project_knowledge())
    for k, v in os.environ.items():
        u = k.upper()
        if u.startswith(_CRED_PREFIX):
            if 'USERNAME' in u or u.endswith('_USER'):
                creds.setdefault('username', v)
            if 'PASSWORD' in u or u.endswith('_PASS'):
                creds.setdefault('password', v)
            if 'TOKEN' in u:
                creds.setdefault('token', v)
            if 'API_KEY' in u:
                creds.setdefault('api_key', v)
            if 'BASE_URL' in u:
                creds.setdefault('base_url', v)
    return creds


def _load_from_project_knowledge():
    """Scan .project-info/ directory recursively for JSON config files.

    Reads config.{PREFIX}_BASE_URL field. base_url matched strictly by prefix.
    """
    import glob
    creds = {}
    for filepath in glob.glob('.project-info/**/*.json', recursive=True):
        try:
            with open(filepath) as f:
                data = json.load(f)
            config = data.get('config', {})
            prefix = _CRED_PREFIX + '_'
            if 'base_url' not in creds:
                for key, val in config.items():
                    if key.upper() == (prefix + 'BASE_URL'):
                        creds.setdefault('base_url', val)
                        break
        except Exception:
            continue
    return creds


def _get_base_url():
    """Get API base URL — 4-level priority."""
    creds = _load_credentials()
    base_url = creds.get('base_url', '').rstrip('/')
    if not base_url:
        print("未检测到 %s_BASE_URL 环境变量，也未在 .project-info/ 找到配置。" % _CRED_PREFIX)
        print("请输入目标系统 API 地址（如 http://<host>:<port>）：")
        base_url = input("> ").strip().rstrip('/')
        if not base_url:
            print("错误：API 地址不能为空", file=sys.stderr)
            sys.exit(3)
        if not (base_url.startswith("http://") or base_url.startswith("https://")):
            print("错误：地址必须以 http:// 或 https:// 开头", file=sys.stderr)
            sys.exit(3)
        print("提示：可通过 export %s_BASE_URL=\"%s\" 永久设置，避免每次输入。" % (_CRED_PREFIX, base_url))
    return base_url


# ---------------------------------------------------------------------------
# API client (no-auth public API; session for admin cookie persistence)
# ---------------------------------------------------------------------------

import requests

_session = requests.Session()


def _build_auth(creds):
    """Build request auth kwargs. No-auth returns empty dict."""
    return {}


def _api_request(method, path, payload=None, params=None, files=None,
                 form_data=None, allow_redirects=True, raw=False):
    """Call the blog system REST API.

    For admin endpoints (admin-login/admin-logout/admin-delete-articles), use
    raw=True to capture status code and cookies without raise_for_status.
    """
    base_url = _get_base_url()
    creds = _load_credentials()
    auth_kwargs = _build_auth(creds)
    url = f"{base_url}{path}"

    try:
        kwargs = dict(auth_kwargs)
        kwargs['timeout'] = 30
        kwargs['allow_redirects'] = allow_redirects

        if method == 'GET':
            resp = _session.get(url, params=params, **kwargs)
        elif method == 'POST':
            if files:
                resp = _session.post(url, files=files, **kwargs)
            elif form_data:
                resp = _session.post(url, data=form_data, **kwargs)
            else:
                resp = _session.post(url, json=payload, **kwargs)
        elif method == 'PUT':
            resp = _session.put(url, json=payload, **kwargs)
        elif method == 'PATCH':
            resp = _session.patch(url, json=payload, **kwargs)
        elif method == 'DELETE':
            resp = _session.delete(url, params=params, **kwargs)
        else:
            print(f"错误：不支持的方法 {method}", file=sys.stderr)
            sys.exit(2)

        if raw:
            result = {"status_code": resp.status_code}
            try:
                result["body"] = resp.json()
            except ValueError:
                result["body"] = resp.text[:500] if resp.text else ""
            if resp.cookies:
                result["cookies_set"] = dict(resp.cookies)
            return result

        resp.raise_for_status()
        if resp.content:
            try:
                return resp.json()
            except ValueError:
                return {"status_code": resp.status_code, "body": resp.text[:500]}
        return {}
    except requests.exceptions.HTTPError as e:
        print(f"错误：API 调用失败 {resp.status_code}: {e}", file=sys.stderr)
        sys.exit(4)
    except requests.exceptions.RequestException as e:
        print(f"错误：网络请求失败: {e}", file=sys.stderr)
        sys.exit(4)
    except ValueError:
        print("错误：API 返回非 JSON 格式（可能返回 HTML 错误页）", file=sys.stderr)
        sys.exit(4)


# ---------------------------------------------------------------------------
# Subcommand implementations
# ---------------------------------------------------------------------------

# --- Health (1) ---

def cmd_health_check(args):
    """AA: Check API health."""
    return _api_request('GET', '/health')


# --- Articles (7) ---

def cmd_list_articles(args):
    """B: List articles (paginated, filterable)."""
    params = {}
    if args.page is not None:
        params['page'] = args.page
    if args.size is not None:
        params['size'] = args.size
    if args.lid is not None:
        params['lid'] = args.lid
    if args.keyword is not None:
        params['keyword'] = args.keyword
    return _api_request('GET', '/api/articles', params=params)


def cmd_create_article(args):
    """C: Create a new article."""
    payload = {'title': args.title, 'content': args.content}
    if args.uid is not None:
        payload['uid'] = args.uid
    if args.lid is not None:
        payload['lid'] = args.lid
    if args.img is not None:
        payload['img'] = args.img
    if args.heat is not None:
        payload['heat'] = args.heat
    return _api_request('POST', '/api/articles', payload=payload)


def cmd_get_article(args):
    """D: Get a single article by ID."""
    return _api_request('GET', f'/api/articles/{args.article_id}')


def cmd_update_article(args):
    """E: Update an article."""
    payload = {}
    if args.title is not None:
        payload['title'] = args.title
    if args.content is not None:
        payload['content'] = args.content
    if args.lid is not None:
        payload['lid'] = args.lid
    if args.img is not None:
        payload['img'] = args.img
    if args.heat is not None:
        payload['heat'] = args.heat
    return _api_request('PUT', f'/api/articles/{args.article_id}', payload=payload)


def cmd_delete_article(args):
    """F: Delete an article (soft/hard)."""
    params = {}
    if args.soft is not None:
        params['soft'] = args.soft
    return _api_request('DELETE', f'/api/articles/{args.article_id}', params=params)


def cmd_restore_article(args):
    """G: Restore a soft-deleted article."""
    return _api_request('POST', f'/api/articles/{args.article_id}/restore')


def cmd_top_articles(args):
    """H: Get top articles by heat."""
    params = {}
    if args.limit is not None:
        params['limit'] = args.limit
    return _api_request('GET', '/api/articles/heat/top', params=params)


# --- Labels (2) — API path uses "lables" (typo), subcommand uses correct spelling ---

def cmd_list_labels(args):
    """I: List all labels (API path: /api/lables)."""
    return _api_request('GET', '/api/lables')


def cmd_create_label(args):
    """J: Create a label (API path: /api/lables)."""
    payload = {'lname': args.lname}
    return _api_request('POST', '/api/lables', payload=payload)


# --- Users (2) ---

def cmd_list_users(args):
    """K: List all users."""
    return _api_request('GET', '/api/users')


def cmd_create_user(args):
    """L: Create a user."""
    payload = {'uname': args.uname}
    if args.phone is not None:
        payload['phone'] = args.phone
    if args.pwd is not None:
        payload['pwd'] = args.pwd
    if args.email is not None:
        payload['email'] = args.email
    if args.img is not None:
        payload['img'] = args.img
    return _api_request('POST', '/api/users', payload=payload)


# --- Comments (3) ---

def cmd_create_comment(args):
    """M: Create a comment on an article."""
    payload = {'uid': args.uid, 'aid': args.aid, 'content': args.content}
    return _api_request('POST', '/api/comments', payload=payload)


def cmd_list_comments(args):
    """N: List comments for an article."""
    return _api_request('GET', f'/api/comments/{args.aid}')


def cmd_delete_comment(args):
    """O: Delete a comment."""
    return _api_request('DELETE', f'/api/comments/{args.comment_id}')


# --- Messages (4) ---

def cmd_list_messages(args):
    """P: List all guestbook messages."""
    return _api_request('GET', '/api/messages')


def cmd_create_message(args):
    """Q: Create a guestbook message."""
    payload = {'uid': args.uid, 'content': args.content}
    return _api_request('POST', '/api/messages', payload=payload)


def cmd_reply_message(args):
    """R: Reply to a guestbook message."""
    payload = {'uid': args.uid, 'mid': args.mid, 'content': args.content}
    return _api_request('POST', '/api/messages/reply', payload=payload)


def cmd_delete_message(args):
    """S: Delete a guestbook message."""
    return _api_request('DELETE', f'/api/messages/{args.message_id}')


# --- Moods (3) ---

def cmd_list_moods(args):
    """T: List all moods (说说)."""
    return _api_request('GET', '/api/moods')


def cmd_create_mood(args):
    """U: Create a mood."""
    payload = {'content': args.content}
    if args.title is not None:
        payload['title'] = args.title
    if args.src is not None:
        payload['src'] = args.src
    return _api_request('POST', '/api/moods', payload=payload)


def cmd_delete_mood(args):
    """V: Delete a mood."""
    return _api_request('DELETE', f'/api/moods/{args.mood_id}')


# --- File Upload (4) ---

def cmd_upload_file(args):
    """W: Upload a single file."""
    with open(args.file, 'rb') as f:
        return _api_request('POST', '/api/upload', files={'file': f})


def cmd_upload_files(args):
    """X: Upload multiple files."""
    files = [open(fp, 'rb') for fp in args.files]
    try:
        return _api_request('POST', '/api/upload/multiple',
                            files=[('files', f) for f in files])
    finally:
        for f in files:
            f.close()


def cmd_list_uploads(args):
    """Y: List uploaded files."""
    return _api_request('GET', '/api/uploads/list')


def cmd_delete_upload(args):
    """Z: Delete an uploaded file."""
    return _api_request('DELETE', f'/api/uploads/{args.filename}')


# --- Admin (3) — requires session cookie via admin-login ---

def cmd_admin_login(args):
    """AA: Admin login (form-based, sets session cookie)."""
    return _api_request('POST', '/admin/login',
                        form_data={'username': args.username, 'password': args.password},
                        allow_redirects=False, raw=True)


def cmd_admin_logout(args):
    """AB: Admin logout."""
    params = {}
    if args.t is not None:
        params['t'] = args.t
    return _api_request('GET', '/admin/logout', params=params, allow_redirects=False, raw=True)


def cmd_admin_delete_articles(args):
    """AC: Admin batch delete articles (requires session)."""
    payload = {'ids': args.ids}
    return _api_request('POST', '/admin/api/delete', payload=payload, raw=True)


# ---------------------------------------------------------------------------
# Capability list
# ---------------------------------------------------------------------------

_CAPABILITIES = [
    {'name': 'health-check', 'description': 'Check API health', 'command': 'health-check'},
    {'name': 'list-articles', 'description': 'List articles (paginated, filterable)', 'command': 'list-articles [--page N] [--size N] [--lid N] [--keyword TEXT]'},
    {'name': 'create-article', 'description': 'Create a new article', 'command': 'create-article --title TEXT --content TEXT [--uid N] [--lid N] [--img URL] [--heat N]'},
    {'name': 'get-article', 'description': 'Get a single article by ID', 'command': 'get-article --article-id N'},
    {'name': 'update-article', 'description': 'Update an article', 'command': 'update-article --article-id N [--title TEXT] [--content TEXT] [--lid N] [--img URL] [--heat N]'},
    {'name': 'delete-article', 'description': 'Delete an article (soft/hard)', 'command': 'delete-article --article-id N [--soft true|false]'},
    {'name': 'restore-article', 'description': 'Restore a soft-deleted article', 'command': 'restore-article --article-id N'},
    {'name': 'top-articles', 'description': 'Get top articles by heat', 'command': 'top-articles [--limit N]'},
    {'name': 'list-labels', 'description': 'List all labels (API path: /api/lables)', 'command': 'list-labels'},
    {'name': 'create-label', 'description': 'Create a label (API path: /api/lables)', 'command': 'create-label --lname TEXT'},
    {'name': 'list-users', 'description': 'List all users', 'command': 'list-users'},
    {'name': 'create-user', 'description': 'Create a user', 'command': 'create-user --uname TEXT [--phone TEXT] [--pwd TEXT] [--email TEXT] [--img URL]'},
    {'name': 'create-comment', 'description': 'Create a comment on an article', 'command': 'create-comment --uid N --aid N --content TEXT'},
    {'name': 'list-comments', 'description': 'List comments for an article', 'command': 'list-comments --aid N'},
    {'name': 'delete-comment', 'description': 'Delete a comment', 'command': 'delete-comment --comment-id N'},
    {'name': 'list-messages', 'description': 'List all guestbook messages', 'command': 'list-messages'},
    {'name': 'create-message', 'description': 'Create a guestbook message', 'command': 'create-message --uid N --content TEXT'},
    {'name': 'reply-message', 'description': 'Reply to a guestbook message', 'command': 'reply-message --uid N --mid N --content TEXT'},
    {'name': 'delete-message', 'description': 'Delete a guestbook message', 'command': 'delete-message --message-id N'},
    {'name': 'list-moods', 'description': 'List all moods', 'command': 'list-moods'},
    {'name': 'create-mood', 'description': 'Create a mood', 'command': 'create-mood --content TEXT [--title TEXT] [--src URL]'},
    {'name': 'delete-mood', 'description': 'Delete a mood', 'command': 'delete-mood --mood-id N'},
    {'name': 'upload-file', 'description': 'Upload a single file', 'command': 'upload-file --file PATH'},
    {'name': 'upload-files', 'description': 'Upload multiple files', 'command': 'upload-files --files PATH [PATH ...]'},
    {'name': 'list-uploads', 'description': 'List uploaded files', 'command': 'list-uploads'},
    {'name': 'delete-upload', 'description': 'Delete an uploaded file', 'command': 'delete-upload --filename TEXT'},
    {'name': 'admin-login', 'description': 'Admin login (form-based, sets session cookie)', 'command': 'admin-login --username TEXT --password TEXT'},
    {'name': 'admin-logout', 'description': 'Admin logout', 'command': 'admin-logout [--t TEXT]'},
    {'name': 'admin-delete-articles', 'description': 'Admin batch delete articles (requires session)', 'command': 'admin-delete-articles --ids N [N ...]'},
]


def cmd_capability_list(args):
    """List all capabilities of this skill."""
    return {
        'capability': 'capability-list',
        'skill': 'blog-mini-yaw-kit',
        'version': '0.1.0',
        'endpoint_count': 32,
        'subcommand_count': len(_CAPABILITIES),
        'capabilities': _CAPABILITIES + [
            {'name': 'capability-list', 'description': 'List all capabilities of this skill',
             'command': 'capability-list'},
        ],
    }


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_md(payload):
    """Render JSON output as Markdown table (optional)."""
    cap = payload.get('capability', '')
    if cap == 'capability-list':
        lines = [f"## Capabilities ({payload.get('skill', '')})", "",
                 "| Capability | Description | Command |", "|---|---|---|"]
        for c in payload.get('capabilities', []):
            lines.append(f"| {c['name']} | {c['description']} | `{c['command']}` |")
        return "\n".join(lines)
    if isinstance(payload, dict) and 'data' in payload and isinstance(payload['data'], list):
        items = payload['data']
        if not items:
            return json.dumps(payload, ensure_ascii=False, indent=2)
        keys = list(items[0].keys())
        lines = ["| " + " | ".join(keys) + " |",
                 "|" + "|".join(["---"] * len(keys)) + "|"]
        for item in items[:50]:
            lines.append("| " + " | ".join(str(item.get(k, '')) for k in keys) + " |")
        return "\n".join(lines)
    return json.dumps(payload, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='blog-mini-yaw-kit',
        description='Blog System API (FastAPI) management skill — 32 endpoints')

    def add_common_args(p):
        p.add_argument('--format', choices=['json', 'md'], default='json',
                       help='输出格式，默认 json')

    sub = parser.add_subparsers(dest='command', help='能力命令')

    # --- Health ---
    p = sub.add_parser('health-check', help='Check API health')
    add_common_args(p)

    # --- Articles ---
    p = sub.add_parser('list-articles', help='List articles (paginated, filterable)')
    p.add_argument('--page', type=int, default=None, help='页码（默认 1）')
    p.add_argument('--size', type=int, default=None, help='每页条数（默认 10）')
    p.add_argument('--lid', type=int, default=None, help='标签 ID 筛选')
    p.add_argument('--keyword', type=str, default=None, help='关键词搜索')
    add_common_args(p)

    p = sub.add_parser('create-article', help='Create a new article')
    p.add_argument('--title', required=True, help='文章标题（必填）')
    p.add_argument('--content', required=True, help='文章内容（必填）')
    p.add_argument('--uid', type=int, default=None, help='作者用户 ID')
    p.add_argument('--lid', type=int, default=None, help='标签 ID')
    p.add_argument('--img', type=str, default=None, help='封面图 URL')
    p.add_argument('--heat', type=int, default=None, help='热度值')
    add_common_args(p)

    p = sub.add_parser('get-article', help='Get a single article by ID')
    p.add_argument('--article-id', type=int, required=True, help='文章 ID（必填）')
    add_common_args(p)

    p = sub.add_parser('update-article', help='Update an article')
    p.add_argument('--article-id', type=int, required=True, help='文章 ID（必填）')
    p.add_argument('--title', type=str, default=None, help='文章标题')
    p.add_argument('--content', type=str, default=None, help='文章内容')
    p.add_argument('--lid', type=int, default=None, help='标签 ID')
    p.add_argument('--img', type=str, default=None, help='封面图 URL')
    p.add_argument('--heat', type=int, default=None, help='热度值')
    add_common_args(p)

    p = sub.add_parser('delete-article', help='Delete an article (soft/hard)')
    p.add_argument('--article-id', type=int, required=True, help='文章 ID（必填）')
    p.add_argument('--soft', type=str, default=None, choices=['true', 'false'],
                   help='软删除（true）或硬删除（false）')
    add_common_args(p)

    p = sub.add_parser('restore-article', help='Restore a soft-deleted article')
    p.add_argument('--article-id', type=int, required=True, help='文章 ID（必填）')
    add_common_args(p)

    p = sub.add_parser('top-articles', help='Get top articles by heat')
    p.add_argument('--limit', type=int, default=None, help='返回条数')
    add_common_args(p)

    # --- Labels ---
    p = sub.add_parser('list-labels', help='List all labels (API path: /api/lables)')
    add_common_args(p)

    p = sub.add_parser('create-label', help='Create a label (API path: /api/lables)')
    p.add_argument('--lname', required=True, help='标签名称（必填）')
    add_common_args(p)

    # --- Users ---
    p = sub.add_parser('list-users', help='List all users')
    add_common_args(p)

    p = sub.add_parser('create-user', help='Create a user')
    p.add_argument('--uname', required=True, help='用户名（必填）')
    p.add_argument('--phone', type=str, default=None, help='手机号')
    p.add_argument('--pwd', type=str, default=None, help='密码')
    p.add_argument('--email', type=str, default=None, help='邮箱')
    p.add_argument('--img', type=str, default=None, help='头像 URL')
    add_common_args(p)

    # --- Comments ---
    p = sub.add_parser('create-comment', help='Create a comment on an article')
    p.add_argument('--uid', type=int, required=True, help='用户 ID（必填）')
    p.add_argument('--aid', type=int, required=True, help='文章 ID（必填）')
    p.add_argument('--content', required=True, help='评论内容（必填）')
    add_common_args(p)

    p = sub.add_parser('list-comments', help='List comments for an article')
    p.add_argument('--aid', type=int, required=True, help='文章 ID（必填）')
    add_common_args(p)

    p = sub.add_parser('delete-comment', help='Delete a comment')
    p.add_argument('--comment-id', type=int, required=True, help='评论 ID（必填）')
    add_common_args(p)

    # --- Messages ---
    p = sub.add_parser('list-messages', help='List all guestbook messages')
    add_common_args(p)

    p = sub.add_parser('create-message', help='Create a guestbook message')
    p.add_argument('--uid', type=int, required=True, help='用户 ID（必填）')
    p.add_argument('--content', required=True, help='留言内容（必填）')
    add_common_args(p)

    p = sub.add_parser('reply-message', help='Reply to a guestbook message')
    p.add_argument('--uid', type=int, required=True, help='用户 ID（必填）')
    p.add_argument('--mid', type=int, required=True, help='被回复留言 ID（必填）')
    p.add_argument('--content', required=True, help='回复内容（必填）')
    add_common_args(p)

    p = sub.add_parser('delete-message', help='Delete a guestbook message')
    p.add_argument('--message-id', type=int, required=True, help='留言 ID（必填）')
    add_common_args(p)

    # --- Moods ---
    p = sub.add_parser('list-moods', help='List all moods')
    add_common_args(p)

    p = sub.add_parser('create-mood', help='Create a mood')
    p.add_argument('--title', type=str, default=None, help='标题')
    p.add_argument('--content', required=True, help='内容（必填）')
    p.add_argument('--src', type=str, default=None, help='配图 URL')
    add_common_args(p)

    p = sub.add_parser('delete-mood', help='Delete a mood')
    p.add_argument('--mood-id', type=int, required=True, help='说说 ID（必填）')
    add_common_args(p)

    # --- File Upload ---
    p = sub.add_parser('upload-file', help='Upload a single file')
    p.add_argument('--file', required=True, help='文件路径（必填）')
    add_common_args(p)

    p = sub.add_parser('upload-files', help='Upload multiple files')
    p.add_argument('--files', required=True, nargs='+', help='文件路径列表（必填，至少 1 个）')
    add_common_args(p)

    p = sub.add_parser('list-uploads', help='List uploaded files')
    add_common_args(p)

    p = sub.add_parser('delete-upload', help='Delete an uploaded file')
    p.add_argument('--filename', required=True, help='文件名（必填）')
    add_common_args(p)

    # --- Admin ---
    p = sub.add_parser('admin-login', help='Admin login (form-based, sets session cookie)')
    p.add_argument('--username', required=True, help='管理员用户名（必填）')
    p.add_argument('--password', required=True, help='管理员密码（必填）')
    add_common_args(p)

    p = sub.add_parser('admin-logout', help='Admin logout')
    p.add_argument('--t', type=str, default=None, help='可选 token 参数')
    add_common_args(p)

    p = sub.add_parser('admin-delete-articles', help='Admin batch delete articles (requires session)')
    p.add_argument('--ids', required=True, nargs='+', type=int, help='文章 ID 列表（必填）')
    add_common_args(p)

    # --- capability-list ---
    p = sub.add_parser('capability-list', help='List all capabilities of this skill')
    add_common_args(p)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(2)

    dispatch = {
        'health-check': cmd_health_check,
        'list-articles': cmd_list_articles,
        'create-article': cmd_create_article,
        'get-article': cmd_get_article,
        'update-article': cmd_update_article,
        'delete-article': cmd_delete_article,
        'restore-article': cmd_restore_article,
        'top-articles': cmd_top_articles,
        'list-labels': cmd_list_labels,
        'create-label': cmd_create_label,
        'list-users': cmd_list_users,
        'create-user': cmd_create_user,
        'create-comment': cmd_create_comment,
        'list-comments': cmd_list_comments,
        'delete-comment': cmd_delete_comment,
        'list-messages': cmd_list_messages,
        'create-message': cmd_create_message,
        'reply-message': cmd_reply_message,
        'delete-message': cmd_delete_message,
        'list-moods': cmd_list_moods,
        'create-mood': cmd_create_mood,
        'delete-mood': cmd_delete_mood,
        'upload-file': cmd_upload_file,
        'upload-files': cmd_upload_files,
        'list-uploads': cmd_list_uploads,
        'delete-upload': cmd_delete_upload,
        'admin-login': cmd_admin_login,
        'admin-logout': cmd_admin_logout,
        'admin-delete-articles': cmd_admin_delete_articles,
        'capability-list': cmd_capability_list,
    }

    handler = dispatch.get(args.command)
    if handler is None:
        print(f"错误：未知命令 {args.command}", file=sys.stderr)
        sys.exit(2)

    try:
        payload = handler(args)
        if args.format == 'md':
            print(render_md(payload))
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
    except SystemExit:
        raise
    except Exception as exc:
        print(f"错误：{exc}", file=sys.stderr)
        sys.exit(4)


if __name__ == '__main__':
    main()
