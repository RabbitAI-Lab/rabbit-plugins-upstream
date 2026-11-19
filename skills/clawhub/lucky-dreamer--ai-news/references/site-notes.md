# Site Notes — ai.codefather.cn/news

Technical notes for maintaining the scraper. Read this when `fetch_news.py` breaks or the site changes.

## Page shape

- Next.js server-rendered app. The list page's article data is embedded in `self.__next_f.push(...)` RSC payloads as **JSON-escaped JSON** (quotes appear as `\"` in the raw HTML). Titles containing quotes can appear triple-escaped (`\\\"`), which is why `clean_rsc_text()` unwraps in stages.
- Article links are `/news/<snowflake-id>`. Detail pages contain the full article inside `<article> ... </article>`, followed by an `<aside aria-label="相关推荐">` block that the extractor ignores.
- Each detail page ends with `原文链接：<a href="...">`, which is the original publisher (AIbase, WeChat公众号, TechCrunch, etc.).
- The list page shows the first 20 items. Pagination is `?current=N` (1-based). `?page=N` is ignored.
- Date filtering is `?date=YYYY-MM-DD`, but the visible date headers (`10月23日 · 周五`) render only on the unfiltered first page, and the filter alone still paginates. The scraper therefore walks pages and groups by article timestamps.

## Article timestamps

Article IDs are Twitter-style snowflakes: `published_ms = (id >> 22) + 1288834974657`. This was verified against the site's own displayed timestamps on 2026-10-23. Detail pages also show `YYYY-MM-DD HH:MM`; the scraper prefers that value when present and falls back to the decoded ID.

The site's dates are **China Standard Time (UTC+8)**. Publishing appears to happen in two daily batches, roughly 12:30 and 23:50 China time.

## Known quirks

- **Listing lag:** the newest date on the site may be yesterday even when today is underway. The default (no `--date`) picks the date of the first listing item, which is the latest date that actually has articles.
- **More than 20 articles per day:** page 1 can contain only the latest date and still have more on page 2. The scraper keeps walking until it sees an item older than the target date.
- **Duplicate stories:** the same event is often carried by multiple original publishers with different titles and numbers. Deduplicate by event in the digest, not by exact title match.
- **Missing bodies:** a small number of articles only have a short body or a meta description. The extractor falls back to `<meta name="description">` when the extracted text is under 80 characters.
- **Images:** image URLs are embedded as `<img>` tags; the scraper drops them and keeps the surrounding paragraphs. Summaries should not claim to have seen an image.

## If the parser breaks

1. Save one list page and one detail page to disk.
2. Check whether the RSC payload still uses `\"href\":\"/news/<id>\"` and the `h4`/`p` class names in `RSC_ITEM_RE`.
3. Check whether detail pages still wrap the article in `<article>` and keep `原文链接：<a href=...>`.
4. Prefer updating the regexes in `scripts/fetch_news.py`; do not add a third-party HTML parser unless the page becomes real DOM rather than RSC payloads.
