#!/usr/bin/env python3
"""
AI Daily Briefing - 统一采集脚本
支持 5 个板块参数化采集，自动根据环境选择数据源。

用法：
  python3 collect.py --section industry          # 行业动态
  python3 collect.py --section github             # GitHub Trending
  python3 collect.py --section producthunt        # Product Hunt
  python3 collect.py --section agent_eng          # Agent 工程
  python3 collect.py --section frontier           # 前沿技术
  python3 collect.py --section industry --output /tmp/my.json  # 指定输出

环境变量：
  PROXY_URL, PH_API_TOKEN, FIRECRAWL_API_KEY, AI_DAILY_DB_PATH
"""
import argparse, json, os, subprocess, re, concurrent.futures, sys
from pathlib import Path
from datetime import datetime, timedelta

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from common import load_env, get_proxy, curl_json, curl_text, default_output_dir, default_date


# ── 环境 ──
load_env()
DATE = os.environ.get("AI_DAILY_DATE", os.popen("date +%Y-%m-%d").read().strip())
DEFAULT_OUTPUT_DIR = f"/tmp/ai-daily-briefing/{DATE}"

# ── 板块配置 ──
SECTIONS = {
    "industry": {
        "source": "hn_topstories",
        "backup_sources": ["official_blogs"],
        "max": 10,
        "keywords": ["claude", "openai", "gpt", "anthropic", "model", "agent", "benchmark", "ai ", "llm"],
    },
    "github": {
        "api_source": "github_search",
        "max": 5,
        "query": "created:>{week_ago}+stars:>50+topic:ai",
    },
    "producthunt": {
        "api_source": "producthunt_graphql",
        "max": 5,
        "query": 'posts(first: 10, order: VOTES, topic: "artificial-intelligence") { edges { node { name tagline votesCount url } } }',
    },
    "agent_eng": {
        "source": "hn_algolia_blogs",
        "backup_sources": ["github_topics_agent"],
        "max": 5,
        "keywords": ["agent framework", "eval loop", "multi-agent", "agent workflow", "agent infrastructure"],
    },
    "frontier": {
        "api_source": "arxiv_github",
        "max": 5,
        "arxiv_query": "all:agent+AND+(all:memory+OR+all:observability+OR+all:self-improvement)",
        "github_query": "agent+memory+OR+observability+OR+self-improvement",
    },
}


# ── 采集器 ──

def collect_hn_topstories(section, max_items):
    """从 HN Top Stories 采集。"""
    ids = curl_json("https://hacker-news.firebaseio.com/v0/topstories.json")
    if not ids:
        return []
    
    ids = ids[:20]
    
    def fetch(id):
        return curl_json(f"https://hacker-news.firebaseio.com/v0/item/{id}.json", max_time=10)
    
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        items = [i for i in ex.map(fetch, ids) if i]
    
    keywords = SECTIONS[section].get("keywords", [])
    filtered = [i for i in items if any(k in f"{i.get('title','').lower()} {i.get('url','').lower()}" for k in keywords)]
    filtered.sort(key=lambda x: x.get("score", 0), reverse=True)
    
    results = []
    for item in filtered[:max_items]:
        results.append({
            "title": item.get("title", "")[:50],
            "url": item.get("url", f"https://news.ycombinator.com/item?id={item.get('id')}"),
            "description": f"HN 讨论: {item.get('score', 0)} ⬆ / {item.get('descendants', 0)} 评论",
            "metric": f"{item.get('score', 0)} ⬆"
        })
    return results


def collect_official_blogs(max_items):
    """从官方博客 RSS 采集第一手发布信息。"""
    # Google AI Blog (新地址)
    blogs = [
        {"name": "OpenAI", "url": "https://openai.com/blog/rss.xml"},
        {"name": "DeepMind", "url": "https://deepmind.google/blog/rss.xml"},
        {"name": "Google AI Blog", "url": "https://blog.google/technology/ai/rss/"},
    ]
    
    results = []
    
    # ── 尝试 Firecrawl 抓取 Anthropic News ──
    fc_key = os.environ.get("FIRECRAWL_API_KEY", "")
    if fc_key:
        try:
            import json as _json
            r = subprocess.run(
                [
                    "curl", "-s", "--max-time", "20",
                    "-X", "POST", "https://api.firecrawl.dev/v1/scrape",
                    "-H", "Content-Type: application/json",
                    "-H", f"Authorization: Bearer {fc_key}",
                    "-d", _json.dumps({"url": "https://www.anthropic.com/news", "formats": ["markdown"]})
                ],
                capture_output=True, text=True, timeout=25
            )
            if r.returncode == 0 and r.stdout.strip():
                fc_data = _json.loads(r.stdout)
                markdown = fc_data.get("data", {}).get("markdown", "")
                if markdown:
                    # 匹配 markdown 列表项: [Jul 14, 2026Product\Introducing Claude for Teachers](URL)
                    pattern = r'\[([A-Za-z]{3}\s+\d{1,2},\s*\d{4})([A-Za-z\s]+?)\\\\\n\s*([^\]]+)\]\(([^)]+)\)'
                    matches = re.findall(pattern, markdown)
                    for date_str, category, title, url in matches[:4]:  # 最多取 4 条
                        # 只保留最近 7 天的
                        try:
                            item_date = datetime.strptime(date_str.strip(), "%b %d, %Y")
                            if (datetime.now() - item_date).days > 7:
                                continue
                        except:
                            continue
                        results.append({
                            "title": title.strip()[:60],
                            "url": url.strip(),
                            "description": f"Anthropic {category.strip()}",
                            "metric": "Anthropic",
                            "source": "blog",
                            "source_id": None
                        })
        except Exception:
            pass
    
    for blog in blogs:
        try:
            # 使用较短超时，避免单个 feed 阻塞
            xml = curl_text(blog["url"], max_time=8)
            if not xml or len(xml) < 100:
                continue
            
            # 支持 RSS (<item>) 和 Atom (<entry>)
            items = re.findall(r'<item>(.*?)</item>', xml, re.DOTALL)
            if not items:
                items = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)
            
            for item in items[:2]:  # 每个博客取最近 2 条
                title = re.search(r'<title>(.*?)</title>', item, re.DOTALL)
                # Atom 用 link href，RSS 用 link
                link = re.search(r'<link href="(.*?)"', item, re.DOTALL)
                if not link:
                    link = re.search(r'<link>(.*?)</link>', item, re.DOTALL)
                pub_date = re.search(r'<pubDate>(.*?)</pubDate>', item, re.DOTALL)
                
                if title and link:
                    title_text = title.group(1).strip().replace('\n', ' ')
                    link_text = link.group(1).strip()
                    
                    # Atom 的 link 可能包含 rel="alternate"，提取纯 URL
                    if '"' in link_text:
                        url_match = re.search(r'href="(.*?)"', link_text)
                        if url_match:
                            link_text = url_match.group(1)
                    
                    # 只保留最近 7 天的
                    if pub_date:
                        try:
                            date_str = pub_date.group(1).strip()
                            item_date = datetime.strptime(date_str[:16], "%a, %d %b %Y")
                            if (datetime.now() - item_date).days > 7:
                                continue
                        except:
                            pass
                    
                    results.append({
                        "title": title_text[:60],
                        "url": link_text,
                        "description": f"{blog['name']} 官方发布",
                        "metric": blog["name"],
                        "source": "blog",
                        "source_id": None
                    })
        except Exception:
            continue
    
    return results[:max_items]


def collect_github_topics_agent(max_items):
    """从 GitHub Topics 采集 Agent 相关新仓库。"""
    topics = ["ai-agent", "multi-agent", "agent-framework", "agentic-ai", "llm-agent"]
    results = []
    seen = set()
    
    for topic in topics:
        if len(results) >= max_items:
            break
        
        data = curl_json(
            f"https://api.github.com/search/repositories?q=topic:{topic}+stars:>10+"
            f"pushed:>{(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}"
            f"&sort=updated&order=desc&per_page=5",
            max_time=15
        )
        
        if not data:
            continue
        
        for item in data.get("items", []):
            full_name = item.get("full_name", "")
            if full_name in seen:
                continue
            seen.add(full_name)
            
            desc = item.get("description", "") or ""
            if any(k in desc.lower() for k in ["wrapper", "demo", "tutorial"]):
                continue
            
            results.append({
                "title": full_name,
                "url": item.get("html_url", ""),
                "description": desc[:100] if desc else "无描述",
                "metric": f"{item.get('stargazers_count', 0)}⭐",
                "source": "github",
                "source_id": f"github:{full_name}"
            })
            
            if len(results) >= max_items:
                break
    
    return results


def collect_github(max_items):
    """从 GitHub Search API 采集。"""
    week_ago = os.popen("date -d '7 days ago' +%Y-%m-%d").read().strip()
    data = curl_json(
        f"https://api.github.com/search/repositories?q=created:>{week_ago}+stars:>50+topic:ai"
        f"&sort=stars&order=desc&per_page=10"
    )
    if not data:
        return []
    
    results = []
    for item in data.get("items", [])[:max_items]:
        desc = item.get("description", "") or ""
        if "wrapper" in desc.lower() or "demo" in desc.lower():
            continue
        results.append({
            "title": item.get("full_name", ""),
            "url": item.get("html_url", ""),
            "description": desc[:100] if desc else "无描述",
            "metric": f"{item.get('stargazers_count', 0)}⭐"
        })
    return results


def collect_producthunt(max_items):
    """从 Product Hunt GraphQL API 采集。"""
    ph_token = os.environ.get("PH_API_TOKEN", "")
    if not ph_token:
        return []
    
    try:
        query_json = json.dumps({"query": f"{{ {SECTIONS['producthunt']['query']} }}"})
        r = subprocess.run(
            ["curl", "-s", "--max-time", "15",
             "-X", "POST", "https://api.producthunt.com/v2/api/graphql",
             "-H", f"Authorization: Bearer {ph_token}",
             "-H", "Content-Type: application/json",
             "-d", query_json
            ],
            capture_output=True, text=True, timeout=20
        )
        data = json.loads(r.stdout) if r.stdout.strip() else {}
    except Exception:
        return []
    
    results = []
    for edge in data.get("data", {}).get("posts", {}).get("edges", [])[:max_items]:
        node = edge.get("node", {})
        tagline = node.get("tagline", "")
        if any(k in tagline.lower() for k in ["ai 搞钱", "ai 副业", "涨粉", "变现"]):
            continue
        results.append({
            "title": node.get("name", ""),
            "url": node.get("url", ""),
            "description": tagline[:100],
            "metric": f"{node.get('votesCount', 0)}票"
        })
    return results


def collect_hn_algolia_blogs(section, max_items):
    """从 HN Algolia + Simon Willison RSS 采集 Agent 工程。"""
    results = []
    
    # HN Algolia
    hn_data = curl_json(
        "https://hn.algolia.com/api/v1/search?query=agent+framework"
        "&tags=story&hitsPerPage=10",
        max_time=15
    )
    for hit in hn_data.get("hits", [])[:3] if hn_data else []:
        results.append({
            "title": hit.get("title", "")[:50],
            "url": hit.get("url", f"https://news.ycombinator.com/item?id={hit.get('objectID')}"),
            "description": f"HN Agent 工程: {hit.get('points', 0)} ⬆",
            "metric": f"{hit.get('points', 0)} ⬆"
        })
    
    # Simon Willison RSS
    xml = curl_text("https://simonwillison.net/atom/everything/", max_time=15)
    if xml:
        entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)
        for entry in entries[:2]:
            title = re.search(r'<title>(.*?)</title>', entry)
            link = re.search(r'<link href="(.*?)"', entry)
            if title and link:
                if any(k in title.group(1).lower() for k in ["agent", "loop", "claude", "prompt"]):
                    results.append({
                        "title": title.group(1)[:50],
                        "url": link.group(1),
                        "description": "Simon Willison: Agent 工程实践",
                        "metric": "博客"
                    })
    
    return results[:max_items]


def collect_twitter_timeline(max_items):
    """从 X/Twitter timeline 采集（GUI 环境专用）。"""
    cdp = os.environ.get("OPENCLI_CDP_ENDPOINT", "http://127.0.0.1:9222")
    try:
        r = subprocess.run(
            ["opencli", "web", "fetch", "https://x.com/home"],
            capture_output=True, text=True, env={**os.environ, "OPENCLI_CDP_ENDPOINT": cdp}
        )
        html = r.stdout
        if not html or len(html) < 1000:
            return []
        # 提取推文内容（基于 X 的 HTML 结构）
        tweets = re.findall(r'<article[^>]*>.*?<a[^>]*href="/([^/]+)/status/\d+"[^>]*>.*?<span[^>]*>(.*?)</span>', html, re.DOTALL)
        results = []
        for username, text in tweets[:max_items]:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            if clean_text and len(clean_text) > 10:
                results.append({
                    "title": clean_text[:100],
                    "url": f"https://x.com/{username}",
                    "description": f"X/Twitter: @{username}",
                    "metric": "X/Twitter"
                })
        return results
    except Exception:
        return []


def collect_twitter_search_agent(max_items):
    """从 X/Twitter search 采集 Agent 相关内容（GUI 环境专用）。"""
    cdp = os.environ.get("OPENCLI_CDP_ENDPOINT", "http://127.0.0.1:9222")
    try:
        r = subprocess.run(
            ["opencli", "web", "fetch", "https://x.com/search?q=agent+framework+AI"],
            capture_output=True, text=True, env={**os.environ, "OPENCLI_CDP_ENDPOINT": cdp}
        )
        html = r.stdout
        if not html or len(html) < 1000:
            return []
        tweets = re.findall(r'<article[^>]*>.*?<a[^>]*href="/([^/]+)/status/\d+"[^>]*>.*?<span[^>]*>(.*?)</span>', html, re.DOTALL)
        results = []
        for username, text in tweets[:max_items]:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            if clean_text and len(clean_text) > 10:
                results.append({
                    "title": clean_text[:100],
                    "url": f"https://x.com/{username}",
                    "description": f"X/Twitter Agent: @{username}",
                    "metric": "X/Twitter"
                })
        return results
    except Exception:
        return []


def collect_frontier(max_items):
    """从 arXiv + GitHub 采集前沿技术。"""
    results = []
    
    # arXiv
    xml = curl_text(
        "https://export.arxiv.org/api/query?"
        "search_query=all:agent+AND+(all:memory+OR+all:observability+OR+all:self-improvement)"
        "&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending",
        max_time=15
    )
    if xml:
        entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)
        for entry in entries[:3]:
            title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
            id_match = re.search(r'<id>(.*?)</id>', entry)
            summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
            if title and id_match:
                arxiv_id = id_match.group(1).split("/")[-1]
                results.append({
                    "title": title.group(1).strip().replace('\n', ' ')[:60],
                    "url": f"https://arxiv.org/pdf/{arxiv_id}",
                    "description": (summary.group(1).strip()[:150] if summary else ""),
                    "metric": "arXiv"
                })
    
    # GitHub
    week_ago = os.popen("date -d '7 days ago' +%Y-%m-%d").read().strip()
    gh_data = curl_json(
        f"https://api.github.com/search/repositories?q=created:>{week_ago}+stars:>5+"
        f"agent+memory+OR+observability+OR+self-improvement"
        f"&sort=stars&order=desc&per_page=5",
        max_time=15
    )
    if gh_data:
        for item in gh_data.get("items", [])[:2]:
            results.append({
                "title": item.get("full_name", ""),
                "url": item.get("html_url", ""),
                "description": (item.get("description", "") or "")[:100],
                "metric": f"{item.get('stargazers_count', 0)}⭐"
            })
    
    return results[:max_items]


# ── 主函数 ──

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", required=True, choices=list(SECTIONS.keys()), help="采集板块")
    parser.add_argument("--output", help="输出文件路径（默认：/tmp/ai-daily-briefing/<date>/<section>.json）")
    args = parser.parse_args()
    
    section = args.section
    config = SECTIONS[section]
    max_items = config["max"]
    
    # 判断环境并选择数据源
    from common import use_x_twitter
    
    if section == "industry":
        if use_x_twitter():
            # GUI 环境：使用 X/Twitter
            results = collect_twitter_timeline(max_items)
        else:
            # 无 GUI 环境：使用 HN + 官方博客
            results = collect_hn_topstories(section, max_items)
            if len(results) < 3:
                print(f"HN only got {len(results)} items, trying backup sources...")
                backup = collect_official_blogs(max_items - len(results))
                results += backup[:max_items - len(results)]
    
    elif section == "github":
        results = collect_github(max_items)
    
    elif section == "producthunt":
        results = collect_producthunt(max_items)
    
    elif section == "agent_eng":
        if use_x_twitter():
            # GUI 环境：使用 X/Twitter search
            results = collect_twitter_search_agent(max_items)
        else:
            # 无 GUI 环境：使用 HN + blogs + GitHub Topics
            results = collect_hn_algolia_blogs(section, max_items)
            if len(results) < 3:
                print(f"HN only got {len(results)} items, trying backup sources...")
                backup = collect_github_topics_agent(max_items - len(results))
                results += backup[:max_items - len(results)]
    
    elif section == "frontier":
        results = collect_frontier(max_items)
    
    else:
        results = []
    
    # 默认输出路径
    output_path = args.output or f"{DEFAULT_OUTPUT_DIR}/{section}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"Collected {len(results)} items for {section} -> {output_path}")


if __name__ == "__main__":
    main()
