#!/usr/bin/env python3
"""Yuque Document Manager - CLI tool for managing Yuque knowledge base documents.

Usage:
    python yuque_cli.py <command> [options]

Commands:
    list     List documents in the knowledge base
    get      Get document detail by ID or slug
    create   Create a new document (auto-appends to TOC)
    update   Update an existing document
    delete   Delete a document (requires --confirm)
    toc      Show knowledge base table of contents
    sync     Sync local markdown files <-> Yuque (only updates changed docs)
    pull     Pull remote doc(s) down to local files
    status   Show sync diff between local files and Yuque (read-only)

Global options:
    --json      Emit machine-readable JSON output
    --dry-run   Preview the action without executing it (create/update/delete)

Environment:
    Reads YUQUE_TOKEN, YUQUE_REPO, and optional YUQUE_BASE_URL from a .env
    file found by searching upward from the current working directory.

Sync state:
    `sync`/`pull`/`status` maintain `.yuque-sync.json` in the project root,
    tracking per-doc local content hash and remote latest_version_id so only
    truly changed documents are pushed. Auto-added to .gitignore.

Exit codes:
    0  success
    1  error (auth, network, validation, etc.)
    2  user confirmation required (e.g. local file deletion detected during sync)
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import find_dotenv, load_dotenv


def load_config():
    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path:
        load_dotenv(dotenv_path)
    else:
        print("Warning: No .env file found. Using environment variables only.", file=sys.stderr)

    token = os.getenv("YUQUE_TOKEN")
    repo = os.getenv("YUQUE_REPO")
    base_url = os.getenv("YUQUE_BASE_URL", "https://www.yuque.com").rstrip("/")

    if not token:
        print("Error: YUQUE_TOKEN not set. Create a .env file with YUQUE_TOKEN=<your_token>.", file=sys.stderr)
        sys.exit(1)
    if not repo:
        print("Error: YUQUE_REPO not set. Create a .env file with YUQUE_REPO=group_login/book_slug.", file=sys.stderr)
        sys.exit(1)
    if "/" not in repo:
        print(f"Error: YUQUE_REPO must be 'group_login/book_slug', got '{repo}'.", file=sys.stderr)
        sys.exit(1)

    group_login, book_slug = repo.split("/", 1)
    return {"token": token, "group_login": group_login, "book_slug": book_slug, "base_url": base_url}


class YuqueClient:
    def __init__(self, token, group_login, book_slug, base_url="https://www.yuque.com"):
        self.base_url = base_url
        self.group_login = group_login
        self.book_slug = book_slug
        self.session = requests.Session()
        self.session.headers.update({
            "X-Auth-Token": token,
            "Content-Type": "application/json",
            "User-Agent": "yuque-cli/1.0",
        })

    @property
    def _repo_path(self):
        return f"/api/v2/repos/{self.group_login}/{self.book_slug}"

    def _request(self, method, path, **kwargs):
        url = self.base_url + path
        resp = self.session.request(method, url, **kwargs)
        if resp.status_code == 429:
            print("Rate limited. Waiting 2 seconds before retry...", file=sys.stderr)
            time.sleep(2)
            resp = self.session.request(method, url, **kwargs)
        if not resp.ok:
            error_messages = {
                401: "Authentication failed. Check YUQUE_TOKEN.",
                403: "Permission denied. Token may lack access.",
                404: "Not found. Check YUQUE_REPO and doc ID/slug.",
                429: "Rate limited. Wait and retry.",
                500: "Yuque server error. Try later.",
            }
            msg = error_messages.get(resp.status_code, "Request failed")
            print(f"Error [{resp.status_code}]: {msg}", file=sys.stderr)
            try:
                print(f"Detail: {json.dumps(resp.json(), ensure_ascii=False)}", file=sys.stderr)
            except Exception:
                print(f"Response: {resp.text[:500]}", file=sys.stderr)
            print(f"Request: {method} {path}", file=sys.stderr)
            sys.exit(1)
        return resp.json()

    def list_docs(self, offset=0, limit=100, optional_properties=None):
        params = {"offset": offset, "limit": limit}
        if optional_properties:
            params["optional_properties"] = optional_properties
        return self._request("GET", f"{self._repo_path}/docs", params=params)

    def list_all_docs(self, optional_properties="latest_version_id"):
        """Page through every doc in the repo. Returns the merged data list."""
        out = []
        offset = 0
        page_size = 100
        while True:
            resp = self.list_docs(offset=offset, limit=page_size, optional_properties=optional_properties)
            batch = resp.get("data", []) or []
            out.extend(batch)
            if len(batch) < page_size:
                break
            offset += page_size
        return out

    def get_doc(self, id_or_slug):
        return self._request("GET", f"{self._repo_path}/docs/{id_or_slug}")

    def create_doc(self, body, title=None, slug=None, format="markdown", public=None):
        data = {"body": body, "format": format}
        if title is not None:
            data["title"] = title
        if slug is not None:
            data["slug"] = slug
        if public is not None:
            data["public"] = public
        return self._request("POST", f"{self._repo_path}/docs", json=data)

    def update_doc(self, id_or_slug, **fields):
        data = {k: v for k, v in fields.items() if v is not None}
        if not data:
            print("Error: No fields to update.", file=sys.stderr)
            sys.exit(1)
        return self._request("PUT", f"{self._repo_path}/docs/{id_or_slug}", json=data)

    def delete_doc(self, id_or_slug):
        return self._request("DELETE", f"{self._repo_path}/docs/{id_or_slug}")

    def get_toc(self):
        return self._request("GET", f"{self._repo_path}/toc")

    def update_toc(self, action, action_mode, **kwargs):
        data = {"action": action, "action_mode": action_mode}
        data.update({k: v for k, v in kwargs.items() if v is not None})
        return self._request("PUT", f"{self._repo_path}/toc", json=data)

    def append_doc_to_toc(self, doc_id):
        return self.update_toc(action="appendNode", action_mode="child", type="DOC", doc_ids=[doc_id])


# --- Output ---

def output(data, use_json=False):
    """Write structured data to stdout. JSON mode for machine consumption, text mode for humans."""
    if use_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        if isinstance(data, str):
            print(data)
        elif isinstance(data, dict):
            for k, v in data.items():
                print(f"{k}: {v}")
        elif isinstance(data, list):
            for item in data:
                print(item)


def read_body(args):
    if getattr(args, "body_file", None):
        p = Path(args.body_file)
        if not p.is_file():
            print(f"Error: File not found: {args.body_file}", file=sys.stderr)
            sys.exit(1)
        raw = p.read_text(encoding="utf-8")
        # Strip YAML frontmatter so it does not leak into the Yuque body
        _, body = parse_frontmatter(raw)
        return body
    return getattr(args, "body", None)


# --- Setup ---

def parse_yuque_url(url):
    """Parse a Yuque knowledge base URL into base_url, group_login, book_slug.

    Accepts formats:
        https://www.yuque.com/group/book
        https://custom.yuque.com/group/book
        https://custom.yuque.com/group/book/anything-after
    """
    url = url.strip().rstrip("/")
    parsed = urlparse(url)

    if not parsed.scheme:
        parsed = urlparse("https://" + url)

    if not re.search(r'yuque\.com$', parsed.hostname or ""):
        return None, "URL must be a yuque.com domain (e.g. https://xxx.yuque.com/group/book)."

    base_url = f"{parsed.scheme}://{parsed.hostname}"
    parts = [p for p in parsed.path.strip("/").split("/") if p]

    if len(parts) < 2:
        return None, "URL must contain at least group_login and book_slug (e.g. https://xxx.yuque.com/group/book)."

    group_login = parts[0]
    book_slug = parts[1]
    return {"base_url": base_url, "group_login": group_login, "book_slug": book_slug}, None


def verify_connection(token, base_url, group_login, book_slug):
    """Test the token and repo by calling the list docs API. Returns (success, message)."""
    url = f"{base_url}/api/v2/repos/{group_login}/{book_slug}/docs?limit=1"
    try:
        resp = requests.get(url, headers={"X-Auth-Token": token, "User-Agent": "yuque-cli/1.0"}, timeout=15)
    except requests.RequestException as e:
        return False, f"Connection failed: {e}"

    if resp.status_code == 401:
        return False, "Token is invalid or expired. Please check and retry."
    if resp.status_code == 404:
        return False, f"Repository '{group_login}/{book_slug}' not found. Check the URL."
    if not resp.ok:
        return False, f"Unexpected error [{resp.status_code}]: {resp.text[:200]}"

    total = resp.json().get("meta", {}).get("total", 0)
    return True, f"Connected. Repository has {total} document(s)."


def ensure_gitignore(project_root):
    """Check that .env is listed in .gitignore. Returns (is_safe, message)."""
    gitignore_path = project_root / ".gitignore"
    if not gitignore_path.is_file():
        return False, ".gitignore does not exist. Create one and add '.env' to it."

    content = gitignore_path.read_text(encoding="utf-8")
    # Check for .env entry (whole line, possibly with comment)
    for line in content.splitlines():
        stripped = line.split("#")[0].strip()
        if stripped == ".env" or stripped == ".env*":
            return True, ".gitignore already contains '.env'."

    return False, ".gitignore exists but does not contain '.env'. Add it to prevent accidental commits."


def cmd_setup(args, _client=None):
    """Set up .env by parsing a Yuque URL, validating the token, and writing the config."""
    # 1. Parse URL
    parsed, err = parse_yuque_url(args.url)
    if err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    base_url = parsed["base_url"]
    group_login = parsed["group_login"]
    book_slug = parsed["book_slug"]
    repo = f"{group_login}/{book_slug}"

    print(f"Parsed URL:", file=sys.stderr)
    print(f"  Base URL:    {base_url}", file=sys.stderr)
    print(f"  Group Login: {group_login}", file=sys.stderr)
    print(f"  Book Slug:   {book_slug}", file=sys.stderr)

    # 2. Verify connection
    print("Verifying connection...", file=sys.stderr)
    ok, msg = verify_connection(args.token, base_url, group_login, book_slug)
    if not ok:
        print(f"Error: {msg}", file=sys.stderr)
        sys.exit(1)
    print(f"OK: {msg}", file=sys.stderr)

    # 3. Determine .env location
    env_path = Path(args.env_path) if args.env_path else Path.cwd() / ".env"
    project_root = env_path.parent

    # 4. Write .env
    if env_path.is_file() and not args.force and not args.dry_run:
        print(f"Error: {env_path} already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    env_content = f"YUQUE_TOKEN={args.token}\nYUQUE_REPO={repo}\nYUQUE_BASE_URL={base_url}\n"

    if args.dry_run:
        result = {"action": "setup", "dry_run": True, "env_path": str(env_path),
                  "base_url": base_url, "repo": repo, "gitignore_check": "skipped"}
        output(result, use_json=True)
        print("Dry run: no files written.", file=sys.stderr)
        return

    env_path.write_text(env_content, encoding="utf-8")
    print(f"Written: {env_path}", file=sys.stderr)

    # 5. Check .gitignore
    safe, gi_msg = ensure_gitignore(project_root)
    if safe:
        print(f"Security: {gi_msg}", file=sys.stderr)
    else:
        print(f"WARNING: {gi_msg}", file=sys.stderr)
        print("Your token could be leaked if .env is committed to git!", file=sys.stderr)

    # 6. Structured output
    result = {"status": "configured", "env_path": str(env_path),
              "base_url": base_url, "repo": repo, "gitignore_safe": safe}
    if args.json:
        output(result, use_json=True)
    else:
        print(f"\nSetup complete. Run 'python {sys.argv[0]} list' to test.")


# --- Commands ---

def cmd_list(args, client):
    result = client.list_docs(offset=args.offset, limit=args.limit)
    if args.json:
        output(result, use_json=True)
        return
    total = result.get("meta", {}).get("total", "?")
    docs = result.get("data", [])
    print(f"Total: {total} documents\n")
    print(f"{'ID':<12} {'Title':<40} {'Slug':<30} {'Updated'}")
    print("-" * 95)
    for doc in docs:
        updated = doc.get("updated_at", "")[:10]
        print(f"{doc.get('id', '?'):<12} {doc.get('title', ''):<40} {doc.get('slug', ''):<30} {updated}")


def cmd_get(args, client):
    result = client.get_doc(args.id_or_slug)
    if args.json:
        output(result, use_json=True)
        return
    d = result.get("data", result)
    print(f"ID:      {d.get('id')}")
    print(f"Title:   {d.get('title')}")
    print(f"Slug:    {d.get('slug')}")
    print(f"Format:  {d.get('format')}")
    print(f"Public:  {d.get('public')}")
    print(f"Words:   {d.get('word_count', 'N/A')}")
    print(f"Updated: {d.get('updated_at', 'N/A')}")
    print("---")
    print(d.get("body", ""))


def cmd_create(args, client):
    body = read_body(args)
    if not body:
        print("Error: --body or --body-file is required.", file=sys.stderr)
        sys.exit(1)

    payload = {"body": body, "format": args.format}
    if args.title:
        payload["title"] = args.title
    if args.slug:
        payload["slug"] = args.slug
    if args.public is not None:
        payload["public"] = args.public

    if args.dry_run:
        preview = {"action": "create", "dry_run": True, "payload": payload, "auto_toc": not args.no_toc}
        output(preview, use_json=True)
        print("Dry run: no changes made.", file=sys.stderr)
        return

    result = client.create_doc(**payload)
    doc = result.get("data", {})
    doc_id = doc.get("id")

    toc_added = False
    if not args.no_toc and doc_id:
        client.append_doc_to_toc(doc_id)
        toc_added = True

    if args.json:
        output({"status": "created", "doc_id": doc_id, "title": doc.get("title"),
                "slug": doc.get("slug"), "toc_added": toc_added}, use_json=True)
    else:
        print(f"Created doc: id={doc_id}, title={doc.get('title')}, slug={doc.get('slug')}")
        if toc_added:
            print("Added to TOC.")


def cmd_update(args, client):
    body = read_body(args)
    fields = {"title": args.title, "body": body, "slug": args.slug,
              "format": args.format, "public": args.public}
    fields = {k: v for k, v in fields.items() if v is not None}

    if not fields:
        print("Error: No fields to update. Provide at least one of --title, --body, --body-file, --slug, --format, --public.", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        preview = {"action": "update", "dry_run": True, "target": args.id_or_slug, "fields": fields}
        output(preview, use_json=True)
        print("Dry run: no changes made.", file=sys.stderr)
        return

    result = client.update_doc(args.id_or_slug, **fields)
    doc = result.get("data", {})
    if args.json:
        output({"status": "updated", "doc_id": doc.get("id"), "title": doc.get("title")}, use_json=True)
    else:
        print(f"Updated doc: id={doc.get('id')}, title={doc.get('title')}")


def cmd_delete(args, client):
    if args.dry_run:
        preview = {"action": "delete", "dry_run": True, "target": args.id_or_slug}
        output(preview, use_json=True)
        print("Dry run: no changes made.", file=sys.stderr)
        return

    doc_info = client.get_doc(args.id_or_slug).get("data", {})
    print(f"Deleting: id={doc_info.get('id')}, title={doc_info.get('title')}, slug={doc_info.get('slug')}", file=sys.stderr)

    result = client.delete_doc(args.id_or_slug)
    doc = result.get("data", {})
    if args.json:
        output({"status": "deleted", "doc_id": doc.get("id"), "title": doc.get("title")}, use_json=True)
    else:
        print(f"Deleted doc: id={doc.get('id')}, title={doc.get('title')}")


def cmd_toc(args, client):
    result = client.get_toc()
    items = result.get("data", [])
    if args.json:
        output(result, use_json=True)
        return
    if not items:
        print("TOC is empty.")
        return
    for item in items:
        depth = item.get("depth", 0)
        indent = "  " * depth
        title = item.get("title", "untitled")
        node_type = item.get("type", "")
        doc_id = item.get("doc_id")
        uuid = item.get("uuid", "")
        suffix = f" [doc_id={doc_id}]" if doc_id else ""
        print(f"{indent}- {title} ({node_type}){suffix}  uuid={uuid}")


# --- Sync: state, layout, helpers ---

STATE_FILENAME = ".yuque-sync.json"
STATE_VERSION = 1
VALID_LAYOUTS = ("flat", "nested", "frontmatter")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def project_root_for_state():
    """The state file lives next to .env. Fall back to cwd if no .env found."""
    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path:
        return Path(dotenv_path).parent
    return Path.cwd()


def state_path(root=None):
    return Path(root or project_root_for_state()) / STATE_FILENAME


def load_state(root=None):
    p = state_path(root)
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Error: {STATE_FILENAME} is corrupt ({e}). Fix or delete it to re-init.", file=sys.stderr)
        sys.exit(1)


def save_state(state, root=None):
    p = state_path(root)
    state["synced_at"] = now_iso()
    p.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ensure_state_in_gitignore(p.parent)


def ensure_state_in_gitignore(project_root):
    """Append .yuque-sync.json to .gitignore if missing. Best-effort, never fatal."""
    gi = Path(project_root) / ".gitignore"
    line_to_add = STATE_FILENAME
    try:
        if not gi.is_file():
            gi.write_text(line_to_add + "\n", encoding="utf-8")
            return
        content = gi.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.split("#", 1)[0].strip() == line_to_add:
                return
        if content and not content.endswith("\n"):
            content += "\n"
        content += line_to_add + "\n"
        gi.write_text(content, encoding="utf-8")
    except OSError as e:
        print(f"Warning: could not update .gitignore for {line_to_add}: {e}", file=sys.stderr)


def normalize_body(body):
    """Normalize markdown body for stable hashing & diff: unify line endings, strip
    trailing whitespace per line, ensure exactly one trailing newline."""
    if body is None:
        return ""
    text = body.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).rstrip("\n") + "\n"


def sha256_body(body):
    return hashlib.sha256(normalize_body(body).encode("utf-8")).hexdigest()


def parse_frontmatter(text):
    """Parse minimal `--- key: value ---` block. Returns (dict, body_without_frontmatter)."""
    if text is None:
        return {}, ""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        fm[k.strip()] = v
    return fm, text[m.end():]


def extract_title(text, file_stem=None, slug=None, force_filename=False):
    """Extract document title. Returns (title, source).

    Priority: frontmatter `title` → first H1 → file_stem → slug.
    `source` is one of: 'frontmatter', 'h1', 'filename', 'slug'.
    When force_filename is True, skip frontmatter/H1 and use file_stem directly.
    """
    fm, content = parse_frontmatter(text)
    if not force_filename and fm.get("title"):
        return fm["title"], "frontmatter"
    if not force_filename:
        for line in content.split("\n"):
            s = line.strip()
            if s.startswith("# "):
                return s[2:].strip(), "h1"
            if s:
                break
    if file_stem:
        return file_stem, "filename"
    return (slug or ""), "slug"


LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def rewrite_links(body, slug_map):
    """Convert local .md file links to Yuque slug links.

    slug_map maps relative paths and basenames to slugs, e.g.:
      {"创建起草任务.md": "create-draft-task"}
    Returns (new_body, unresolved) where unresolved is a list of link
    targets that could not be mapped (kept as-is in the body).
    """
    unresolved = []

    def replacer(match):
        text = match.group(1)
        raw = match.group(2).strip()
        # Split URL and optional title: `url "title"`
        if " " in raw:
            url, _, title_part = raw.partition(" ")
        else:
            url = raw
            title_part = None
        # Skip external URLs, anchors, mailto, and non-md links
        if url.startswith(("http://", "https://", "//", "#", "mailto:")) or not url.endswith(".md"):
            return match.group(0)
        # Normalize: strip leading ./
        norm = url[2:] if url.startswith("./") else url
        # Try exact match, then basename match
        slug = slug_map.get(norm)
        if slug is None:
            basename = norm.split("/")[-1]
            slug = slug_map.get(basename)
        if slug is not None:
            if title_part:
                return f"[{text}]({slug} {title_part})"
            return f"[{text}]({slug})"
        unresolved.append(url)
        return match.group(0)

    new_body = LINK_RE.sub(replacer, body)
    return new_body, unresolved


def reverse_links(body, reverse_map):
    """Convert slug links back to local filename links (for pull).

    reverse_map maps slug -> local_path (e.g. "create-draft-task" -> "创建起草任务.md").
    """
    def replacer(match):
        text = match.group(1)
        raw = match.group(2).strip()
        if " " in raw:
            url, _, title_part = raw.partition(" ")
        else:
            url = raw
            title_part = None
        if url.startswith(("http://", "https://", "//", "#", "mailto:")):
            return match.group(0)
        # The slug is the last path segment of the URL
        slug_candidate = url.rstrip("/").split("/")[-1]
        local_path = reverse_map.get(slug_candidate) or reverse_map.get(url)
        if local_path:
            if title_part:
                return f"[{text}]({local_path} {title_part})"
            return f"[{text}]({local_path})"
        return match.group(0)

    return LINK_RE.sub(replacer, body)


def fix_bold_format(body):
    """Insert a space after `**label：**` when directly followed by a non-space char.

    Yuque's Markdown renderer does not treat `**` as a bold-close marker when it
    is immediately followed by a non-space character. This rewrites
    `**标签：**值` → `**标签：** 值` so the bold renders correctly.
    Already-correct `**标签：** 值` (with space) is left untouched.
    """
    return re.sub(r'\*\*([^*]+[：:])\*\*([^\s*])', r'**\1** \2', body)


def scan_md_files(root):
    """Return sorted list of .md Paths under root, skipping hidden dirs."""
    root = Path(root)
    out = []
    if not root.is_dir():
        return out
    for p in root.rglob("*.md"):
        rel = p.relative_to(root)
        if any(part.startswith(".") for part in rel.parts):
            continue
        out.append(p)
    return sorted(out)


def detect_layout(root):
    """Probe root and pick a layout. Returns (layout_or_None, message).
    layout in: 'empty', 'flat', 'nested', 'frontmatter'. None means ambiguous."""
    files = scan_md_files(root)
    if not files:
        return "empty", "No .md files found"

    fm_with_slug = 0
    top_level = 0
    nested = 0
    for f in files:
        rel = f.relative_to(root)
        if len(rel.parts) == 1:
            top_level += 1
        else:
            nested += 1
        try:
            head = f.read_text(encoding="utf-8")[:2048]
        except OSError:
            continue
        fm, _ = parse_frontmatter(head)
        if fm.get("slug"):
            fm_with_slug += 1

    total = len(files)
    if fm_with_slug == total:
        return "frontmatter", f"All {total} file(s) have `slug:` frontmatter"
    if 0 < fm_with_slug < total:
        return None, (
            f"{fm_with_slug}/{total} file(s) have `slug:` frontmatter — "
            f"either give every file a slug, or remove all slug frontmatter and use "
            f"file-stem as slug. Re-run with --layout to override."
        )
    if nested == 0:
        return "flat", f"All {top_level} file(s) at top level (file stem = slug)"
    if top_level == 0:
        return "nested", f"All {nested} file(s) in subdirectories (file stem = slug)"
    return None, (
        f"Mixed: {top_level} top-level + {nested} nested .md file(s). "
        f"Re-run with --layout flat or --layout nested to choose."
    )


def slug_for_file(path, root, layout):
    """Compute the slug a local file maps to. Raises ValueError on misconfig."""
    rel = path.relative_to(root)
    if layout == "frontmatter":
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            raise ValueError(f"Cannot read {rel}: {e}")
        fm, _ = parse_frontmatter(text)
        slug = fm.get("slug")
        if not slug:
            raise ValueError(f"{rel}: missing `slug:` frontmatter (layout=frontmatter)")
        return slug
    return path.stem


def file_path_for_slug(slug, root, layout, hint_subdir=None):
    """Where should a pulled doc be written locally?"""
    root = Path(root)
    if layout == "nested" and hint_subdir:
        return root / hint_subdir / f"{slug}.md"
    return root / f"{slug}.md"


def init_state(root, layout=None):
    """Build a fresh state dict by detecting layout. Exits on ambiguity."""
    root = Path(root).resolve()
    if not root.is_dir():
        print(f"Error: root '{root}' is not a directory.", file=sys.stderr)
        sys.exit(1)
    if layout is None:
        detected, msg = detect_layout(root)
        if detected is None:
            print(f"Error: cannot detect layout. {msg}", file=sys.stderr)
            sys.exit(1)
        layout = detected
        print(f"Detected layout: {layout} ({msg})", file=sys.stderr)
    elif layout not in VALID_LAYOUTS:
        print(f"Error: --layout must be one of {VALID_LAYOUTS}", file=sys.stderr)
        sys.exit(1)
    return {
        "version": STATE_VERSION,
        "root": str(root),
        "layout": layout,
        "synced_at": None,
        "docs": {},
    }


# --- Sync: planning & execution ---

def _read_local_body(path, layout):
    raw = path.read_text(encoding="utf-8")
    if layout == "frontmatter":
        _, body = parse_frontmatter(raw)
    else:
        body = raw
    return raw, body


def build_sync_plan(state, remote_docs, force_title=False):
    """Categorize every local file and remote doc into action buckets."""
    root = Path(state["root"])
    layout = state["layout"]
    state_docs = state.get("docs", {}) or {}
    remote_by_slug = {d.get("slug"): d for d in remote_docs if d.get("slug")}

    plan = {
        "create": [], "update": [], "conflict": [],
        "unchanged": [], "skip_format": [],
        "missing_local": [], "remote_only": [],
        "title_fallback": [], "errors": [],
        "slug_map": {},
    }

    local_by_slug = {}
    for path in scan_md_files(root):
        try:
            slug = slug_for_file(path, root, layout)
        except ValueError as e:
            plan["errors"].append(str(e))
            continue
        local_by_slug[slug] = path
        rel = str(path.relative_to(root))
        plan["slug_map"][rel] = slug
        plan["slug_map"][path.name] = slug

    for slug, path in local_by_slug.items():
        try:
            raw, body = _read_local_body(path, layout)
        except OSError as e:
            plan["errors"].append(f"{path}: {e}")
            continue
        local_sha = sha256_body(body)
        title, title_source = extract_title(
            raw, file_stem=path.stem, slug=slug, force_filename=force_title,
        )
        rel = str(path.relative_to(root))
        if title_source in ("filename", "slug"):
            plan["title_fallback"].append({
                "slug": slug, "title": title,
                "path": rel, "title_source": title_source,
            })
        remote = remote_by_slug.get(slug)
        st = state_docs.get(slug)

        if remote is None:
            plan["create"].append({
                "slug": slug, "title": title, "path": rel,
                "body": body, "local_sha": local_sha,
            })
            continue

        if remote.get("format") and remote["format"] != "markdown":
            plan["skip_format"].append({
                "slug": slug, "title": remote.get("title"),
                "doc_id": remote.get("id"), "remote_format": remote.get("format"),
                "path": rel,
            })
            continue

        remote_version = remote.get("latest_version_id")
        local_unchanged = (st is not None) and (local_sha == st.get("local_sha256"))
        remote_changed = (
            st is not None
            and st.get("remote_latest_version_id") is not None
            and remote_version is not None
            and remote_version != st.get("remote_latest_version_id")
        )

        if st is None:
            plan["conflict"].append({
                "slug": slug, "title": remote.get("title"),
                "doc_id": remote.get("id"), "path": rel,
                "reason": "first_sync_existing_remote",
                "local_sha": local_sha,
                "remote_version_now": remote_version,
            })
        elif local_unchanged and not remote_changed:
            plan["unchanged"].append({
                "slug": slug, "title": remote.get("title"),
                "doc_id": remote.get("id"),
            })
        elif local_unchanged and remote_changed:
            plan["conflict"].append({
                "slug": slug, "title": remote.get("title"),
                "doc_id": remote.get("id"), "path": rel,
                "reason": "remote_moved",
                "remote_version_was": st.get("remote_latest_version_id"),
                "remote_version_now": remote_version,
            })
        elif not local_unchanged and not remote_changed:
            plan["update"].append({
                "slug": slug, "title": title, "doc_id": remote.get("id"),
                "path": rel, "body": body, "local_sha": local_sha,
                "remote_version_now": remote_version,
            })
        else:
            plan["conflict"].append({
                "slug": slug, "title": remote.get("title"),
                "doc_id": remote.get("id"), "path": rel,
                "reason": "both_changed",
                "remote_version_was": st.get("remote_latest_version_id"),
                "remote_version_now": remote_version,
                "local_sha": local_sha,
            })

    for slug, remote in remote_by_slug.items():
        if slug in local_by_slug:
            continue
        if slug in state_docs:
            # Tracked but local file gone — handled by missing_local below.
            continue
        plan["remote_only"].append({
            "slug": slug, "title": remote.get("title"),
            "doc_id": remote.get("id"), "format": remote.get("format"),
            "content_updated_at": remote.get("content_updated_at"),
            "latest_version_id": remote.get("latest_version_id"),
        })

    for slug, st in state_docs.items():
        if slug in local_by_slug:
            continue
        if slug not in remote_by_slug:
            continue
        plan["missing_local"].append({
            "slug": slug,
            "title": remote_by_slug[slug].get("title"),
            "doc_id": st.get("doc_id") or remote_by_slug[slug].get("id"),
            "last_synced_at": st.get("last_synced_at") or state.get("synced_at"),
        })

    return plan


def execute_push(plan, client, state):
    counts = {"created": 0, "updated": 0}
    unresolved_links = []
    slug_map = plan.get("slug_map", {})

    def prepare_body(raw_body):
        body, unresolved = rewrite_links(raw_body, slug_map)
        unresolved_links.extend(unresolved)
        body = fix_bold_format(body)
        return body

    for item in plan["create"]:
        body = prepare_body(item["body"])
        result = client.create_doc(
            body=body, title=item["title"],
            slug=item["slug"], format="markdown",
        )
        doc = result.get("data", {}) or {}
        doc_id = doc.get("id")
        if doc_id:
            try:
                client.append_doc_to_toc(doc_id)
            except SystemExit:
                pass
        state["docs"][item["slug"]] = {
            "doc_id": doc_id,
            "title": doc.get("title", item["title"]),
            "local_path": item["path"],
            "local_sha256": item["local_sha"],
            "remote_latest_version_id": doc.get("latest_version_id"),
            "remote_content_updated_at": doc.get("content_updated_at"),
            "last_synced_at": now_iso(),
        }
        counts["created"] += 1

    for item in plan["update"]:
        body = prepare_body(item["body"])
        result = client.update_doc(
            item["doc_id"], body=body, title=item["title"], format="markdown",
        )
        doc = result.get("data", {}) or {}
        state["docs"][item["slug"]] = {
            "doc_id": item["doc_id"],
            "title": doc.get("title", item["title"]),
            "local_path": item["path"],
            "local_sha256": item["local_sha"],
            "remote_latest_version_id": doc.get("latest_version_id") or item.get("remote_version_now"),
            "remote_content_updated_at": doc.get("content_updated_at"),
            "last_synced_at": now_iso(),
        }
        counts["updated"] += 1

    if unresolved_links:
        unique = sorted(set(unresolved_links))
        print(f"Warning: {len(unique)} link(s) could not be resolved to a slug "
              f"(kept as-is):", file=sys.stderr)
        for link in unique[:20]:
            print(f"  {link}", file=sys.stderr)
        if len(unique) > 20:
            print(f"  ... and {len(unique) - 20} more", file=sys.stderr)

    return counts


def execute_on_missing(action, plan, client, state):
    """Apply --on-missing decision to each missing_local item."""
    counts = {"deleted": 0, "pulled": 0, "forgotten": 0}
    root = Path(state["root"])
    layout = state["layout"]

    for item in plan["missing_local"]:
        slug = item["slug"]
        if action == "delete":
            client.delete_doc(item["doc_id"])
            state["docs"].pop(slug, None)
            counts["deleted"] += 1
        elif action == "pull":
            detail = client.get_doc(item["doc_id"]).get("data", {}) or {}
            if detail.get("format") and detail.get("format") != "markdown":
                print(f"Warning: skip pull of '{slug}' — remote format is {detail.get('format')}",
                      file=sys.stderr)
                continue
            target = file_path_for_slug(slug, root, layout)
            target.parent.mkdir(parents=True, exist_ok=True)
            body = detail.get("body", "") or ""
            if layout == "frontmatter":
                body = f"---\nslug: {slug}\ntitle: {detail.get('title', slug)}\n---\n\n{body}"
            target.write_text(normalize_body(body), encoding="utf-8")
            state["docs"][slug] = {
                "doc_id": detail.get("id"),
                "title": detail.get("title"),
                "local_path": str(target.relative_to(root)),
                "local_sha256": sha256_body(detail.get("body", "") or ""),
                "remote_latest_version_id": detail.get("latest_version_id"),
                "remote_content_updated_at": detail.get("content_updated_at"),
                "last_synced_at": now_iso(),
            }
            counts["pulled"] += 1
        elif action == "forget":
            state["docs"].pop(slug, None)
            counts["forgotten"] += 1

    return counts


# --- Sync: output formatting ---

def _section(title, items, line_fmt):
    if not items:
        return ""
    out = [f"{title} ({len(items)}):"]
    for it in items:
        out.append("  " + line_fmt(it))
    return "\n".join(out) + "\n"


def render_status(plan):
    """Human-readable status report. Sections fixed; Claude translates per user language."""
    parts = []
    parts.append(_section(
        "Local changes to push", plan["create"] + plan["update"],
        lambda x: f"{x.get('slug'):30} {x.get('title') or ''}",
    ))
    parts.append(_section(
        "Conflicts (skipped — resolve manually with `pull`/`update`)", plan["conflict"],
        lambda x: f"{x.get('slug'):30} reason={x.get('reason')}  doc_id={x.get('doc_id')}",
    ))
    parts.append(_section(
        "Skipped (remote format is not markdown)", plan["skip_format"],
        lambda x: f"{x.get('slug'):30} format={x.get('remote_format')}  doc_id={x.get('doc_id')}",
    ))
    parts.append(_section(
        "Remote-only (not in local; run `pull --slug <slug>` or `pull --all` to fetch)",
        plan["remote_only"],
        lambda x: f"{x.get('slug'):30} {x.get('title') or ''}  doc_id={x.get('doc_id')}",
    ))
    parts.append(_section(
        "Missing locally (previously synced; needs --on-missing decision)",
        plan["missing_local"],
        lambda x: f"{x.get('slug'):30} {x.get('title') or ''}  doc_id={x.get('doc_id')}",
    ))
    parts.append(_section(
        "Unchanged", plan["unchanged"],
        lambda x: f"{x.get('slug'):30} {x.get('title') or ''}",
    ))
    parts.append(_section(
        "Title fallback (no H1 or frontmatter title — using filename/slug)",
        plan.get("title_fallback", []),
        lambda x: f"{x.get('slug'):30} source={x.get('title_source')}  path={x.get('path')}",
    ))
    if plan["errors"]:
        parts.append("Errors:\n" + "\n".join("  " + e for e in plan["errors"]) + "\n")
    text = "\n".join(p for p in parts if p)
    return text or "Nothing to report. Local and remote are in sync.\n"


def render_missing_confirmation(plan, pushed_counts):
    """Fixed-format confirmation message for the missing_local case.
    Caller (Claude) translates to the user's query language while keeping
    flag values like `--on-missing delete` literal."""
    lines = []
    lines.append("⚠️  Confirmation required: local files are missing")
    lines.append("")
    lines.append(f"The following {len(plan['missing_local'])} document(s) were previously synced "
                 f"from this directory")
    lines.append("but no longer exist locally. No remote action has been taken.")
    lines.append("")
    lines.append(f"  {'Slug':<24} {'Title':<32} {'Doc ID':<10} Last synced")
    lines.append("  " + "─" * 78)
    for it in plan["missing_local"]:
        title = (it.get("title") or "")[:30]
        last = (it.get("last_synced_at") or "")[:19]
        lines.append(f"  {it.get('slug'):<24} {title:<32} {str(it.get('doc_id') or ''):<10} {last}")
    lines.append("")
    lines.append("How should I handle them on Yuque?")
    lines.append("")
    lines.append("  [delete]  Delete them on Yuque as well")
    lines.append("            → re-run with: --on-missing delete")
    lines.append("")
    lines.append("  [pull]    Restore them locally by pulling from Yuque")
    lines.append("            → re-run with: --on-missing pull")
    lines.append("")
    lines.append("  [forget]  Keep them on Yuque, drop from local sync state")
    lines.append("            → re-run with: --on-missing forget")
    lines.append("")
    pushed_summary = (
        f"Other changes ({pushed_counts.get('updated', 0)} updated, "
        f"{pushed_counts.get('created', 0)} created) were pushed successfully."
    )
    lines.append(pushed_summary)
    lines.append("Re-run sync with one of the options above to resolve the missing files.")
    return "\n".join(lines) + "\n"


def render_missing_confirmation_json(plan, pushed_counts):
    return {
        "status": "confirmation_required",
        "reason": "local_files_missing",
        "exit_code": 2,
        "pushed": pushed_counts,
        "missing": plan["missing_local"],
        "options": [
            {"key": "delete", "flag": "--on-missing delete",
             "description": "Delete on Yuque as well"},
            {"key": "pull", "flag": "--on-missing pull",
             "description": "Restore locally by pulling from Yuque"},
            {"key": "forget", "flag": "--on-missing forget",
             "description": "Keep on Yuque, drop from local sync state"},
        ],
    }


# --- Sync commands ---

def _ensure_state_or_init(args, allow_init=True):
    """Return (state, was_initialized). Init from --root/--layout if no state file."""
    state = load_state()
    if state is not None:
        return state, False
    if not allow_init:
        print(f"Error: no {STATE_FILENAME} found. Run `sync` first or pass --root.", file=sys.stderr)
        sys.exit(1)
    root = getattr(args, "root", None) or os.getcwd()
    layout = getattr(args, "layout", None)
    state = init_state(root, layout=layout)
    return state, True


def cmd_sync(args, client):
    state, initialized = _ensure_state_or_init(args)
    if initialized:
        print(f"Initialized sync state at {state_path()} "
              f"(root={state['root']}, layout={state['layout']}).", file=sys.stderr)

    remote_docs = client.list_all_docs(optional_properties="latest_version_id")
    plan = build_sync_plan(state, remote_docs, force_title=getattr(args, "force_title", False))

    if args.check or args.dry_run:
        if args.json:
            output({"plan": plan}, use_json=True)
        else:
            print(render_status(plan))
        return

    pushed = execute_push(plan, client, state)
    save_state(state)

    if plan["missing_local"]:
        if args.on_missing:
            counts = execute_on_missing(args.on_missing, plan, client, state)
            save_state(state)
            if args.json:
                output({"status": "ok", "pushed": pushed, "on_missing": args.on_missing,
                        "missing_counts": counts}, use_json=True)
            else:
                print(f"Pushed: {pushed['updated']} updated, {pushed['created']} created.")
                print(f"Missing handled ({args.on_missing}): "
                      f"{counts['deleted']} deleted, {counts['pulled']} pulled, "
                      f"{counts['forgotten']} forgotten.")
            return
        # Block with confirmation request.
        if args.json:
            output(render_missing_confirmation_json(plan, pushed), use_json=True)
        else:
            print(render_missing_confirmation(plan, pushed))
        sys.exit(2)

    # Plain success
    summary = {
        "status": "ok", "pushed": pushed,
        "skipped": {"unchanged": len(plan["unchanged"]),
                    "conflict": len(plan["conflict"]),
                    "non_markdown": len(plan["skip_format"])},
        "remote_only": len(plan["remote_only"]),
    }
    if args.json:
        output(summary, use_json=True)
    else:
        print(f"Pushed: {pushed['updated']} updated, {pushed['created']} created.")
        skipped = summary["skipped"]
        if any(skipped.values()):
            print(f"Skipped: {skipped['unchanged']} unchanged, "
                  f"{skipped['conflict']} conflict, {skipped['non_markdown']} non-markdown.")
        if summary["remote_only"]:
            print(f"Remote-only: {summary['remote_only']} doc(s) — run `status` to list, "
                  f"or `pull --all` to fetch.")


def cmd_status(args, client):
    state, initialized = _ensure_state_or_init(args)
    if initialized:
        print(f"Initialized sync state at {state_path()} "
              f"(root={state['root']}, layout={state['layout']}).", file=sys.stderr)
    remote_docs = client.list_all_docs(optional_properties="latest_version_id")
    plan = build_sync_plan(state, remote_docs)
    if args.json:
        output({"plan": plan}, use_json=True)
    else:
        print(render_status(plan))


def cmd_pull(args, client):
    state, initialized = _ensure_state_or_init(args)
    if initialized:
        print(f"Initialized sync state at {state_path()} "
              f"(root={state['root']}, layout={state['layout']}).", file=sys.stderr)

    root = Path(state["root"])
    layout = state["layout"]

    # Build slug -> local filename map for reverse link conversion
    reverse_map = {}
    for s, info in (state.get("docs", {}) or {}).items():
        lp = info.get("local_path")
        if lp:
            reverse_map[s] = lp

    if args.all:
        remote_docs = client.list_all_docs(optional_properties="latest_version_id")
        targets = [d.get("slug") for d in remote_docs if d.get("slug")]
    elif args.slug:
        targets = [args.slug]
    else:
        print("Error: pass --slug <slug> or --all.", file=sys.stderr)
        sys.exit(1)

    pulled = []
    skipped = []
    for slug in targets:
        detail = client.get_doc(slug).get("data", {}) or {}
        if detail.get("format") and detail.get("format") != "markdown":
            skipped.append({"slug": slug, "reason": f"format={detail.get('format')}"})
            continue
        target = file_path_for_slug(slug, root, layout)
        if target.exists() and not args.overwrite:
            skipped.append({"slug": slug, "reason": "local file exists (pass --overwrite to replace)"})
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        body = detail.get("body", "") or ""
        if reverse_map:
            body = reverse_links(body, reverse_map)
        if layout == "frontmatter":
            body = f"---\nslug: {slug}\ntitle: {detail.get('title', slug)}\n---\n\n{body}"
        target.write_text(normalize_body(body), encoding="utf-8")
        state["docs"][slug] = {
            "doc_id": detail.get("id"),
            "title": detail.get("title"),
            "local_path": str(target.relative_to(root)),
            "local_sha256": sha256_body(detail.get("body", "") or ""),
            "remote_latest_version_id": detail.get("latest_version_id"),
            "remote_content_updated_at": detail.get("content_updated_at"),
            "last_synced_at": now_iso(),
        }
        pulled.append({"slug": slug, "path": str(target.relative_to(root))})

    save_state(state)

    if args.json:
        output({"status": "ok", "pulled": pulled, "skipped": skipped}, use_json=True)
    else:
        for p in pulled:
            print(f"Pulled: {p['slug']} -> {p['path']}")
        for s in skipped:
            print(f"Skipped: {s['slug']} ({s['reason']})")
        if not pulled and not skipped:
            print("Nothing to pull.")


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Yuque Document Manager",
        epilog="Environment: YUQUE_TOKEN, YUQUE_REPO (group_login/book_slug), YUQUE_BASE_URL (optional)")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON output")
    parser.add_argument("--dry-run", action="store_true", help="Preview action without executing (create/update/delete)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = subparsers.add_parser("list", help="List documents in the knowledge base")
    p_list.add_argument("-o", "--offset", type=int, default=0, help="Pagination offset (default: 0)")
    p_list.add_argument("-l", "--limit", type=int, default=100, help="Docs per page, max 100 (default: 100)")

    # get
    p_get = subparsers.add_parser("get", help="Get document detail")
    p_get.add_argument("id_or_slug", help="Document ID or slug")

    # create
    p_create = subparsers.add_parser("create", help="Create a new document")
    p_create.add_argument("-t", "--title", default=None, help="Document title")
    body_group = p_create.add_mutually_exclusive_group(required=True)
    body_group.add_argument("-b", "--body", default=None, help="Body content as string")
    body_group.add_argument("-f", "--body-file", default=None, help="Read body from file path")
    p_create.add_argument("--format", choices=["markdown", "html", "lake"], default="markdown", help="Content format (default: markdown)")
    p_create.add_argument("--public", type=int, choices=[0, 1, 2], default=None, help="Visibility: 0=private, 1=public, 2=org-internal")
    p_create.add_argument("--slug", default=None, help="Custom URL slug")
    p_create.add_argument("--no-toc", action="store_true", help="Skip automatic TOC insertion")

    # update
    p_update = subparsers.add_parser("update", help="Update an existing document")
    p_update.add_argument("id_or_slug", help="Document ID or slug")
    p_update.add_argument("-t", "--title", default=None, help="New title")
    body_group_u = p_update.add_mutually_exclusive_group()
    body_group_u.add_argument("-b", "--body", default=None, help="New body content")
    body_group_u.add_argument("-f", "--body-file", default=None, help="Read new body from file")
    p_update.add_argument("--format", choices=["markdown", "html", "lake"], default=None, help="Content format")
    p_update.add_argument("--public", type=int, choices=[0, 1, 2], default=None, help="Visibility")
    p_update.add_argument("--slug", default=None, help="New slug")

    # delete
    p_delete = subparsers.add_parser("delete", help="Delete a document")
    p_delete.add_argument("id_or_slug", help="Document ID or slug")
    p_delete.add_argument("--confirm", action="store_true", required=True, help="Confirm deletion (mandatory)")

    # setup
    p_setup = subparsers.add_parser("setup", help="Initialize .env from a Yuque knowledge base URL")
    p_setup.add_argument("--url", required=True, help="Yuque knowledge base URL (e.g. https://xxx.yuque.com/group/book)")
    p_setup.add_argument("--token", required=True, help="Yuque API token")
    p_setup.add_argument("--env-path", default=None, help="Path to write .env file (default: ./.env)")
    p_setup.add_argument("--force", action="store_true", help="Overwrite existing .env file")

    # toc
    subparsers.add_parser("toc", help="Show knowledge base table of contents")

    # sync
    p_sync = subparsers.add_parser(
        "sync",
        help="Sync local markdown files <-> Yuque (push only changed docs)",
    )
    p_sync.add_argument("--root", default=None,
                        help="Local root directory for first-time init (default: cwd)")
    p_sync.add_argument("--layout", choices=VALID_LAYOUTS, default=None,
                        help="Force layout for first-time init: flat | nested | frontmatter")
    p_sync.add_argument("--check", action="store_true",
                        help="Show diff only; do not push, pull, or delete")
    p_sync.add_argument("--on-missing", choices=["delete", "pull", "forget"], default=None,
                        help="How to handle docs that exist remotely but not locally "
                             "(blocks for confirmation if not provided)")
    p_sync.add_argument("--force-title", action="store_true",
                        help="Always use the file name as the doc title, "
                             "ignoring H1 and frontmatter title")

    # pull
    p_pull = subparsers.add_parser(
        "pull",
        help="Pull remote doc(s) down to local files",
    )
    p_pull.add_argument("--root", default=None, help="Local root for first-time init")
    p_pull.add_argument("--layout", choices=VALID_LAYOUTS, default=None,
                        help="Force layout for first-time init")
    pull_target = p_pull.add_mutually_exclusive_group(required=True)
    pull_target.add_argument("--slug", default=None, help="Pull a single doc by slug")
    pull_target.add_argument("--all", action="store_true", help="Pull every remote doc")
    p_pull.add_argument("--overwrite", action="store_true",
                        help="Overwrite local file if it already exists")

    # status
    p_status = subparsers.add_parser(
        "status",
        help="Show sync diff between local files and Yuque (read-only)",
    )
    p_status.add_argument("--root", default=None, help="Local root for first-time init")
    p_status.add_argument("--layout", choices=VALID_LAYOUTS, default=None,
                          help="Force layout for first-time init")

    args = parser.parse_args()

    # setup command does not need existing config
    if args.command == "setup":
        cmd_setup(args)
        return

    config = load_config()
    client = YuqueClient(config["token"], config["group_login"], config["book_slug"], config["base_url"])

    commands = {
        "list": cmd_list,
        "get": cmd_get,
        "create": cmd_create,
        "update": cmd_update,
        "delete": cmd_delete,
        "toc": cmd_toc,
        "sync": cmd_sync,
        "pull": cmd_pull,
        "status": cmd_status,
    }
    commands[args.command](args, client)


if __name__ == "__main__":
    main()
