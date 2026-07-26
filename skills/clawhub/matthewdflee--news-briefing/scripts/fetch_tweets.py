#!/usr/bin/env python3
"""
Fetch recent tweets from all configured accounts using Scweet.
Outputs JSON array of tweets from the last 24 hours.

Usage: python3 fetch_tweets.py [--hours N] [--output path] [--limit N]

Requirements:
- pip install scweet
- Twitter/X auth_token (get from browser cookies)
- VPN/proxy if x.com is restricted in your region
"""

import json
import sys
import os
import argparse
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

from Scweet import Scweet

# ============================================================
# CONFIGURATION - Edit these values for your setup
# ============================================================

# Your Twitter/X auth_token
# Get it from: browser login to x.com -> F12 -> Application -> Cookies -> auth_token
AUTH_TOKEN = os.environ.get("TWITTER_AUTH_TOKEN", "YOUR_AUTH_TOKEN_HERE")

# All accounts grouped by category
# Customize these lists with your preferred accounts
ACCOUNTS = {
    "ICT Trading": ["example_trader1", "example_trader2", "example_trader3"],
    "US Stocks": ["example_stock1", "example_stock2", "example_stock3"],
    "AI": ["example_ai1", "example_ai2", "example_ai3"],
    "Politics": ["example_politician1", "example_politician2", "example_politician3"],
    "Finance": ["example_finance1", "example_finance2", "example_finance3"],
    "Tech": ["example_tech1", "example_tech2", "example_tech3"],
}

# ============================================================


def parse_timestamp(ts_str):
    """Parse Scweet timestamp string like 'Wed Jul 15 13:11:11 +0000 2026'"""
    try:
        return parsedate_to_datetime(ts_str)
    except Exception:
        try:
            return datetime.strptime(ts_str, "%a %b %d %H:%M:%S %z %Y")
        except Exception:
            return None


def main():
    parser = argparse.ArgumentParser(description="Fetch recent tweets")
    parser.add_argument("--hours", type=int, default=24, help="Hours to look back")
    parser.add_argument("--output", type=str, default=None, help="Output file path")
    parser.add_argument("--limit", type=int, default=5, help="Max tweets per account")
    args = parser.parse_args()

    if AUTH_TOKEN == "YOUR_AUTH_TOKEN_HERE":
        print("ERROR: Please set your Twitter auth_token.", file=sys.stderr)
        print("Either set TWITTER_AUTH_TOKEN env var or edit AUTH_TOKEN in this script.", file=sys.stderr)
        sys.exit(1)

    api = Scweet(auth_token=AUTH_TOKEN)

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    all_tweets = []

    # Fetch in batches to avoid rate limits
    for category, users in ACCOUNTS.items():
        print(f"Fetching {category}: {users}", file=sys.stderr)
        try:
            tweets = api.get_profile_tweets(users=users, limit=args.limit)
            for t in tweets:
                ts = parse_timestamp(t.get("timestamp", ""))
                if ts and ts >= cutoff:
                    user_info = t.get("user", {})
                    screen_name = user_info.get("screen_name", "?") if isinstance(user_info, dict) else str(user_info)
                    all_tweets.append({
                        "category": category,
                        "username": screen_name,
                        "text": t.get("text", ""),
                        "timestamp": t.get("timestamp", ""),
                        "likes": t.get("likes", 0),
                        "retweets": t.get("retweets", 0),
                        "comments": t.get("comments", 0),
                        "tweet_url": t.get("tweet_url", ""),
                        "tweet_id": t.get("tweet_id", ""),
                    })
        except Exception as e:
            print(f"  Error fetching {category}: {e}", file=sys.stderr)

    # Sort by likes descending
    all_tweets.sort(key=lambda x: x.get("likes", 0), reverse=True)

    output = json.dumps(all_tweets, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Written {len(all_tweets)} tweets to {args.output}", file=sys.stderr)
    else:
        print(output)

    print(f"Total: {len(all_tweets)} tweets from last {args.hours}h", file=sys.stderr)


if __name__ == "__main__":
    main()
