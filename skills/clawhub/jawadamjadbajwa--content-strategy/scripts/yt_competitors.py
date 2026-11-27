#!/usr/bin/env python3
"""Competitor benchmark for YouTube channels (content-strategy skill).

Usage
  python yt_competitors.py @handle1 https://www.youtube.com/@handle2 UCxxxxxxxxxxxxxxxxxxxxxx \\
      --uploads 30 --out research/competitors

Per channel it reports posting cadence, median views, outlier share (how often
the channel beats its own median by 3x), short-form share, typical duration,
upload days and title patterns. Needs YOUTUBE_API_KEY (or --key). Cost is about
4 quota units per channel. Reuses yt_research.py from the same folder.

Input forms: @handle, a youtube.com/@handle or /channel/UC... URL, a bare UC id,
or a legacy /user/name URL. Legacy /c/ custom URLs cannot be resolved cheaply.
"""
import argparse
import csv
import json
import os
import re
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_research as yt  # noqa: E402

PARTS = "snippet,statistics,contentDetails"
UC = r"UC[\w-]{22}"


def get_channel(key, **kw):
    data = yt.api("channels", key, part=PARTS, **kw)
    items = data.get("items", [])
    if not items:
        raise yt.YTError(f"Channel not found for {kw}.")
    return items[0]


def resolve(key, ref):
    ref = ref.strip()
    m = re.search(rf"youtube\.com/channel/({UC})", ref) or re.fullmatch(rf"({UC})", ref)
    if m:
        return get_channel(key, id=m.group(1))
    m = re.search(r"youtube\.com/(@[\w.\-]+)", ref) or re.fullmatch(r"(@[\w.\-]+)", ref)
    if m:
        return get_channel(key, forHandle=m.group(1))
    m = re.search(r"youtube\.com/user/([\w.\-]+)", ref)
    if m:
        return get_channel(key, forUsername=m.group(1))
    raise ValueError(f"Cannot resolve '{ref}'. Use @handle, a /channel/UC... URL or the UC id.")


def pct(part, whole):
    return round(100 * part / whole, 1) if whole else None


def analyse(key, ch, n, now):
    uploads = ((ch.get("contentDetails") or {}).get("relatedPlaylists") or {}).get("uploads")
    if not uploads:
        raise yt.YTError(f"{ch['snippet']['title']}: no uploads playlist.")
    pl = yt.api("playlistItems", key, part="contentDetails", playlistId=uploads, maxResults=max(1, min(n, 50)))
    ids = [i["contentDetails"]["videoId"] for i in pl.get("items", [])]
    vids = yt.fetch_videos(key, ids) if ids else {}
    rows = []
    for v in vids.values():
        r = yt.build_row(v, ch, now)
        pub = yt.parse_time(v["snippet"]["publishedAt"])
        r["weekday"], r["hour_utc"] = pub.strftime("%a"), pub.hour
        rows.append(r)
    if not rows:
        raise yt.YTError(f"{ch['snippet']['title']}: no videos returned.")
    views = [r["views"] for r in rows if r["views"] is not None]
    med = statistics.median(views) if views else None
    for r in rows:
        r["vs_channel_median_x"] = round(r["views"] / med, 1) if med and r["views"] is not None else None
    pubs = [yt.parse_time(v["snippet"]["publishedAt"]) for v in vids.values()]
    window = max((now - min(pubs)).days, 1)
    st = ch.get("statistics") or {}
    subs = None if st.get("hiddenSubscriberCount") else yt.num(st, "subscriberCount")
    titles = [r["title"] for r in rows]
    top = sorted(rows, key=lambda r: r["views"] or 0, reverse=True)[:3]
    days = [d for d, _ in Counter(r["weekday"] for r in rows).most_common(2)]
    summary = {
        "channel": ch["snippet"]["title"], "channel_id": ch["id"],
        "handle": ch["snippet"].get("customUrl", ""),
        "subscribers": subs, "total_views": yt.num(st, "viewCount"), "video_count": yt.num(st, "videoCount"),
        "uploads_analyzed": len(rows), "window_days": window,
        "posts_per_week": round(len(rows) / (window / 7), 2),
        "days_since_last_upload": (now - max(pubs)).days,
        "median_views": int(med) if med is not None else None,
        "median_views_per_sub": round(med / subs, 3) if med is not None and subs else None,
        "outlier_share_pct": pct(sum(1 for r in rows if (r["vs_channel_median_x"] or 0) >= 3), len(rows)),
        "median_duration_sec": int(statistics.median(r["duration_sec"] for r in rows)),
        "short_form_share_pct": pct(sum(1 for r in rows if 0 < r["duration_sec"] <= 60), len(rows)),
        "top_upload_days": ", ".join(days),
        "title_has_number_pct": pct(sum(1 for t in titles if re.search(r"\d", t)), len(titles)),
        "title_question_pct": pct(sum(1 for t in titles if "?" in t), len(titles)),
        "median_title_chars": int(statistics.median(len(t) for t in titles)),
        "top_titles": " | ".join(f"{r['title']} ({yt.fmt(r['views'])})" for r in top),
    }
    for r in rows:
        r["competitor"] = summary["channel"]
    return summary, rows


def write_outputs(base, summaries, videos, meta):
    parent = os.path.dirname(base)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "channels": summaries, "videos": videos}, f, ensure_ascii=False, indent=2)
    for suffix, rows in (("_channels", summaries), ("_videos", videos)):
        if rows:
            with open(base + suffix + ".csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)
    print(f"\nSaved {base}.json, {base}_channels.csv and {base}_videos.csv", file=sys.stderr)


def print_table(summaries):
    print(f"{'channel':<24} {'subs':>6} {'/wk':>5} {'last':>5} {'med views':>9} {'outlr%':>6} {'short%':>6} "
          f"{'dur':>5}  days")
    for s in summaries:
        print(f"{s['channel'][:24]:<24} {yt.fmt(s['subscribers']):>6} {s['posts_per_week']:>5} "
              f"{str(s['days_since_last_upload']) + 'd':>5} {yt.fmt(s['median_views']):>9} "
              f"{str(s['outlier_share_pct']):>6} {str(s['short_form_share_pct']):>6} "
              f"{s['median_duration_sec']:>4}s  {s['top_upload_days']}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("channels", nargs="+", help="@handle, channel URL or UC id")
    p.add_argument("--uploads", type=int, default=30, help="recent uploads to analyze per channel (max 50)")
    p.add_argument("--key", help="API key (default: env YOUTUBE_API_KEY)")
    p.add_argument("--out", help="base path for .json and _channels/_videos .csv")
    a = p.parse_args(argv)
    key = a.key or os.environ.get("YOUTUBE_API_KEY")
    if not key:
        print("error: no API key. Set YOUTUBE_API_KEY or pass --key.", file=sys.stderr)
        return 2
    now = datetime.now(timezone.utc)
    summaries, videos, failed = [], [], []
    for ref in a.channels:
        try:
            s, rows = analyse(key, resolve(key, ref), a.uploads, now)
            summaries.append(s)
            videos += rows
        except (yt.YTError, ValueError) as e:
            failed.append((ref, str(e)))
            print(f"skipped {ref}: {e}", file=sys.stderr)
    if summaries:
        print_table(summaries)
        print("\nposts_per_week = uploads analyzed / weeks since the oldest analyzed upload (so inactivity lowers it). "
              "outlier share = videos at 3x+ the channel's own median.")
        meta = {"generated_at": now.strftime("%Y-%m-%d %H:%M UTC"), "uploads_per_channel": a.uploads,
                "quota_units_used": yt.QUOTA["used"], "failed": failed}
        if a.out:
            write_outputs(a.out, summaries, videos, meta)
    print(f"\nQuota units used this run: {yt.QUOTA['used']}", file=sys.stderr)
    return 0 if summaries else 1


if __name__ == "__main__":
    sys.exit(main())
