#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search SkillHub (skillhub.cn) public skills API and convert ClawHub links.

Part of the `fuck-clawhub` skill. Queries the public, no-auth SkillHub list
API and prints results in the format required by the skill (name / version /
author / update date / description), ranked by relevance.

Modes:
  search  "<keyword>" [--category CAT] [--limit N] [--sort-by score|downloads|...]
  convert "<clawhub_url>" [--limit N]

Run with the environment Python, e.g.:
  python3 scripts/search_skillhub.py search "pdf 提取"
  python3 scripts/search_skillhub.py convert "https://clawhub.ai/mjzj-tec/mjzj-skillhub"
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_BASE = "https://api.skillhub.cn/api/skills"
WORKBUDDY_SKILLS_DIR = "~/.workbuddy/skills"  # user-level; project-level is <workspace>/.workbuddy/skills


def fetch(keyword, category=None, sort_by="score", page=1, page_size=10):
    params = {
        "keyword": keyword,
        "sortBy": sort_by,
        "page": page,
        "pageSize": page_size,
    }
    if category:
        params["category"] = category
    url = API_BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "fuck-clawhub/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if data.get("code") != 0:
        raise RuntimeError("API error: %s" % data.get("message"))
    return data["data"]


def fmt_date(ms):
    if not ms:
        return "未知"
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def skillhub_url(slug):
    return "https://skillhub.cn/skills/%s" % slug


def install_cmd(slug):
    return "skillhub install %s --dir %s   # WorkBuddy 用户级 skills 目录" % (slug, WORKBUDDY_SKILLS_DIR)


def print_skill(idx, s):
    name = s.get("name", "?")
    version = s.get("version", "?")
    author = s.get("ownerName", "?")
    updated = fmt_date(s.get("updated_at"))
    category = s.get("category", "?")
    desc = (s.get("description_zh") or s.get("description") or "").strip().replace("\n", " ")
    if len(desc) > 120:
        desc = desc[:117] + "..."
    slug = s.get("slug", "?")
    print("%d. %s" % (idx, name))
    print("   版本号: %s   作者: %s   更新日期: %s   分类: %s" % (version, author, updated, category))
    print("   简介: %s" % desc)
    print("   SkillHub 链接: %s" % skillhub_url(slug))
    print("   安装命令: %s" % install_cmd(slug))
    print()


def cmd_search(args):
    data = fetch(args.keyword, args.category, args.sort_by, 1, args.limit)
    skills = data.get("skills", [])
    total = data.get("total", len(skills))
    print("在 SkillHub 找到 %d 个相关 skill，按相关度(score)排序，展示前 %d 个：\n"
          % (total, len(skills)))
    if not skills:
        print("SkillHub 上没有匹配的结果。可换同义词/上位词重试，或去掉 --category 放宽。")
        return
    for i, s in enumerate(skills, 1):
        print_skill(i, s)


def cmd_convert(args):
    url = args.url
    parsed = urllib.parse.urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    slug = None
    namespace = ""
    if parsed.netloc.lower().endswith("clawhub.ai") and len(parts) >= 2:
        namespace = parts[-2]
        slug = parts[-1]
    elif parts:
        slug = parts[-1]
    if not slug:
        print("无法从链接解析出 skill 标识：%s" % url, file=sys.stderr)
        sys.exit(1)

    print("解析 ClawHub 链接 -> namespace=%s  slug=%s" % (namespace or "?", slug))
    print("在 SkillHub 中按名称搜索「%s」...\n" % slug)

    data = fetch(slug, None, "score", 1, args.limit)
    skills = data.get("skills", [])
    total = data.get("total", len(skills))
    print("SkillHub 候选结果（共 %d 个）：\n" % total)
    for i, s in enumerate(skills, 1):
        print_skill(i, s)

    match = None
    for s in skills:
        s_slug = (s.get("slug") or "").lower()
        s_name = (s.get("name") or "").lower().replace(" ", "-")
        if s_slug == slug.lower() or s_name == slug.lower():
            match = s
            break

    if match:
        print("在 SkillHub 找到同名/同 slug 的替代：%s" % skillhub_url(match["slug"]))
    else:
        print("SkillHub 上未找到确定的同名替代（上方为相关候选，请人工判断功能是否相近）。")


def main():
    p = argparse.ArgumentParser(description="Search SkillHub / convert ClawHub links")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("search", help="Search SkillHub by keyword")
    sp.add_argument("keyword")
    sp.add_argument("--category", help="一级分类过滤，如 office-efficiency")
    sp.add_argument("--limit", type=int, default=10)
    sp.add_argument("--sort-by", default="score")
    sp.set_defaults(func=cmd_search)

    cp = sub.add_parser("convert", help="Convert a ClawHub link to SkillHub candidates")
    cp.add_argument("url")
    cp.add_argument("--limit", type=int, default=10)
    cp.set_defaults(func=cmd_convert)

    args = p.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print("错误: %s" % e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
