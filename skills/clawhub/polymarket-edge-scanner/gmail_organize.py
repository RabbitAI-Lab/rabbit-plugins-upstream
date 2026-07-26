#!/usr/bin/env python3
"""Batch-organize Gmail inbox using local Maton CLI (rate-limited)."""
import json
import subprocess
import sys
import time
from collections import defaultdict

MATON = "./node_modules/.bin/maton"
API_KEY = "v2.fSIdyoTHcoGKwYQnWcS0DBYQNSBCv-FMrmCNeqjTktG9LgZMjo6UAimFGtHmrmH7ztgXj5f5kHmmzGRcElsYQWHw6hShbxkOsG1JwxBWFO3lfviy1xdpp7vS"

def run(cmd, env=None):
    full_env = {
        "MATON_API_KEY": API_KEY,
        "HOME": "/root",
    }
    if env:
        full_env.update(env)
    result = subprocess.run(cmd, capture_output=True, text=True, env=full_env, cwd="/root/.openclaw/workspace")
    return result.stdout, result.stderr, result.returncode

def api_call(cmd, retries=5):
    """Execute a Maton CLI command with rate-limit backoff."""
    for attempt in range(retries):
        stdout, stderr, rc = run(cmd)
        if rc == 0:
            time.sleep(0.8)
            return stdout, None
        if "429" in stderr and attempt < retries - 1:
            sleep_time = 2 ** attempt
            print(f"  429, sleeping {sleep_time}s...", file=sys.stderr)
            time.sleep(sleep_time)
            continue
        time.sleep(0.8)
        return stdout, stderr
    return stdout, stderr

def list_unread(query, max_results=100):
    cmd = [MATON, "gmail", "message", "list", "-L", str(max_results), "--query", query, "--hydrate", "--json"]
    stdout, err = api_call(cmd)
    if err:
        print(f"list '{query}' failed: {err}", file=sys.stderr)
        return []
    try:
        data = json.loads(stdout)
        return data.get("messages", [])
    except json.JSONDecodeError as e:
        print(f"list '{query}' JSON error: {e}", file=sys.stderr)
        return []

def get_message(msg_id):
    cmd = [MATON, "gmail", "message", "get", msg_id, "--headers", "--json"]
    stdout, err = api_call(cmd)
    if err:
        print(f"get {msg_id} failed: {err}", file=sys.stderr)
        return None
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return None

def modify_message(msg_id, add_labels=None, remove_labels=None):
    cmd = [MATON, "gmail", "message", "modify", msg_id]
    if add_labels:
        for lbl in add_labels:
            cmd.extend(["--add-label", lbl])
    if remove_labels:
        for lbl in remove_labels:
            cmd.extend(["--remove-label", lbl])
    stdout, err = api_call(cmd)
    return err is None, err

LABELS = {
    "linkedin": "Label_13",
    "jobs": "Label_15",
    "finance": "Label_14",
    "newsletters": "Label_17",
    "igaming": "Label_16",
    "tech": "Label_18",
}

PROMO_SENDERS = [
    "michaelkors", "michael kors",
    "checkers", "pick n pay", "pnp.co.za",
    "fortinet", "samuraiguitartheory", "samurai guitar",
    "firstshop", "oldjwauctioneers", "sunglass hut", "sunglasshut",
    "stevenslateaudio", "fanvue.com", "fanvue",
    "onedealaday", "one deal a day",
    "motley fool", "premiuminfo.fool", "motley.fool",
]

JOB_SENDERS = [
    "indeed", "pnet", "greenhouse", "monks.com", "greys", "placementpartner",
    "executive placements", "executiveplacements", "glassdoor", "simplify.hr",
    "jobstellen", "orange cyberdefense", "teamtailor",
]

FINANCE_SENDERS = [
    "fnb.co.za", "discovery bank", "discovery.bank", "moonshot", "hostinger", "stripe.com",
]

NEWSLETTER_SENDERS = [
    "udemy", "udemymail",
]

IGAMING_SENDERS = [
    "wordpress@igamingreviews", "igamingreviews",
]

TECH_SENDERS = [
    "1password", "anthropic", "google",
]

def classify(msg):
    headers = msg.get("headers", {})
    from_hdr = (headers.get("from") or "").lower()
    subject = (headers.get("subject") or "").lower()

    label = None
    is_promo = False

    if any(s in from_hdr for s in JOB_SENDERS) or "job alert" in subject or "application" in subject or "matching your profile" in subject:
        label = LABELS["jobs"]
    elif "linkedin" in from_hdr:
        label = LABELS["linkedin"]
    elif any(s in from_hdr for s in FINANCE_SENDERS):
        label = LABELS["finance"]
    elif any(s in from_hdr for s in NEWSLETTER_SENDERS):
        label = LABELS["newsletters"]
    elif any(s in from_hdr for s in IGAMING_SENDERS) or "igaming" in subject:
        label = LABELS["igaming"]
    elif any(s in from_hdr for s in TECH_SENDERS):
        label = LABELS["tech"]

    if any(s in from_hdr for s in PROMO_SENDERS):
        is_promo = True

    return label, is_promo

def fetch_all_unread():
    """Fetch unread by date slices to avoid pagination issues."""
    queries = [
        "is:unread newer_than:1d",
        "is:unread older_than:1d newer_than:2d",
        "is:unread older_than:2d newer_than:3d",
        "is:unread older_than:3d newer_than:7d",
        "is:unread older_than:7d newer_than:14d",
        "is:unread older_than:14d newer_than:30d",
        "is:unread older_than:30d",
    ]
    all_messages = []
    seen = set()
    for q in queries:
        msgs = list_unread(q, 100)
        new = [m for m in msgs if m["id"] not in seen]
        seen.update(m["id"] for m in new)
        all_messages.extend(new)
        print(f"  '{q}' -> {len(msgs)} total, {len(new)} new")
    return all_messages

def main():
    print("Fetching unread messages by date range (rate-limited)...")
    messages = fetch_all_unread()
    print(f"Total unique unread fetched: {len(messages)}")

    # Enrich only empty hydrated entries (with retry/backoff built in)
    enriched = []
    empty_count = 0
    for m in messages:
        if not m.get("from") and not m.get("subject"):
            full = get_message(m["id"])
            if full:
                enriched.append(full)
            else:
                empty_count += 1
        else:
            enriched.append({
                "id": m["id"],
                "headers": {
                    "from": m.get("from", ""),
                    "subject": m.get("subject", ""),
                    "date": m.get("date", ""),
                },
                "body": "",
            })
    if empty_count:
        print(f"Skipped {empty_count} messages that couldn't be enriched.")

    label_plan = defaultdict(list)
    promo_ids = []
    for msg in enriched:
        label, is_promo = classify(msg)
        if label:
            label_plan[label].append(msg["id"])
        if is_promo:
            promo_ids.append(msg["id"])

    print("\nLabeling plan:")
    for label, ids in sorted(label_plan.items()):
        print(f"  {label}: {len(ids)} messages")
    print(f"Promotions to mark read: {len(promo_ids)} messages")

    print("\nApplying labels...")
    label_ok = label_fail = 0
    for label, ids in label_plan.items():
        for msg_id in ids:
            ok, err = modify_message(msg_id, add_labels=[label])
            if ok:
                label_ok += 1
            else:
                label_fail += 1
                print(f"  FAIL label {label} on {msg_id}: {err.strip() if err else 'unknown'}")

    print("\nMarking promotions as read...")
    read_ok = read_fail = 0
    for msg_id in promo_ids:
        ok, err = modify_message(msg_id, remove_labels=["UNREAD"])
        if ok:
            read_ok += 1
        else:
            read_fail += 1
            print(f"  FAIL mark read {msg_id}: {err.strip() if err else 'unknown'}")

    print(f"\nDone: {label_ok} labels applied, {label_fail} failures; {read_ok} marked read, {read_fail} failures.")

if __name__ == "__main__":
    main()
