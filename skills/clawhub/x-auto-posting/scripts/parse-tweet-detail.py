import argparse
import json
import sys


def find_target_tweet(body: dict, tweet_id: str) -> dict | None:
    """Walk a TweetDetail GraphQL response and find the entry matching tweet-{id}."""
    ins = (body.get("data", {})
               .get("threaded_conversation_with_injections_v2", {})
               .get("instructions", []) or [])
    for instruction in ins:
        if instruction.get("type") != "TimelineAddEntries":
            continue
        for entry in instruction.get("entries", []) or []:
            entry_id = entry.get("entryId") or ""
            if entry_id != f"tweet-{tweet_id}":
                continue
            content = entry.get("content", {}) or {}
            item = content.get("itemContent") or {}
            result = (item.get("tweet_results") or {}).get("result") or {}
            if result.get("__typename") == "TweetWithVisibilityResults":
                result = result.get("tweet", {}) or {}
            return result
    return None


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description=(
            "Parse a TweetDetail GraphQL response and extract engagement metrics for a specific tweet. "
            "Input: full JSON from `browser-act network request <id> --format json` via stdin."
        )
    )
    parser.add_argument("tweet_id", help="Tweet ID to locate within the response (e.g. 1234567890)")
    args = parser.parse_args()

    try:
        raw = sys.stdin.buffer.read().decode("utf-8")
    except AttributeError:
        raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"error": True, "message": "empty stdin"}))
        sys.exit(1)

    envelope = json.loads(raw)
    body_raw = envelope.get("response_body") if isinstance(envelope, dict) else None
    body = json.loads(body_raw) if body_raw is not None else envelope

    tweet = find_target_tweet(body, args.tweet_id)
    if not tweet:
        print(json.dumps({"error": True, "message": f"tweet {args.tweet_id} not found in response -- verify tweet URL and that the request is TweetDetail"}))
        sys.exit(1)

    legacy = tweet.get("legacy") or {}
    user_result = ((tweet.get("core") or {}).get("user_results") or {}).get("result") or {}
    user_core = user_result.get("core") or {}

    views_raw = (tweet.get("views") or {}).get("count")
    try:
        views = int(views_raw) if views_raw is not None else None
    except (TypeError, ValueError):
        views = None

    screen = user_core.get("screen_name")

    out = {
        "id": tweet.get("rest_id") or args.tweet_id,
        "url": f"https://x.com/{screen}/status/{args.tweet_id}" if screen else None,
        "text": legacy.get("full_text"),
        "lang": legacy.get("lang"),
        "created_at": legacy.get("created_at"),
        "author": {
            "screen_name": screen,
            "name": user_core.get("name"),
        },
        "metrics": {
            "likes": legacy.get("favorite_count", 0) or 0,
            "replies": legacy.get("reply_count", 0) or 0,
            "retweets": legacy.get("retweet_count", 0) or 0,
            "quotes": legacy.get("quote_count", 0) or 0,
            "bookmarks": legacy.get("bookmark_count", 0) or 0,
            "views": views,
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
