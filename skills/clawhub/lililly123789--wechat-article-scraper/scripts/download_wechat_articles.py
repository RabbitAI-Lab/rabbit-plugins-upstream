#!/usr/bin/env python3
"""
Batch download WeChat (微信公众号) articles as Markdown with images.

Usage:
    python3 download_wechat_articles.py <urls_file> [--output-dir <dir>] [--min-image-size <bytes>] [--start-index <n>] [--retry <n>]

Arguments:
    urls_file          Text file with one WeChat article URL per line
    --output-dir       Output directory for markdown files (default: ./articles-md)
    --min-image-size   Minimum image size in bytes to keep (default: 6000)
                       Filters out decorative icons/UI elements
    --start-index      Starting article index for numbering (default: 1)
    --retry            Number of retries on failure (default: 3)

Output:
    articles-md/
    ├── 01-YYYY-MM-DD_Article_Title.md
    ├── 02-YYYY-MM-DD_Another_Title.md
    ├── ...
    └── images/
        ├── art01_img01.png
        ├── art01_img02.jpg
        └── ...

Requirements:
    pip install requests beautifulsoup4 lxml
"""

import os
import re
import sys
import json
import time
import datetime
import argparse
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def sanitize_filename(name):
    """Remove invalid characters from filename, truncate to 80 chars."""
    name = re.sub(r'[\\/:*?"<>|\n\r\t]', '_', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:80]


def extract_publish_date(html, title=""):
    """
    Extract publish date from WeChat article HTML using multiple strategies.

    WeChat renders dates via JavaScript, so the <em id="publish_time"> element
    is empty in raw HTML. However, the article's creation timestamp is embedded
    in JavaScript variables within the page source.

    Strategies (in order of reliability):
    1. var ct = "unix_timestamp"        -- primary, most reliable
    2. var oriCreateTime = "timestamp"  -- fallback
    3. create_time = "YYYY-MM-DD"       -- fallback (sometimes present)
    4. <em id="publish_time"> text      -- fallback (rarely populated)
    5. Date pattern in article title    -- last resort (e.g., "26.8.1周记")

    Returns:
        str: Date in "YYYY-MM-DD" format, or "unknown-date" if all strategies fail.
    """
    # Strategy 1: var ct = "1757330462" (Unix timestamp)
    ct_match = re.findall(r'var\s+ct\s*=\s*["\'](\d{10})["\']', html)
    if ct_match:
        try:
            dt = datetime.datetime.fromtimestamp(int(ct_match[0]))
            return dt.strftime("%Y-%m-%d")
        except (ValueError, OSError):
            pass

    # Strategy 2: oriCreateTime = "1757330462"
    ori_match = re.findall(r'oriCreateTime\s*=\s*["\'](\d{10})["\']', html)
    if ori_match:
        try:
            dt = datetime.datetime.fromtimestamp(int(ori_match[0]))
            return dt.strftime("%Y-%m-%d")
        except (ValueError, OSError):
            pass

    # Strategy 3: create_time = "2025-09-08"
    ct_date = re.findall(r'create_time\s*=\s*["\'](\d{4}-\d{2}-\d{2})["\']', html)
    if ct_date:
        return ct_date[0]

    # Strategy 4: <em id="publish_time">2026年8月3日</em>
    # (rarely populated in raw HTML, but check just in case)
    soup = BeautifulSoup(html, "lxml")
    date_tag = soup.find("em", id="publish_time")
    if date_tag:
        date_text = date_tag.get_text(strip=True)
        m = re.match(r"(\d{4})年(\d{1,2})月(\d{1,2})日", date_text)
        if m:
            return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"

    # Strategy 5: Extract date from title
    # Common patterns: "26.8.1周记", "2026-08-03", "8月3日", etc.
    if title:
        # Pattern: YY.M.D (e.g., "26.8.1" -> 2026-08-01)
        m = re.search(r'(\d{2})\.(\d{1,2})\.(\d{1,2})', title)
        if m:
            year = 2000 + int(m.group(1))
            return f"{year}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"

        # Pattern: YYYY-MM-DD
        m = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', title)
        if m:
            return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"

        # Pattern: YYYY年M月D日
        m = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', title)
        if m:
            return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"

    return "unknown-date"


def is_long_format_url(url):
    """
    Check if URL is in long format (with __biz parameter).

    Long format URLs (mp.weixin.qq.com/s?__biz=...&mid=...&sn=...) trigger
    WeChat's anti-scraping CAPTCHA when accessed via HTTP requests.
    Short format URLs (mp.weixin.qq.com/s/xxxxx) work reliably.

    Returns:
        bool: True if URL is in long format.
    """
    return "__biz=" in url or "mid=" in url


def download_image(url, save_path, headers, min_size=1000):
    """Download an image if it meets minimum size requirement."""
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200 and len(resp.content) >= min_size:
            with open(save_path, "wb") as f:
                f.write(resp.content)
            return True
    except Exception as e:
        print(f"  [WARN] Image download failed: {e}")
    return False


def extract_image_extension(url, content_type=""):
    """
    Determine image file extension from URL or Content-Type header.

    Args:
        url: Image URL
        content_type: Optional Content-Type header value

    Returns:
        str: File extension including dot (e.g., ".png", ".jpg")
    """
    # Try Content-Type header first (most reliable)
    if content_type:
        ct = content_type.lower()
        if "png" in ct:
            return ".png"
        if "gif" in ct:
            return ".gif"
        if "webp" in ct:
            return ".webp"
        if "jpeg" in ct or "jpg" in ct:
            return ".jpg"

    # Fall back to URL path analysis
    # Parse the URL path and look for file extension
    from urllib.parse import urlparse
    path = urlparse(url).path.lower()
    for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"]:
        if path.endswith(ext):
            return ext

    # Last resort: check if extension appears anywhere in URL
    url_lower = url.lower()
    if ".png" in url_lower:
        return ".png"
    if ".gif" in url_lower:
        return ".gif"
    if ".webp" in url_lower:
        return ".webp"
    if ".jpeg" in url_lower or ".jpg" in url_lower:
        return ".jpg"

    return ".jpg"  # default


def fetch_with_retry(url, headers, max_retries=3, delay=2):
    """
    Fetch URL with exponential backoff retry.

    Args:
        url: URL to fetch
        headers: HTTP headers
        max_retries: Maximum number of retry attempts
        delay: Base delay between retries (exponential backoff)

    Returns:
        Response object if successful, None if all retries fail.
    """
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            resp.encoding = "utf-8"

            # Check for CAPTCHA / verification page
            if "captcha" in resp.text.lower() or "环境异常" in resp.text:
                print(f"  [WARN] CAPTCHA/verification detected (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    wait = delay * (2 ** attempt)
                    print(f"  Retrying in {wait}s...")
                    time.sleep(wait)
                    continue

            if resp.status_code == 200:
                return resp

            print(f"  [WARN] HTTP {resp.status_code} (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))

        except requests.RequestException as e:
            print(f"  [WARN] Request failed: {e} (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))

    return None


def extract_article(html, article_idx, source_url, images_dir, min_image_size):
    """
    Extract title, date, author, and content with images from WeChat article HTML.

    Returns dict with article metadata and markdown content, or None if extraction fails.
    """
    soup = BeautifulSoup(html, "lxml")

    # Title
    title_tag = soup.find("h1", id="activity-name") or soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else f"Article_{article_idx}"
    title = sanitize_filename(title)

    # Author / Account name
    account_tag = soup.find("a", id="js_name")
    account_name = account_tag.get_text(strip=True) if account_tag else ""

    # Publish date -- use multi-strategy extraction
    publish_date = extract_publish_date(html, title)

    # Content area
    content_div = soup.find("div", id="js_content") or soup.find("div", class_="rich_media_content")
    if not content_div:
        print("  [WARN] No content div found")
        return None

    # Phase 1: Download all images, build URL -> filename mapping
    img_map = {}  # url -> filename
    img_counter = 0
    all_imgs = content_div.find_all("img")

    for img_tag in all_imgs:
        img_url = img_tag.get("data-src") or img_tag.get("src", "")
        if not img_url or not img_url.startswith("http"):
            continue
        if img_url in img_map:
            continue

        img_counter += 1

        # Determine extension from both URL and Content-Type
        ext = extract_image_extension(img_url)
        img_filename = f"art{article_idx:02d}_img{img_counter:02d}{ext}"
        img_path = os.path.join(images_dir, img_filename)

        if not os.path.exists(img_path):
            if download_image(img_url, img_path, HEADERS, min_size=1000):
                actual_size = os.path.getsize(img_path)
                if actual_size < min_image_size:
                    os.remove(img_path)
                    print(f"  [SKIP] {img_filename} too small ({actual_size} bytes)")
                    continue

                # Re-check extension from Content-Type and rename if needed
                try:
                    resp_head = requests.head(img_url, headers=HEADERS, timeout=10)
                    ct = resp_head.headers.get("Content-Type", "")
                    correct_ext = extract_image_extension(img_url, ct)
                    if correct_ext != ext:
                        new_filename = f"art{article_idx:02d}_img{img_counter:02d}{correct_ext}"
                        new_path = os.path.join(images_dir, new_filename)
                        os.rename(img_path, new_path)
                        img_filename = new_filename
                        img_path = new_path
                except Exception:
                    pass  # Keep original extension if HEAD fails

                print(f"  [OK] {img_filename} ({actual_size} bytes)")
            else:
                continue

        img_map[img_url] = img_filename

    # Phase 2: Build markdown content, preserving text/image order
    content_parts = []

    def process_element(element):
        """Recursively process elements to maintain text/image order."""
        for child in element.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    content_parts.append(text)
            elif child.name == "img":
                img_url = child.get("data-src") or child.get("src", "")
                if img_url and img_url in img_map:
                    content_parts.append(f"\n\n![图片](images/{img_map[img_url]})\n")
            elif child.name in ("p", "div", "section", "span", "strong", "b", "em", "i"):
                process_element(child)
            elif child.name == "br":
                content_parts.append("\n")
            elif child.name in ("h1", "h2", "h3", "h4"):
                text = child.get_text(strip=True)
                if text:
                    level = int(child.name[1])
                    content_parts.append(f"\n\n{'#' * level} {text}\n")
            elif child.name == "li":
                text = child.get_text(strip=True)
                if text:
                    content_parts.append(f"\n- {text}")
            elif child.name == "table":
                rows = child.find_all("tr")
                if rows:
                    for i, row in enumerate(rows):
                        cells = row.find_all(["td", "th"])
                        cell_texts = [c.get_text(strip=True) for c in cells]
                        if cell_texts:
                            content_parts.append("| " + " | ".join(cell_texts) + " |")
                            if i == 0:
                                content_parts.append("| " + " | ".join(["---"] * len(cell_texts)) + " |")
                    content_parts.append("\n")
                else:
                    content_parts.append("\n[表格内容见原文]\n")
            else:
                text = child.get_text(strip=True)
                if text:
                    content_parts.append(text)

    process_element(content_div)

    # Build final markdown
    date_str = publish_date
    md_content = f"""---
source_index: {article_idx}
source_url: {source_url}
title: "{title}"
author: "{account_name}"
publish_date: "{date_str}"
---

# {title}

**公众号**: {account_name}
**发布时间**: {date_str}

---

"""
    body = "\n".join(content_parts)
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    md_content += body + "\n"

    return {
        "title": title,
        "account_name": account_name,
        "publish_date": date_str,
        "md_content": md_content,
        "img_count": len(img_map),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Batch download WeChat articles as Markdown with images"
    )
    parser.add_argument(
        "urls_file",
        help="Text file with one WeChat article URL per line",
    )
    parser.add_argument(
        "--output-dir",
        default="./articles-md",
        help="Output directory (default: ./articles-md)",
    )
    parser.add_argument(
        "--min-image-size",
        type=int,
        default=6000,
        help="Minimum image size in bytes to keep (default: 6000)",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=1,
        help="Starting article index for numbering (default: 1)",
    )
    parser.add_argument(
        "--retry",
        type=int,
        default=3,
        help="Number of retries on failure (default: 3)",
    )
    args = parser.parse_args()

    # Read URLs
    with open(args.urls_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and line.strip().startswith("http")]

    if not urls:
        print("No valid URLs found in file.")
        sys.exit(1)

    # Warn about long-format URLs
    long_urls = [u for u in urls if is_long_format_url(u)]
    if long_urls:
        print(f"[WARNING] {len(long_urls)} URL(s) use long format (__biz parameter).")
        print("  Long format URLs may trigger WeChat's CAPTCHA and fail to download.")
        print("  If they fail, try converting them to short format (mp.weixin.qq.com/s/xxxxx).")
        print()

    print(f"Found {len(urls)} URLs to download.\n")

    # Create output directories
    output_dir = args.output_dir
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    results = []
    failed = []

    for i, url in enumerate(urls):
        idx = args.start_index + i
        print(f"{'=' * 60}")
        print(f"[{idx}] ({i + 1}/{len(urls)}) {url}")
        print(f"{'=' * 60}")

        # Fetch with retry
        resp = fetch_with_retry(url, HEADERS, max_retries=args.retry)
        if not resp:
            print(f"  [ERROR] Failed after {args.retry} retries")
            failed.append({"idx": idx, "url": url, "reason": "fetch_failed"})
            continue

        # Check for CAPTCHA
        if "captcha" in resp.text.lower() or "环境异常" in resp.text:
            print(f"  [ERROR] CAPTCHA detected, cannot bypass programmatically")
            failed.append({"idx": idx, "url": url, "reason": "captcha"})
            continue

        result = extract_article(resp.text, idx, url, images_dir, args.min_image_size)
        if not result:
            print(f"  [ERROR] Failed to extract content")
            failed.append({"idx": idx, "url": url, "reason": "extraction_failed"})
            continue

        # Generate filename: NN-YYYY-MM-DD_Title.md
        date_str = result["publish_date"]
        filename = f"{idx:02d}-{date_str}_{sanitize_filename(result['title'])}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result["md_content"])

        date_display = date_str if date_str != "unknown-date" else "unknown-date (check manually)"
        print(f"\n  [SAVED] {filename}")
        print(f"  [DATE]  {date_display}")
        print(f"  [IMAGES] {result['img_count']} content images")

        results.append({
            "idx": idx,
            "title": result["title"],
            "date": date_str,
            "filename": filename,
            "images": result["img_count"],
            "url": url,
        })

        time.sleep(2)  # Rate limit

    # Save manifest
    manifest_path = os.path.join(output_dir, "manifest.json")
    manifest_data = {"articles": results, "failed": failed}
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    total_images = sum(r["images"] for r in results)
    print(f"\n{'=' * 60}")
    print(f"DONE! {len(results)}/{len(urls)} articles saved.")
    print(f"Total content images: {total_images}")
    if failed:
        print(f"Failed: {len(failed)} articles (see manifest.json for details)")
    print(f"Output: {output_dir}")
    print(f"Images: {images_dir}")
    print(f"Manifest: {manifest_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
