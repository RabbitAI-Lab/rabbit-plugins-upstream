#!/usr/bin/env python3
"""周报素材收集:扫描目录下的 Git 仓库,汇总最近 N 天的提交记录。

只读操作(git log),不修改任何仓库。输出 JSON 到 stdout。
用法:python3 collect_git.py --dirs ~/code ~/work --days 7 [--author 名字或邮箱] [--include-merges] [--mode weekly|monthly]
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys

MAX_DEPTH = 3          # 目录扫描深度上限
MAX_REPOS = 30         # 仓库数量上限,防失控
MAX_COMMITS_PER_REPO = 200
GIT_TIMEOUT_SECONDS = 15
SKIP_DIRS = {"node_modules", ".venv", "venv", "Library", ".Trash", ".cache", "__pycache__", ".git"}


def find_repos(roots):
    """在给定根目录内(限深)查找 git 仓库。"""
    repos = []
    for root in roots:
        root = os.path.abspath(os.path.expanduser(root))
        if not os.path.isdir(root):
            continue
        base_depth = root.rstrip(os.sep).count(os.sep)
        for dirpath, dirnames, _ in os.walk(root):
            if dirpath.rstrip(os.sep).count(os.sep) - base_depth >= MAX_DEPTH:
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames
                           if d not in SKIP_DIRS and not (d.startswith(".") and d != ".git")]
            entries = os.listdir(dirpath) if os.path.isdir(dirpath) else []
            if ".git" in entries:
                repos.append(dirpath)
                dirnames[:] = []
            if len(repos) >= MAX_REPOS:
                return repos
    return repos


def repo_commits(repo, days, author, include_merges=False):
    cmd = ["git", "-C", repo, "log", f"--since={days} days ago",
           "--pretty=format:%ad|%s", "--date=format:%Y-%m-%d"]
    if not include_merges:
        cmd.append("--no-merges")
    if author:
        cmd += ["--author", author]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True,
                             timeout=GIT_TIMEOUT_SECONDS).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return []
    commits = []
    for line in out.splitlines()[:MAX_COMMITS_PER_REPO]:
        if "|" in line:
            date, msg = line.split("|", 1)
            commits.append({"date": date, "msg": msg.strip()})
    return commits


def repo_stats(repo, days, author):
    """获取仓库统计:文件数、增删行数。只读,不修改。"""
    cmd = ["git", "-C", repo, "log", f"--since={days} days ago",
           "--pretty=tformat:", "--numstat", "--no-merges"]
    if author:
        cmd += ["--author", author]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True,
                             timeout=GIT_TIMEOUT_SECONDS).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return {"files_changed": 0, "lines_added": 0, "lines_deleted": 0}
    lines_added, lines_deleted = 0, 0
    files = set()
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3:
            try:
                lines_added += int(parts[0]) if parts[0] != "-" else 0
                lines_deleted += int(parts[1]) if parts[1] != "-" else 0
                files.add(parts[2])
            except ValueError:
                continue
    return {"files_changed": len(files), "lines_added": lines_added, "lines_deleted": lines_deleted}


def main():
    parser = argparse.ArgumentParser(description="周报 Git 素材收集(只读)")
    parser.add_argument("--dirs", nargs="+", default=["."], help="要扫描的目录,可多个")
    parser.add_argument("--days", type=int, default=7, help="回溯天数,默认7")
    parser.add_argument("--author", default=None, help="按作者过滤(名字或邮箱片段)")
    parser.add_argument("--include-merges", action="store_true", help="包含 merge commits")
    parser.add_argument("--mode", default="weekly", choices=["weekly", "monthly"],
                        help="周报/月报模式,影响默认天数(weekly=7, monthly=30)")
    parser.add_argument("--with-stats", action="store_true", help="附带每个仓库的增删行数统计")
    args = parser.parse_args()

    days = args.days
    if args.mode == "monthly" and days == 7:
        days = 30  # 月报默认30天

    repos = find_repos(args.dirs)
    result = {
        "generated_at": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "since_days": days,
        "mode": args.mode,
        "author_filter": args.author,
        "include_merges": args.include_merges,
        "repos": [],
    }
    for repo in repos:
        commits = repo_commits(repo, days, args.author, args.include_merges)
        if commits:
            entry = {
                "path": repo,
                "name": os.path.basename(repo),
                "commit_count": len(commits),
                "commits": commits,
            }
            if args.with_stats:
                entry["stats"] = repo_stats(repo, days, args.author)
            result["repos"].append(entry)
    result["total_commits"] = sum(r["commit_count"] for r in result["repos"])
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
