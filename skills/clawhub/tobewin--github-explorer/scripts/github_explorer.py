#!/usr/bin/env python3
"""
GitHub Explorer — 发现并分析 GitHub 优质开源项目。

纯标准库实现，零外部依赖。通过 GitHub 官方 REST API 搜索仓库、获取详情与 README。

用法:
  python3 github_explorer.py search <关键词> [--mode classic|trending] [--lang python] [--topic ml] [--limit 10] [--stars >1000] [--created-after 2024-01-01] [--created-before 2024-06-01] [--license mit] [--sort stars|forks|updated] [--no-cache]
  python3 github_explorer.py analyze <owner/repo> [--readme-full] [--no-cache]
  python3 github_explorer.py cache [status|clear]
  python3 github_explorer.py help

两种搜索模式:
  classic   经典优质: 按 star 排序，过滤近 6 个月有更新的项目
  trending  新兴热门: 按 star 排序，过滤近 1 年创建的项目（抓新但已起量的项目）

环境变量:
  GITHUB_TOKEN  可选。设置后 Search API 限额从 10 次/分钟提升到 30 次/分钟。

缓存:
  搜索结果和 analyze 结果缓存到 ~/.cache/github-explorer/，有效期 1 小时。
  加 --no-cache 跳过缓存。
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import os
import sys
import base64
import time
import hashlib
import re
from datetime import datetime, timedelta

API_BASE = "https://api.github.com"
CACHE_DIR = os.path.expanduser("~/.cache/github-explorer")
CACHE_TTL = 3600  # 1 hour

# ── Chinese → English keyword mapping ──────────────────────────────
CN_TO_EN = {
    # AI/ML
    "大模型": "large language model",
    "语言模型": "language model",
    "机器学习": "machine learning",
    "深度学习": "deep learning",
    "神经网络": "neural network",
    "人工智能": "artificial intelligence",
    "自然语言处理": "natural language processing",
    "计算机视觉": "computer vision",
    "图像识别": "image recognition",
    "语音识别": "speech recognition",
    "语音合成": "text to speech",
    "文本转语音": "text to speech",
    "推荐系统": "recommender system",
    "强化学习": "reinforcement learning",
    "模型部署": "model serving",
    "模型训练": "model training",
    "模型推理": "inference",
    "向量嵌入": "embedding",
    "向量检索": "vector search",
    "知识图谱": "knowledge graph",
    "多模态": "multimodal",
    "文生图": "text to image",
    "图生文": "image to text",
    "生成式": "generative",
    "智能体": "agent",
    "智能助手": "assistant",
    "推理加速": "inference acceleration",
    "推理": "inference",
    "训练": "training",
    "部署": "deployment",
    "检索": "retrieval",
    "识别": "recognition",
    # Data / DB
    "数据库": "database",
    "向量数据库": "vector database",
    "数据挖掘": "data mining",
    "数据可视化": "data visualization",
    "数据分析": "data analysis",
    "数据工程": "data engineering",
    "数据管道": "data pipeline",
    "大数据": "big data",
    "流处理": "stream processing",
    "实时计算": "real time computing",
    # Web / Frontend
    "前端框架": "frontend framework",
    "前端": "frontend",
    "后端框架": "backend framework",
    "后端": "backend",
    "全栈": "full stack",
    "框架": "framework",
    "组件库": "component library",
    "用户界面": "user interface",
    "移动端": "mobile",
    "跨平台": "cross platform",
    "响应式": "responsive",
    # Languages
    "编程语言": "programming language",
    # Tools / Infra
    "容器编排": "container orchestration",
    "容器": "container",
    "微服务": "microservice",
    "消息队列": "message queue",
    "搜索引擎": "search engine",
    "配置管理": "configuration management",
    "自动化": "automation",
    "监控": "monitoring",
    "日志": "logging",
    "负载均衡": "load balancing",
    "网关": "gateway",
    "代理": "proxy",
    # DevOps
    "持续集成": "continuous integration",
    "持续部署": "continuous deployment",
    "基础设施": "infrastructure",
    # Security
    "安全": "security",
    "加密": "encryption",
    "身份认证": "authentication",
    "权限": "authorization",
    # Git
    "版本控制": "version control",
    # Common tech terms
    "算法": "algorithm",
    "搜索": "search",
    "引擎": "engine",
    "推荐": "recommendation",
    "图像": "image",
    "文本": "text",
    "视频": "video",
    "音频": "audio",
    "组件": "component",
    "插件": "plugin",
    "工具": "tool",
    "平台": "platform",
    "系统": "system",
    "服务": "service",
    "管理": "management",
    "调度": "scheduling",
    "同步": "sync",
    "异步": "async",
    "协议": "protocol",
    "标准": "standard",
    "格式": "format",
    # Misc
    "区块链": "blockchain",
    "物联网": "internet of things",
    "云计算": "cloud computing",
    "边缘计算": "edge computing",
    "编译器": "compiler",
    "操作系统": "operating system",
    "网络": "networking",
    "测试": "testing",
    "单元测试": "unit testing",
    "端到端测试": "end to end testing",
}


def _has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]', text))


def _translate_query(query):
    """If query contains Chinese, map known terms to English using longest-match tokenizer."""
    if not _has_chinese(query):
        return query

    cn_keys = sorted(CN_TO_EN.keys(), key=lambda x: -len(x))

    tokens = []
    i = 0
    while i < len(query):
        matched = False
        for cn in cn_keys:
            if query[i:i + len(cn)] == cn:
                tokens.append(CN_TO_EN[cn])
                i += len(cn)
                matched = True
                break
        if matched:
            continue

        if not _has_chinese(query[i]):
            j = i
            while j < len(query) and not _has_chinese(query[j]):
                j += 1
            piece = query[i:j].strip()
            if piece:
                tokens.append(piece)
            i = j
        else:
            tokens.append(query[i])
            i += 1
    return ' '.join(tokens)


def _sanitize_query(query):
    """Remove or replace chars that confuse GitHub Search API."""
    query = re.sub(r'[^\w\s\-."\'()\[\]{}@$!%&=#:;/\\,<>?+*~`|^]', ' ', query)
    return re.sub(r'\s+', ' ', query).strip()


# ── Cache ──────────────────────────────────────────────────────────

def _cache_key(*parts):
    raw = json.dumps(parts, sort_keys=True)
    return hashlib.md5(raw.encode()).hexdigest()


def _cache_get(*parts):
    key = _cache_key(*parts)
    path = os.path.join(CACHE_DIR, f"{key}.json")
    try:
        with open(path) as f:
            data = json.load(f)
        if time.time() - data["_t"] < CACHE_TTL:
            return data["_r"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass
    return None


def _cache_set(*parts):
    result = parts[-1]
    key_parts = parts[:-1]
    key = _cache_key(*key_parts)
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        path = os.path.join(CACHE_DIR, f"{key}.json")
        with open(path, "w") as f:
            json.dump({"_t": time.time(), "_r": result}, f)
    except OSError:
        pass


def cmd_cache(args):
    """cache [status|clear]"""
    sub = args[0] if args else "status"

    if sub == "status":
        if not os.path.isdir(CACHE_DIR):
            print(json.dumps({"count": 0, "size_bytes": 0, "dir": CACHE_DIR}))
            return
        total = 0
        size = 0
        for fname in os.listdir(CACHE_DIR):
            if fname.endswith(".json"):
                total += 1
                path = os.path.join(CACHE_DIR, fname)
                try:
                    size += os.path.getsize(path)
                except OSError:
                    pass
        print(json.dumps({"count": total, "size_bytes": size, "dir": CACHE_DIR}))
    elif sub == "clear":
        if not os.path.isdir(CACHE_DIR):
            print(json.dumps({"ok": True, "cleared": 0, "dir": CACHE_DIR}))
            return
        cleared = 0
        for fname in os.listdir(CACHE_DIR):
            if fname.endswith(".json"):
                try:
                    os.remove(os.path.join(CACHE_DIR, fname))
                    cleared += 1
                except OSError:
                    pass
        print(json.dumps({"ok": True, "cleared": cleared, "dir": CACHE_DIR}))
    else:
        print(f"未知子命令: {sub}。支持: status, clear", file=sys.stderr)
        sys.exit(1)


# ── API ────────────────────────────────────────────────────────────

def _headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-explorer-skill",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _api_get(path, params=None):
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        remaining = e.headers.get("X-RateLimit-Remaining")
        if e.code == 403 and remaining == "0":
            return {"rate_limit": True,
                    "detail": "GitHub Search API 限流。未配置 GITHUB_TOKEN 时每分钟仅 10 次请求；"
                              "设置环境变量 GITHUB_TOKEN 可提升到 30 次/分钟。"}
        body = e.read().decode(errors="replace")
        try:
            err = json.loads(body)
            return {"error": True, "detail": err.get("message", body)}
        except Exception:
            return {"error": True, "detail": body[:300]}
    except urllib.error.URLError as e:
        return {"error": True, "detail": f"网络错误: {e}"}
    except Exception as e:
        return {"error": True, "detail": str(e)}


def _date_years_ago(years):
    return (datetime.now() - timedelta(days=365 * years)).strftime("%Y-%m-%d")


def _date_months_ago(months):
    return (datetime.now() - timedelta(days=30 * months)).strftime("%Y-%m-%d")


# ── Flag parser ────────────────────────────────────────────────────

def _parse_flags(args):
    flags = {}
    positionals = []
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith("--"):
            key = a[2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                flags[key] = args[i + 1]
                i += 2
            else:
                flags[key] = True
                i += 1
        else:
            positionals.append(a)
            i += 1
    return flags, positionals


# ── Commands ───────────────────────────────────────────────────────

def cmd_search(args):
    flags, positionals = _parse_flags(args)

    if flags.pop("help", None) or flags.pop("h", None):
        print("用法: search <关键词> [--mode classic|trending] [--lang python] [--topic ml]")
        print("               [--limit 10] [--stars >1000] [--created-after 2024-01-01]")
        print("               [--created-before 2024-06-01] [--license mit] [--sort stars|forks|updated]")
        print("               [--no-cache]")
        print()
        print("  关键词: 支持中英文混合输入，中文技术术语自动映射到英文")
        print("  --mode: classic（默认，按 star）/ trending（新兴，近 1 年创建）")
        print("  --lang: 限定编程语言，如 python / rust / go")
        print("  --topic: 限定 GitHub 主题标签，如 machine-learning")
        print("  --limit: 返回数量，默认 10，最大 30")
        print("  --stars: star 数过滤，如 >1000 / >=5000 / 1000..5000")
        print("  --created-after: 创建时间下限，如 2024-01-01")
        print("  --created-before: 创建时间上限，如 2024-06-01")
        print("  --license: 许可证类型，如 mit / apache-2.0 / gpl-3.0")
        print("  --sort: 排序字段，stars（默认）/ forks / updated")
        print("  --no-cache: 跳过缓存，强制请求 API")
        return None

    query = " ".join(positionals)
    if not query:
        return {"error": True, "detail": "请输入搜索关键词，例如: python web framework"}

    query = _translate_query(query)
    query = _sanitize_query(query)

    mode = flags.get("mode", "classic")
    lang = flags.get("lang")
    topic = flags.get("topic")
    stars = flags.get("stars", "").strip()
    created_after = flags.get("created-after", "").strip()
    created_before = flags.get("created-before", "").strip()
    lic = flags.get("license", "").strip()
    sort = flags.get("sort", "stars")
    no_cache = flags.get("no-cache", False)

    try:
        limit = int(flags.get("limit", 10))
    except ValueError:
        limit = 10
    limit = max(1, min(limit, 30))

    q_parts = [query]
    if lang:
        q_parts.append(f"language:{lang}")
    if topic:
        q_parts.append(f"topic:{topic}")
    if stars:
        if stars.isdigit():
            stars = f">={stars}"
        q_parts.append(f"stars:{stars}")
    if created_after:
        q_parts.append(f"created:>{created_after}")
    if created_before:
        q_parts.append(f"created:<{created_before}")
    if lic:
        q_parts.append(f"license:{lic}")
    q_parts.append("fork:false")
    if mode == "trending":
        q_parts.append(f"created:>{_date_years_ago(1)}")
    else:
        q_parts.append(f"pushed:>{_date_months_ago(6)}")
    q = " ".join(q_parts)

    if sort not in ("stars", "forks", "updated"):
        sort = "stars"

    cache_args = {"mode": mode, "q": q, "limit": limit, "sort": sort}
    if not no_cache:
        cached = _cache_get("search", cache_args)
        if cached is not None:
            cached["_cache"] = "hit"
            return cached

    data = _api_get("/search/repositories", {
        "q": q,
        "sort": sort,
        "order": "desc",
        "per_page": limit,
    })
    if data.get("error") or data.get("rate_limit"):
        return data

    items = data.get("items", [])
    results = []
    for it in items:
        results.append({
            "full_name": it.get("full_name"),
            "url": it.get("html_url"),
            "description": it.get("description") or "",
            "stars": it.get("stargazers_count", 0),
            "forks": it.get("forks_count", 0),
            "language": it.get("language"),
            "topics": it.get("topics", []),
            "pushed_at": it.get("pushed_at"),
            "license": (it.get("license") or {}).get("spdx_id"),
        })
    result = {
        "mode": mode,
        "query": query,
        "total_count": data.get("total_count", 0),
        "count": len(results),
        "results": results,
    }
    _cache_set("search", cache_args, result)
    return result


def cmd_analyze(args):
    flags, positionals = _parse_flags(args)

    if flags.pop("help", None) or flags.pop("h", None):
        print("用法: analyze <owner/repo> [--readme-full] [--no-cache]")
        print()
        print("  owner/repo: 仓库全名，如 langchain-ai/langchain")
        print("  --readme-full: 获取完整 README 内容（默认截断 8000 字符）")
        print("  --no-cache: 跳过缓存，强制请求 API")
        return None

    repo = positionals[0] if positionals else ""
    if not repo or "/" not in repo:
        return {"error": True, "detail": "请输入 owner/repo，例如: langchain-ai/langchain"}
    no_cache = flags.get("no-cache", False)
    readme_full = flags.get("readme-full", False)

    if not no_cache:
        cached = _cache_get("analyze", repo, readme_full)
        if cached is not None:
            cached["_cache"] = "hit"
            return cached

    detail = _api_get(f"/repos/{repo}")
    if detail.get("error") or detail.get("rate_limit"):
        return detail
    if detail.get("message") == "Not Found":
        return {"error": True, "detail": f"仓库不存在: {repo}"}

    readme = _api_get(f"/repos/{repo}/readme")
    readme_text = ""
    if not readme.get("error") and readme.get("content"):
        try:
            readme_text = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
        except Exception:
            readme_text = ""
    if not readme_full:
        readme_text = readme_text[:8000]

    result = {
        "full_name": detail.get("full_name"),
        "url": detail.get("html_url"),
        "description": detail.get("description") or "",
        "stars": detail.get("stargazers_count", 0),
        "forks": detail.get("forks_count", 0),
        "watchers": detail.get("subscribers_count", 0),
        "open_issues": detail.get("open_issues_count", 0),
        "language": detail.get("language"),
        "topics": detail.get("topics", []),
        "license": (detail.get("license") or {}).get("spdx_id"),
        "created_at": detail.get("created_at"),
        "pushed_at": detail.get("pushed_at"),
        "homepage": detail.get("homepage"),
        "readme": readme_text,
    }
    _cache_set("analyze", repo, readme_full, result)
    return result


def print_help():
    print("GitHub Explorer — 发现并分析 GitHub 优质开源项目")
    token = os.environ.get("GITHUB_TOKEN")
    print(f"GITHUB_TOKEN: {'✅ Set (30 req/min)' if token else '❌ Not set (10 req/min)'}")
    print(f"Cache: {CACHE_DIR}")
    print()
    print("Commands:")
    print("  search <query> [--mode classic|trending] [--lang python] [--topic ml] [--limit 10]")
    print("               [--stars >1000] [--created-after 2024-01-01] [--created-before 2024-06-01]")
    print("               [--license mit] [--sort stars|forks|updated] [--no-cache]")
    print("  analyze <owner/repo> [--readme-full] [--no-cache]")
    print("  cache [status|clear]                查看或清空本地缓存")
    print("  help                                 显示本帮助")
    print()
    print("查询关键词支持中英文混合输入，中文技术术语自动映射为英文。")
    print()
    print("Examples:")
    print('  python3 github_explorer.py search "llm inference" --lang python --sort stars --limit 10')
    print('  python3 github_explorer.py search "大模型 推理加速" --lang python --stars ">5000"')
    print("  python3 github_explorer.py analyze langchain-ai/langchain --readme-full")
    print("  python3 github_explorer.py search 向量数据库 --mode trending --license mit")
    print("  python3 github_explorer.py cache status")
    print("  python3 github_explorer.py cache clear")
    print()
    print("More: 对 search / analyze 加 --help 查看子命令详细参数。")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("help", "--help", "-h"):
        print_help()
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]
    handlers = {
        "search": cmd_search,
        "analyze": cmd_analyze,
        "cache": cmd_cache,
    }
    handler = handlers.get(cmd)
    if not handler:
        print(json.dumps({"error": True, "detail": f"未知命令: {cmd}"}, ensure_ascii=False))
        sys.exit(1)
    result = handler(args)
    if result is None:
        sys.exit(0)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("error") or result.get("rate_limit"):
        sys.exit(1)
