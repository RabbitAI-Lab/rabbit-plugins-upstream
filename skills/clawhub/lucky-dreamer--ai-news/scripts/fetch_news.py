#!/usr/bin/env python3
"""Fetch and extract AI news articles from ai.codefather.cn/news.

Standard-library only. No credentials, no third-party packages.

Outputs (in --out, default ./ai-news-output):
  articles-<date>.json       structured articles with full text
  digest-input-<date>.md     all articles in one readable file
  batch-01.md, batch-02.md   chunks sized for sequential reading
  meta.json                  target date, fetch time, counts, errors
"""

from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

DEFAULT_BASE_URL = "https://ai.codefather.cn"
NEWS_PATH = "/news"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
CHINA_TZ = timezone(timedelta(hours=8))
# The site uses Twitter-style snowflake IDs (verified against its list pages).
SNOWFLAKE_EPOCH_MS = 1288834974657
PAGE_SIZE = 20

RSC_ITEM_RE = re.compile(
    r'\\"href\\":\\"/news/(\d+)\\",.*?'
    r'\\"h4\\",null,\{\\"className\\":\\"font-semibold text-base text-slate-900\\",'
    r'\\"children\\":\\"(.*?)\\"\}.*?'
    r'\\"p\\",null,\{\\"className\\":\\"mt-1 line-clamp-3 text-sm text-slate-600\\",'
    r'\\"children\\":\\"(.*?)\\"\}',
    re.S,
)
PLAIN_ITEM_RE = re.compile(
    r'href="/news/(\d+)".*?<h4[^>]*>(.*?)</h4>.*?<p[^>]*>(.*?)</p>',
    re.S,
)
NOISE_LINE_RE = re.compile(
    r"^(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}|阅读 \d+|\+ 关注|"
    r"(?:编程导航|机器之心|量子位|新智元|36氪|智东西|AI前线|极客公园|"
    r"财联社|新浪科技|澎湃新闻|TechCrunch)"
    r"(?:\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2})?)$"
)


def enable_utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def clean_rsc_text(text: str) -> str:
    """Undo the double JSON escaping used by the Next.js RSC payload."""
    text = text.replace('\\\\\\"', '"')
    text = text.replace('\\"', '"')
    text = text.replace("\\\\", "\\")
    return html.unescape(text).strip()


def snowflake_datetime(article_id: str) -> datetime:
    ms = (int(article_id) >> 22) + SNOWFLAKE_EPOCH_MS
    return datetime.fromtimestamp(ms / 1000, tz=CHINA_TZ)


def http_get(url: str, timeout: int = 40, retries: int = 3) -> str:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": DEFAULT_BASE_URL + NEWS_PATH,
    }
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, "ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < retries - 1:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def parse_list_items(page_html: str) -> list[dict]:
    items: list[dict] = []
    for match in RSC_ITEM_RE.finditer(page_html):
        items.append(
            {
                "id": match.group(1),
                "title": clean_rsc_text(match.group(2)),
                "snippet": clean_rsc_text(match.group(3)),
            }
        )
    if not items:
        for match in PLAIN_ITEM_RE.finditer(page_html):
            items.append(
                {
                    "id": match.group(1),
                    "title": html.unescape(re.sub(r"<[^>]+>", "", match.group(2))).strip(),
                    "snippet": html.unescape(re.sub(r"<[^>]+>", "", match.group(3))).strip(),
                }
            )
    return items


def list_page_url(base_url: str, page: int) -> str:
    if page == 1:
        return base_url + NEWS_PATH
    return f"{base_url}{NEWS_PATH}?current={page}"


def collect_items(
    base_url: str, target_date: str | None, max_pages: int
) -> tuple[str, list[dict], str | None]:
    """Walk list pages until the target date's articles are exhausted.

    Returns (target_date, items_for_target, latest_available_date).
    """
    collected: list[dict] = []
    seen: set[str] = set()
    target = target_date
    latest_seen: str | None = None
    for page in range(1, max_pages + 1):
        page_html = http_get(list_page_url(base_url, page))
        page_items = parse_list_items(page_html)
        if not page_items:
            break
        older_seen = False
        for item in page_items:
            date_str = snowflake_datetime(item["id"]).strftime("%Y-%m-%d")
            if latest_seen is None:
                latest_seen = date_str
            if target is None:
                target = date_str
            item["date"] = date_str
            if date_str == target and item["id"] not in seen:
                seen.add(item["id"])
                collected.append(item)
            elif date_str < target:
                older_seen = True
        if older_seen:
            break
    if target is None:
        raise RuntimeError("Could not determine a news date from the listing page.")
    return target, collected, latest_seen


def extract_article(page_html: str, title: str = "") -> tuple[str, str, str]:
    """Return (content, original_url, published_text)."""
    article_match = re.search(r"<article[^>]*>(.*?)</article>", page_html, re.S)
    body = article_match.group(1) if article_match else page_html

    original_url = ""
    link_match = re.search(r'原文链接：\s*<a href="([^"]+)"', body, re.S)
    if link_match:
        original_url = html.unescape(link_match.group(1))

    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
    body = re.sub(r"<img[^>]*>", "\n", body)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</(p|div|h[1-6]|li|tr|section|blockquote|td|th)>", "\n", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)

    raw_lines = [line.strip() for line in body.split("\n")]
    published_text = ""
    for line in raw_lines:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", line):
            published_text = line
            break

    lines: list[str] = []
    for line in raw_lines:
        if not line or NOISE_LINE_RE.match(line):
            continue
        if lines and lines[-1] == line:
            continue
        lines.append(line)
    text = "\n".join(lines)

    if title and lines:
        normalized_title = re.sub(r"\s+", "", title)
        normalized_first = re.sub(r"\s+", "", lines[0])
        if normalized_first == normalized_title:
            text = "\n".join(lines[1:])

    cut = text.rfind("原文链接：")
    if cut > len(text) * 0.5:
        text = text[:cut].rstrip()

    if len(text) < 80:
        meta_match = re.search(
            r'<meta name="description" content="([^"]*)"', page_html, re.S
        )
        if meta_match:
            text = html.unescape(meta_match.group(1)).strip()

    return text, original_url, published_text


def fetch_article(base_url: str, item: dict) -> dict:
    url = f"{base_url}{NEWS_PATH}/{item['id']}"
    page_html = http_get(url)
    content, original_url, published_text = extract_article(page_html, item["title"])
    published_at = snowflake_datetime(item["id"])
    if published_text:
        try:
            published_at = datetime.strptime(published_text, "%Y-%m-%d %H:%M").replace(
                tzinfo=CHINA_TZ
            )
        except ValueError:
            pass
    return {
        "id": item["id"],
        "title": item["title"],
        "published_at": published_at.isoformat(timespec="minutes"),
        "date": published_at.strftime("%Y-%m-%d"),
        "url": url,
        "original_url": original_url,
        "source_domain": urllib.parse.urlparse(original_url).netloc if original_url else "",
        "snippet": item.get("snippet", ""),
        "content": content,
        "content_chars": len(content),
    }


def article_block(index: int, article: dict) -> str:
    lines = [
        f"===== ARTICLE {index} | {article['id']} | {article['published_at']} | {article['title']}",
        f"site: {article['url']}",
    ]
    if article["original_url"]:
        lines.append(f"original: {article['original_url']}")
    lines.append("")
    lines.append(article["content"])
    lines.append("")
    return "\n".join(lines)


def write_batches(out_dir: Path, date_str: str, articles: list[dict], batch_chars: int) -> int:
    batches: list[list[str]] = []
    current: list[str] = []
    current_chars = 0
    for index, article in enumerate(articles, start=1):
        block = article_block(index, article)
        if current and current_chars + len(block) > batch_chars:
            batches.append(current)
            current = []
            current_chars = 0
        current.append(block)
        current_chars += len(block)
    if current:
        batches.append(current)

    for number, blocks in enumerate(batches, start=1):
        path = out_dir / f"batch-{number:02d}.md"
        header = f"# AI news input — {date_str} — batch {number}/{len(batches)}\n\n"
        path.write_text(header + "\n".join(blocks), encoding="utf-8")
    return len(batches)


def main() -> int:
    enable_utf8_stdout()
    parser = argparse.ArgumentParser(description="Fetch AI news from ai.codefather.cn")
    parser.add_argument("--date", help="Target date in China time, YYYY-MM-DD (default: latest)")
    parser.add_argument("--out", help="Output directory (default: ./ai-news-output)")
    parser.add_argument("--max-pages", type=int, default=15, help="Pagination safety limit")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent detail fetches")
    parser.add_argument("--batch-chars", type=int, default=9000, help="Approx chars per batch")
    parser.add_argument("--max-articles", type=int, default=0, help="0 = no cap")
    parser.add_argument("--timeout", type=int, default=40, help="Per-request timeout in seconds")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Alternate base URL")
    args = parser.parse_args()

    if args.date:
        try:
            datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid --date {args.date!r}; expected YYYY-MM-DD.", file=sys.stderr)
            return 2

    base_url = args.base_url.rstrip("/")
    out_dir = Path(args.out) if args.out else Path.cwd() / "ai-news-output"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        target_date, items, latest_available = collect_items(base_url, args.date, args.max_pages)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not items:
        print(
            f"No articles found for {args.date or target_date}. "
            f"Latest available date on the site: {latest_available}. "
            "Try without --date to use the latest available date.",
            file=sys.stderr,
        )
        return 1

    matched_count = len(items)
    if args.max_articles and len(items) > args.max_articles:
        items = items[: args.max_articles]

    articles: list[dict] = []
    errors: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(fetch_article, base_url, item): item for item in items
        }
        for future in concurrent.futures.as_completed(futures):
            item = futures[future]
            try:
                article = future.result()
                if article["date"] == target_date:
                    articles.append(article)
                else:
                    errors.append(
                        {
                            "id": item["id"],
                            "title": item["title"],
                            "error": f"detail date {article['date']} != target {target_date}",
                        }
                    )
            except Exception as exc:
                errors.append({"id": item["id"], "title": item["title"], "error": str(exc)})

    order = {item["id"]: index for index, item in enumerate(items)}
    articles.sort(key=lambda a: order.get(a["id"], 10**9))

    if not articles:
        print("ERROR: article pages were fetched but no article matched the target date.", file=sys.stderr)
        return 1

    json_path = out_dir / f"articles-{target_date}.json"
    json_path.write_text(json.dumps(articles, ensure_ascii=False, indent=2), encoding="utf-8")

    digest_input = "# AI news input — " + target_date + "\n\n"
    digest_input += "".join(article_block(i, a) for i, a in enumerate(articles, start=1))
    (out_dir / f"digest-input-{target_date}.md").write_text(digest_input, encoding="utf-8")

    batch_count = write_batches(out_dir, target_date, articles, max(1000, args.batch_chars))

    meta = {
        "source": base_url + NEWS_PATH,
        "target_date": target_date,
        "requested_date": args.date,
        "latest_available_date": latest_available,
        "fetched_at": datetime.now(CHINA_TZ).isoformat(timespec="seconds"),
        "timezone": "UTC+8 (China Standard Time)",
        "matched_article_count": matched_count,
        "article_count": len(articles),
        "truncated": matched_count != len(articles),
        "batches": batch_count,
        "errors": errors,
        "note": "Merge same-event reports before counting distinct stories.",
    }
    (out_dir / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    total_chars = sum(a["content_chars"] for a in articles)
    print(f"Date: {target_date} (latest available: {latest_available})")
    print(f"Articles: {len(articles)} of {matched_count} matched (content chars: {total_chars})")
    if matched_count != len(articles):
        print("Note: --max-articles truncated this run; the digest is a sample, not the full day.")
    print(f"Batches: {batch_count}")
    if errors:
        print(f"Warnings: {len(errors)} article(s) skipped or mismatched (see meta.json)")
    print(f"Output: {out_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
