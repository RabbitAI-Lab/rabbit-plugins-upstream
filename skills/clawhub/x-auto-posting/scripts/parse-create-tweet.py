import argparse
import json
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description=(
            "Parse a CreateTweet GraphQL response and return the newly created tweet's id and public URL. "
            "Input: full JSON from `browser-act network request <id> --format json` via stdin."
        )
    )
    parser.parse_args()

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

    if isinstance(body, dict) and body.get("errors"):
        print(json.dumps({"error": True, "message": "CreateTweet returned errors", "errors": body["errors"]}, ensure_ascii=False))
        sys.exit(1)

    result = (body.get("data", {})
                  .get("create_tweet", {})
                  .get("tweet_results", {})
                  .get("result", {})) or {}
    if result.get("__typename") == "TweetWithVisibilityResults":
        result = result.get("tweet", {}) or {}

    rest_id = result.get("rest_id")
    legacy = result.get("legacy") or {}
    user_result = ((result.get("core") or {}).get("user_results") or {}).get("result") or {}
    user_core = user_result.get("core") or {}
    screen = user_core.get("screen_name")

    if not rest_id:
        print(json.dumps({"error": True, "message": "could not locate rest_id in CreateTweet response -- may be a duplicate or failed post"}))
        sys.exit(1)

    print(json.dumps({
        "id": rest_id,
        "url": f"https://x.com/{screen}/status/{rest_id}" if screen else f"https://x.com/i/status/{rest_id}",
        "author": screen,
        "text": legacy.get("full_text"),
        "created_at": legacy.get("created_at"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
