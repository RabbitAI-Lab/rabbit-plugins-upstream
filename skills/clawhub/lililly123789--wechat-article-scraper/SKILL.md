---
name: wechat-article-scraper
slug: wechat-article-scraper
version: 1.1.1
displayName: WeChat Article Scraper
description: "Batch download WeChat (微信公众号) articles as Markdown files with embedded images. Triggers: 下载公众号文章, 批量抓取微信文章, 保存公众号内容, download wechat articles, scrape wechat posts, save articles with images."
summary: "Batch download WeChat articles as Markdown with images. Smart date extraction, decorative image filtering, retry logic."
tags: [wechat, scraper, markdown, articles, 公众号]
license: MIT-0
homepage: https://github.com/lililly123789/wechat-article-scraper
agent_created: true
---

# WeChat Article Scraper

## Overview

Batch download WeChat (微信公众号) articles from `mp.weixin.qq.com` URLs, saving each article as a properly formatted Markdown file with all content images downloaded locally and referenced via correct relative paths (`images/artXX_imgXX.png`).

## When to Use

- User provides one or more `mp.weixin.qq.com` URLs and wants the full article content saved
- User wants to batch download a series of WeChat articles for offline reading, analysis, or archiving
- User wants to extract text AND images from WeChat articles (WebFetch alone only gets text, no images)

## Workflow

### Step 1: Prepare URL List

Collect all article URLs from the user. Create a text file with one URL per line:

```
https://mp.weixin.qq.com/s/xxxxx
https://mp.weixin.qq.com/s/yyyyy
https://mp.weixin.qq.com/s/zzzzz
```

**Important**: Only short-format URLs (`mp.weixin.qq.com/s/xxxxx`) work reliably. Long-format URLs (`mp.weixin.qq.com/s?__biz=...&mid=...&sn=...`) trigger WeChat's CAPTCHA and will fail. If the user provides long-format URLs, ask them to find the short-format versions instead.

### Step 2: Ensure Dependencies

The script requires `requests`, `beautifulsoup4`, and `lxml`. Install into the managed venv:

```bash
# Install packages (adjust path to match your environment)
<python-path> -m pip install requests beautifulsoup4 lxml
```

### Step 3: Run the Download Script

Execute the bundled script:

```bash
<python-path> <skill-dir>/scripts/download_wechat_articles.py urls.txt \
  --output-dir ./articles-md \
  --min-image-size 6000
```

**Parameters:**
- `urls_file`: Text file with one WeChat URL per line (required)
- `--output-dir`: Output directory for markdown files (default: `./articles-md`)
- `--min-image-size`: Minimum image size in bytes to keep (default: `6000`). WeChat articles contain many small decorative icons (3-5KB) that are useless; real content images (charts, tables, screenshots) are typically 10KB+.
- `--start-index`: Starting article number for file naming (default: `1`). Use when downloading additional batches to avoid filename conflicts.
- `--retry`: Number of retries on failure (default: `3`). Uses exponential backoff.

### Step 4: Verify Results

After download, check:

1. All files have proper dates (not `unknown-date`)
2. Image paths include `images/` prefix
3. No broken image references

Quick check command:
```bash
# List articles and their image counts
for f in articles-md/*.md; do
  count=$(grep -c '!\[图片\]' "$f")
  echo "${count}张  $(basename "$f")"
done

# Check for any unknown-date files
ls articles-md/*unknown-date* 2>/dev/null
```

If any files have `unknown-date`, the date extraction failed (rare). Check the article content for date clues and rename manually.

## Output Structure

```
articles-md/
├── 01-2026-08-03_Article_Title.md
├── 02-2026-08-01_Another_Title.md
├── ...
├── images/
│   ├── art01_img01.png    (16KB - content chart)
│   ├── art01_img02.jpg    (31KB - screenshot)
│   └── ...
└── manifest.json          # metadata for all downloaded articles
```

The `manifest.json` contains:
```json
{
  "articles": [
    {"idx": 1, "title": "...", "date": "2026-08-03", "filename": "...", "images": 2, "url": "..."}
  ],
  "failed": [
    {"idx": 5, "url": "...", "reason": "captcha"}
  ]
}
```

## Key Technical Notes

### Date Extraction (Solved)

WeChat renders publish dates via JavaScript, so the `<em id="publish_time">` element is empty in raw HTML. The script uses a multi-strategy approach to extract the date:

1. **`var ct = "unix_timestamp"`** — Primary method. WeChat embeds the article's creation time as a Unix timestamp in a JS variable. This is the most reliable source.
2. **`oriCreateTime = "timestamp"`** — Fallback.
3. **`create_time = "YYYY-MM-DD"`** — Fallback (sometimes present in page scripts).
4. **`<em id="publish_time">` text** — Rarely populated in raw HTML, but checked as a fallback.
5. **Title pattern matching** — Last resort. Extracts dates from titles like "26.8.1周记" → 2026-08-01.

### Image Extraction
- WeChat uses lazy-loading: image URLs are in the `data-src` attribute, not `src`
- Always check `data-src` first, fall back to `src`
- Image extension is determined from both URL pattern and Content-Type header

### Content Structure
- Article body is in `<div id="js_content">` or `<div class="rich_media_content">`
- Title is in `<h1 id="activity-name">`
- Account name is in `<a id="js_name">`
- Content uses nested `<section>`, `<p>`, `<span>` tags heavily — recursive traversal preserves reading order

### Decorative Image Filtering
WeChat articles embed many small UI elements as images:
- Account QR codes (~5KB)
- "Subscribe" buttons (~4KB)
- Decorative dividers (~3KB)
- Emoji/stickers (~2-5KB)

Setting `--min-image-size 6000` filters most of these. Real content images (charts, data tables, screenshots) are typically 10KB+.

### Rate Limiting
The script includes a 2-second delay between article fetches to avoid being rate-limited by WeChat servers. Do not remove this delay.

### Retry Mechanism
Failed downloads automatically retry with exponential backoff (2s, 4s, 8s). The `--retry` parameter controls the number of attempts.

## Limitations

1. **Long-format URLs blocked**: URLs with `__biz=` parameter trigger CAPTCHA. Only short URLs (`/s/xxxxx`) work.
2. **No comments**: Article comments are not extracted.
3. **No embedded videos/GIFs**: Only static images are downloaded.
4. **Temporary URLs**: Some WeChat article URLs expire after a period. Download promptly after receiving them.

## Resources

### scripts/
- `download_wechat_articles.py` — Main batch download script. Accepts a URL list file and output directory, handles image downloading with size filtering, generates properly formatted Markdown with correct image paths. Supports retry logic and multi-strategy date extraction.

### requirements.txt
- `requests` — HTTP client for fetching articles and images
- `beautifulsoup4` — HTML parsing
- `lxml` — Fast XML/HTML parser backend for BeautifulSoup
