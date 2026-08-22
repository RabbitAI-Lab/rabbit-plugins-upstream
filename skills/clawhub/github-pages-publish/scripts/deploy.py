#!/usr/bin/env python3
"""Deploy a static site to GitHub Pages.

Full pipeline: create/reuse repo -> upload files (contents API) -> enable Pages -> poll -> print URL.

Usage:
  # Full automation: local dir -> GitHub Pages
  python deploy.py --dir ./site --repo my-site [--owner myname] [--branch gh-pages] [--token ghp_xxx]

  # Single file -> existing repo (does not touch existing index.html)
  python deploy.py --file ./page.html --remote-path page.html --repo my-site [--owner myname] [--branch main]

  # Enable-only: files already uploaded (e.g. via GitHub MCP), just enable Pages + verify
  python deploy.py --enable-only --repo my-site [--owner myname] [--branch gh-pages]

Token resolution order: --token > GITHUB_TOKEN > GH_TOKEN
Uses only the Python standard library (urllib). No pip installs, no git required.
"""

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://api.github.com"


def get_token(args):
    if args.token:
        return args.token
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(name)
        if value:
            return value
    return None


def api_request(method, path, token, data=None):
    url = API + path
    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "github-pages-publish")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as err:
        return err.code, {"error": err.read().decode("utf-8", "replace")}


def resolve_owner(args, token):
    if args.owner:
        return args.owner
    status, me = api_request("GET", "/user", token)
    if status != 200:
        print("[ERROR] Cannot resolve owner: " + str(me.get("error")))
        sys.exit(1)
    return me["login"]


def ensure_repo(owner, repo, token):
    status, _ = api_request("GET", "/repos/{}/{}".format(owner, repo), token)
    if status == 200:
        print("[OK] Repo exists: {}/{}".format(owner, repo))
        return
    if status == 404:
        data = {"name": repo, "private": False, "auto_init": False}
        status, resp = api_request("POST", "/user/repos", token, data)
        if status not in (200, 201):
            print("[ERROR] Failed to create repo: " + str(resp))
            sys.exit(1)
        print("[OK] Repo created: {}/{}".format(owner, repo))
        return
    print("[ERROR] Failed to check repo, HTTP " + str(status))
    sys.exit(1)


def upload_directory(owner, repo, dir_path, branch, token):
    """Incrementally upload a whole directory via the contents API.

    Creates/updates files present locally while leaving any remote files that
    are not in the local directory untouched. This is a per-file sync (no
    `git push --force`), so it can never wipe out pre-existing remote content.
    """
    count = 0
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fname in files:
            local_path = os.path.join(root, fname)
            remote_path = os.path.relpath(local_path, dir_path).replace(os.sep, "/")
            upload_single_file(owner, repo, local_path, remote_path, branch, token)
            count += 1
    print("[OK] Uploaded {} file(s)".format(count))


def upload_single_file(owner, repo, local_file, remote_path, branch, token):
    """Upload one file to an existing repo via the contents API (no git needed).

    Auto-handles update-vs-create: fetches the file's SHA first if it exists.
    """
    with open(local_file, "rb") as f:
        raw = f.read()
    payload = {
        "message": "Add " + remote_path,
        "content": base64.b64encode(raw).decode("ascii"),
        "branch": branch,
    }
    path = "/repos/{}/{}/contents/{}".format(owner, repo, remote_path)
    status, existing = api_request("GET", path, token)
    if status == 200:
        payload["sha"] = existing.get("sha")
        payload["message"] = "Update " + remote_path
    elif status != 404:
        print("[ERROR] Check file failed, HTTP " + str(status))
        sys.exit(1)
    status, resp = api_request("PUT", path, token, payload)
    if status not in (200, 201):
        print("[ERROR] Upload failed: " + str(resp))
        print("[HINT] 403 means the token lacks write access (fine-grained needs Contents=Read and write).")
        sys.exit(1)
    print("[OK] Uploaded: " + remote_path)


def enable_pages(owner, repo, branch, token):
    path = "/repos/{}/{}/pages".format(owner, repo)
    status, _ = api_request("GET", path, token)
    if status == 200:
        print("[OK] Pages already enabled")
        return
    data = {"build_type": "legacy", "source": {"branch": branch, "path": "/"}}
    status, resp = api_request("POST", path, token, data)
    if status not in (200, 201):
        print("[ERROR] Failed to enable Pages: " + str(resp))
        print("[HINT] Manual route: repo Settings -> Pages -> Source: Deploy from a branch ->")
        print("       select branch '{}' and '/ (root)' -> Save.".format(branch))
        sys.exit(1)
    print("[OK] Pages enabled on branch: " + branch)


def wait_until_built(owner, repo, token, timeout=180):
    path = "/repos/{}/{}/pages".format(owner, repo)
    start = time.time()
    while time.time() - start < timeout:
        status, resp = api_request("GET", path, token)
        if status == 200 and resp.get("status") == "built":
            return resp.get("html_url")
        time.sleep(5)
    return None


def main():
    parser = argparse.ArgumentParser(description="Deploy static site to GitHub Pages")
    parser.add_argument("--dir", help="local static site directory (must contain index.html)")
    parser.add_argument("--file", help="single local file to upload (pair with --remote-path)")
    parser.add_argument("--remote-path", help="remote path for --file, e.g. 'page.html'")
    parser.add_argument("--repo", required=True, help="repository name")
    parser.add_argument("--owner", help="GitHub owner (defaults to authenticated user)")
    parser.add_argument("--branch", default="gh-pages", help="publish branch (default gh-pages)")
    parser.add_argument("--token", help="GitHub PAT (or set GITHUB_TOKEN/GH_TOKEN)")
    parser.add_argument("--enable-only", action="store_true",
                        help="only enable Pages + verify (files already uploaded)")
    args = parser.parse_args()

    token = get_token(args)
    if not token:
        print("[ERROR] No GitHub token found.")
        print("  Provide via --token or set env GITHUB_TOKEN / GH_TOKEN.")
        print("  Get a PAT at https://github.com/settings/tokens (scope: repo).")
        sys.exit(1)

    owner = resolve_owner(args, token)
    branch = args.branch

    if args.enable_only:
        enable_pages(owner, args.repo, branch, token)
    elif args.file:
        if not args.remote_path:
            print("[ERROR] --remote-path is required when --file is set.")
            sys.exit(1)
        ensure_repo(owner, args.repo, token)
        upload_single_file(owner, args.repo, args.file, args.remote_path, branch, token)
        enable_pages(owner, args.repo, branch, token)
    else:
        if not args.dir:
            print("[ERROR] --dir is required unless --file/--enable-only is set.")
            sys.exit(1)
        if not os.path.isfile(os.path.join(args.dir, "index.html")):
            print("[ERROR] index.html not found in --dir. Pages needs an index.html at root.")
            sys.exit(1)
        ensure_repo(owner, args.repo, token)
        upload_directory(owner, args.repo, args.dir, branch, token)
        enable_pages(owner, args.repo, branch, token)

    if args.file and args.remote_path:
        final_url = "https://{}.github.io/{}/{}".format(owner, args.repo, args.remote_path)
    elif args.repo == owner + ".github.io":
        final_url = "https://{}.github.io".format(owner)
    else:
        final_url = "https://{}.github.io/{}".format(owner, args.repo)

    built_url = wait_until_built(owner, args.repo, token)
    print("[DONE] Site URL: " + final_url)
    if built_url:
        print("[OK] Deployment confirmed: " + built_url)


if __name__ == "__main__":
    main()
