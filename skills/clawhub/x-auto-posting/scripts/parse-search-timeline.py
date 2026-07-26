import argparse
import json
import sys


def extract_tweets(body: dict) -> list:
    """Walk a SearchTimeline GraphQL response and return the tweet entries (normalized)."""
    timeline = (body.get("data", {})
                    .get("search_by_raw_query", {})
                    .get("search_timeline", {})
                    .get("timeline", {}))
    instructions = timeline.get("instructions", [])
    entries = []
    for ins in instructions:
        entries.extend(ins.get("entries", []) or [])

    out = []
    for entry in entries:
        content = entry.get("content", {}) or {}
        item = content.get("itemContent") or {}
        if item.get("itemType") != "TimelineTweet":
            continue
        result = (item.get("tweet_results") or {}).get("result") or {}
        if result.get("__typename") == "TweetWithVisibilityResults":
            result = result.get("tweet", {}) or {}
        if result.get("__typename") not in ("Tweet", None):
            # skip tombstones / unavailable tweets
            continue
        legacy = result.get("legacy") or {}
        user_result = ((result.get("core") or {}).get("user_results") or {}).get("result") or {}
        user_core = user_result.get("core") or {}
        user_legacy = user_result.get("legacy") or {}
        verification = user_result.get("verification") or {}

        rest_id = result.get("rest_id") or legacy.get("id_str")
        screen = user_core.get("screen_name")
        views_raw = (result.get("views") or {}).get("count")
        try:
            views = int(views_raw) if views_raw is not None else None
        except (TypeError, ValueError):
            views = None

        metrics = {
            "likes": legacy.get("favorite_count", 0) or 0,
            "replies": legacy.get("reply_count", 0) or 0,
            "retweets": legacy.get("retweet_count", 0) or 0,
            "quotes": legacy.get("quote_count", 0) or 0,
            "bookmarks": legacy.get("bookmark_count", 0) or 0,
            "views": views,
        }
        score = (metrics["likes"]
                 + metrics["retweets"] * 2
                 + metrics["replies"] * 1.5
                 + metrics["bookmarks"] * 1.5
                 + metrics["quotes"] * 2)

        hashtags = [h.get("text") for h in ((legacy.get("entities") or {}).get("hashtags") or []) if h.get("text")]
        mentions = [m.get("screen_name") for m in ((legacy.get("entities") or {}).get("user_mentions") or []) if m.get("screen_name")]
        media_list = ((legacy.get("extended_entities") or {}).get("media") or [])
        media = [{"type": m.get("type"), "url": m.get("media_url_https")} for m in media_list]

        out.append({
            "id": rest_id,
            "url": f"https://x.com/{screen}/status/{rest_id}" if screen and rest_id else None,
            "text": legacy.get("full_text"),
            "lang": legacy.get("lang"),
            "created_at": legacy.get("created_at"),
            "author": {
                "screen_name": screen,
                "name": user_core.get("name"),
                "followers": user_legacy.get("followers_count"),
                "verified": verification.get("verified") or user_result.get("is_blue_verified", False),
            },
            "metrics": metrics,
            "hashtags": hashtags,
            "mentions": mentions,
            "has_media": len(media) > 0,
            "media": media,
            "is_reply": bool(legacy.get("in_reply_to_status_id_str")),
            "score": round(score, 2),
        })
    return out


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description=(
            "Parse the response body of a SearchTimeline GraphQL request. "
            "Input: full JSON from `browser-act network request <id> --format json` (piped via stdin). "
            "Output: extracted tweet list with normalized fields, sorted by engagement score desc."
        )
    )
    parser.add_argument("--top", type=int, default=None, help="Return only the top N tweets by score")
    parser.add_argument("--min-score", type=float, default=None, help="Filter out tweets with score below this threshold")
    parser.add_argument("--non-reply-only", action="store_true", help="Drop replies (tweets that are in-reply-to)")
    args = parser.parse_args()

    try:
        raw = sys.stdin.buffer.read().decode("utf-8")
    except AttributeError:
        raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"error": True, "message": "empty stdin -- pipe `browser-act network request <id> --format json` into this script"}))
        sys.exit(1)

    try:
        envelope = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": True, "message": f"stdin is not valid JSON: {e}"}))
        sys.exit(1)

    body_raw = envelope.get("response_body") if isinstance(envelope, dict) else None
    if body_raw is None:
        # Maybe the caller already passed the raw GraphQL body
        body = envelope
    else:
        try:
            body = json.loads(body_raw)
        except json.JSONDecodeError:
            print(json.dumps({"error": True, "message": "response_body is not JSON -- target request may not be SearchTimeline"}))
            sys.exit(1)

    tweets = extract_tweets(body)
    if args.non_reply_only:
        tweets = [t for t in tweets if not t["is_reply"]]
    if args.min_score is not None:
        tweets = [t for t in tweets if t["score"] >= args.min_score]
    tweets.sort(key=lambda t: t["score"], reverse=True)
    if args.top:
        tweets = tweets[: args.top]

    print(json.dumps({"count": len(tweets), "tweets": tweets}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
