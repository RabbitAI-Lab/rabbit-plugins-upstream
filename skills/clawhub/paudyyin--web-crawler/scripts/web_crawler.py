#!/usr/bin/env python3
"""
web_crawler.py - Unified web crawling tool.

Subcommands:
  fetch  - Single page fetch with JS rendering (SPA support, CSS selectors, custom JS)
  crawl  - BFS site-wide crawl with checkpoint/resume

Usage:
  python web_crawler.py fetch <url> [options]
  python web_crawler.py crawl <url> [options]
"""

import argparse
import asyncio
import sys


def cmd_fetch(args):
    """Execute single page fetch."""
    from web_fetch_enhanced import WebFetchEnhanced
    from pathlib import Path
    import json

    fetcher = WebFetchEnhanced()

    try:
        result = fetcher.fetch(
            url=args.url,
            wait_until=args.wait,
            timeout=args.timeout,
            selector=args.selector,
            remove_selector=args.remove_selector,
            js=args.js,
            use_playwright=not args.no_playwright if args.no_playwright else None,
        )

        if args.json:
            output = json.dumps(
                {
                    "url": args.url,
                    "content": result,
                    "length": len(result),
                    "mode": "requests" if args.no_playwright else "playwright",
                },
                ensure_ascii=False,
                indent=2,
            )
        else:
            output = result

        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Saved to {args.output}", file=sys.stderr)
        else:
            print(output)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


async def cmd_crawl(args):
    """Execute BFS site crawl."""
    from crawler import SiteCrawler

    crawler = SiteCrawler(
        start_url=args.url,
        max_pages=args.max_pages,
        same_domain=not args.no_same_domain,
        output_dir=args.output_dir,
        headless=not args.no_headless,
    )
    await crawler.crawl(resume=not args.no_resume)


def main():
    parser = argparse.ArgumentParser(
        description="Unified web crawling tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single page fetch
  python web_crawler.py fetch https://example.com
  python web_crawler.py fetch https://spa-app.com --wait networkidle
  python web_crawler.py fetch https://blog.com/post --selector "article"

  # Site-wide crawl
  python web_crawler.py crawl https://docs.example.com
  python web_crawler.py crawl https://example.com --max-pages 20
        """,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # fetch subcommand
    fetch_parser = subparsers.add_parser("fetch", help="Single page fetch with JS rendering")
    fetch_parser.add_argument("url", help="URL to fetch")
    fetch_parser.add_argument(
        "--wait",
        choices=["load", "domcontentloaded", "networkidle"],
        default="load",
        help="When to consider navigation complete (default: load)",
    )
    fetch_parser.add_argument(
        "--timeout",
        type=int,
        default=30000,
        help="Navigation timeout in ms (default: 30000)",
    )
    fetch_parser.add_argument(
        "--selector",
        help="Only extract content within this CSS selector",
    )
    fetch_parser.add_argument(
        "--remove",
        dest="remove_selector",
        help="Additional CSS selectors to remove (comma-separated)",
    )
    fetch_parser.add_argument(
        "--js",
        help="JavaScript to execute after page load",
    )
    fetch_parser.add_argument(
        "--no-playwright",
        action="store_true",
        help="Force fallback mode (requests + BeautifulSoup)",
    )
    fetch_parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)",
    )
    fetch_parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON with metadata",
    )

    # crawl subcommand
    crawl_parser = subparsers.add_parser("crawl", help="BFS site-wide crawl")
    crawl_parser.add_argument("url", help="Starting URL")
    crawl_parser.add_argument(
        "--max-pages",
        type=int,
        default=50,
        help="Max pages to crawl (default: 50)",
    )
    crawl_parser.add_argument(
        "--no-same-domain",
        action="store_true",
        help="Allow cross-domain crawling",
    )
    crawl_parser.add_argument(
        "--output-dir",
        help="Output directory",
    )
    crawl_parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Show browser window",
    )
    crawl_parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Start fresh (ignore checkpoint)",
    )

    args = parser.parse_args()

    if args.command == "fetch":
        cmd_fetch(args)
    elif args.command == "crawl":
        asyncio.run(cmd_crawl(args))


if __name__ == "__main__":
    main()
