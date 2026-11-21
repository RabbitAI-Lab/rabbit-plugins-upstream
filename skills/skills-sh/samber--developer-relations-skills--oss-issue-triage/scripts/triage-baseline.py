#!/usr/bin/env python3
"""Measure an issue/PR queue before redesigning its triage system.

Reads an issue export (JSON array, JSON Lines, or CSV) and reports queue size,
age distribution, untriaged share, label usage, first-response time and
inflow/outflow balance. Expected fields per record, missing ones skipped rather
than fatal: number, title, state, createdAt, updatedAt, closedAt, labels,
author, comments. SKILL.md step 1 has the export and invocation commands.
"""

import argparse
import csv
import json
import sys
from datetime import datetime, timezone


def parse_time(value):
    if not value:
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc)
    text = str(value).strip().replace("Z", "+00:00")
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(text, fmt)
                break
            except ValueError:
                continue
        else:
            return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def load_records(path):
    with open(path, encoding="utf-8") as handle:
        head = handle.read(1)
        handle.seek(0)
        if head == "[":
            return json.load(handle)
        if head == "{":
            return [json.loads(line) for line in handle if line.strip()]
        return list(csv.DictReader(handle))


def normalize_labels(raw):
    """Accept [{'name': 'bug'}], ['bug'], or 'bug,enhancement'."""
    if not raw:
        return []
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError:
            return [part.strip() for part in raw.split(",") if part.strip()]
    if isinstance(raw, dict):
        raw = raw.get("nodes", [])
    out = []
    for item in raw or []:
        if isinstance(item, dict):
            name = item.get("name") or item.get("title")
            if name:
                out.append(str(name))
        elif item:
            out.append(str(item))
    return out


def author_login(raw):
    if isinstance(raw, dict):
        return raw.get("login") or raw.get("username") or raw.get("name")
    return str(raw) if raw else None


def first_response_hours(record, created):
    """Hours until the first comment by someone other than the author.

    Bot accounts are excluded: an automated greeting is not a response, and
    counting it would hide exactly the delay this measures.
    """
    comments = record.get("comments")
    if isinstance(comments, dict):
        comments = comments.get("nodes", [])
    if not isinstance(comments, list) or not created:
        return None
    opener = (author_login(record.get("author")) or "").lower()
    best = None
    for comment in comments:
        if not isinstance(comment, dict):
            continue
        login = (author_login(comment.get("author")) or "").lower()
        if not login or login == opener or login.endswith("[bot]") or login.endswith("-bot"):
            continue
        at = parse_time(comment.get("createdAt") or comment.get("created_at"))
        if at and (best is None or at < best):
            best = at
    if best is None:
        return None
    return max(0.0, (best - created).total_seconds() / 3600.0)


def percentile(values, share):
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, int(round((len(ordered) - 1) * share)))
    return ordered[index]


def build_report(records, now, stale_days, triage_prefixes, window_days):
    open_ages, response_hours, label_counts = [], [], {}
    untriaged, stale, no_response = [], [], []
    open_count = closed_count = created_in_window = closed_in_window = 0

    for record in records:
        state = str(record.get("state") or record.get("status") or "open").lower()
        created = parse_time(record.get("createdAt") or record.get("created_at"))
        updated = parse_time(record.get("updatedAt") or record.get("updated_at")) or created
        closed = parse_time(record.get("closedAt") or record.get("closed_at"))
        labels = normalize_labels(record.get("labels"))
        number = record.get("number") or record.get("iid") or record.get("id")

        for label in labels:
            label_counts[label] = label_counts.get(label, 0) + 1

        if created and (now - created).days <= window_days:
            created_in_window += 1
        if closed and (now - closed).days <= window_days:
            closed_in_window += 1

        if state.startswith("closed") or state == "merged" or closed:
            closed_count += 1
            continue

        open_count += 1
        if created:
            open_ages.append((now - created).days)
        if updated and (now - updated).days >= stale_days:
            stale.append(number)

        classified = any(
            label.startswith(prefix) or label == prefix.rstrip("/")
            for label in labels
            for prefix in triage_prefixes
        ) if triage_prefixes else bool(labels)
        if not classified:
            untriaged.append(number)

        hours = first_response_hours(record, created)
        if hours is None:
            if isinstance(record.get("comments"), (list, dict)):
                no_response.append(number)
        else:
            response_hours.append(hours)

    return {
        "generated_at": now.isoformat(),
        "totals": {
            "records": len(records),
            "open": open_count,
            "closed": closed_count,
        },
        "open_age_days": {
            "median": percentile(open_ages, 0.5),
            "p90": percentile(open_ages, 0.9),
            "max": max(open_ages) if open_ages else None,
        },
        "untriaged": {
            "count": len(untriaged),
            "share_of_open": round(len(untriaged) / open_count, 3) if open_count else None,
            "sample": untriaged[:15],
        },
        "stale": {
            "threshold_days": stale_days,
            "count": len(stale),
            "share_of_open": round(len(stale) / open_count, 3) if open_count else None,
            "sample": stale[:15],
        },
        "first_response_hours": {
            "measured": len(response_hours),
            "median": round(percentile(response_hours, 0.5), 1) if response_hours else None,
            "p90": round(percentile(response_hours, 0.9), 1) if response_hours else None,
            "never_answered_open": len(no_response),
        },
        "flow_window_days": window_days,
        "flow": {
            "created": created_in_window,
            "closed": closed_in_window,
            "net": created_in_window - closed_in_window,
        },
        "labels": {
            "distinct": len(label_counts),
            "top": sorted(label_counts.items(), key=lambda kv: -kv[1])[:20],
            "used_once": sorted(name for name, count in label_counts.items() if count == 1),
        },
    }


def render(report):
    totals, ages = report["totals"], report["open_age_days"]
    lines = [
        f"Records {totals['records']}  open {totals['open']}  closed {totals['closed']}",
        f"Open age (days): median {ages['median']}  p90 {ages['p90']}  oldest {ages['max']}",
        f"Untriaged: {report['untriaged']['count']} ({report['untriaged']['share_of_open']} of open)"
        f"  sample {report['untriaged']['sample']}",
        f"Inactive >= {report['stale']['threshold_days']}d: {report['stale']['count']}"
        f" ({report['stale']['share_of_open']} of open)",
        f"First response (h): median {report['first_response_hours']['median']}"
        f"  p90 {report['first_response_hours']['p90']}"
        f"  measured on {report['first_response_hours']['measured']} items"
        f"  never answered {report['first_response_hours']['never_answered_open']}",
        f"Last {report['flow_window_days']}d: +{report['flow']['created']} created"
        f"  -{report['flow']['closed']} closed  net {report['flow']['net']:+d}",
        f"Labels: {report['labels']['distinct']} distinct,"
        f" {len(report['labels']['used_once'])} used exactly once",
    ]
    for name, count in report["labels"]["top"]:
        lines.append(f"  {count:>5}  {name}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", help="issue export files (JSON array, JSONL or CSV)")
    parser.add_argument("--stale-days", type=int, default=90, help="inactivity threshold (default 90)")
    parser.add_argument("--window-days", type=int, default=90, help="inflow/outflow window (default 90)")
    parser.add_argument(
        "--triage-prefix",
        default="",
        help="comma-separated label prefixes that count as triaged, e.g. 'kind/,priority/'."
        " Empty means any label counts.",
    )
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    records = []
    for path in args.paths:
        try:
            records.extend(load_records(path))
        except (OSError, json.JSONDecodeError) as error:
            print(f"cannot read {path}: {error}", file=sys.stderr)
            return 1
    if not records:
        print("no records found", file=sys.stderr)
        return 1

    prefixes = [p.strip() for p in args.triage_prefix.split(",") if p.strip()]
    report = build_report(records, datetime.now(timezone.utc), args.stale_days, prefixes, args.window_days)
    print(json.dumps(report, indent=2) if args.format == "json" else render(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
