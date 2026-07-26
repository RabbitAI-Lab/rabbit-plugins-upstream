#!/usr/bin/env python3
"""Targeted Gmail cleanup using search queries."""
import json
import subprocess
import sys
import time

MATON = "./node_modules/.bin/maton"

def run(cmd):
    env = {
        "MATON_API_KEY": "v2.fSIdyoTHcoGKwYQnWcS0DBYQNSBCv-FMrmCNeqjTktG9LgZMjo6UAimFGtHmrmH7ztgXj5f5kHmmzGRcElsYQWHw6hShbxkOsG1JwxBWFO3lfviy1xdpp7vS",
        "HOME": "/root",
    }
    return subprocess.run(cmd, capture_output=True, text=True, env=env, cwd="/root/.openclaw/workspace")

def search(query, max_results=50):
    cmd = [MATON, "gmail", "message", "list", "-L", str(max_results), "--query", query, "--json"]
    r = run(cmd)
    if r.returncode != 0:
        print(f"search failed for {query}: {r.stderr}", file=sys.stderr)
        return []
    try:
        data = json.loads(r.stdout)
        return data.get("messages", [])
    except Exception as e:
        print(f"parse failed for {query}: {e}", file=sys.stderr)
        return []

def add_label(msg_id, label):
    r = run([MATON, "gmail", "message", "modify", msg_id, "--add-label", label])
    return r.returncode == 0, r.stderr

def remove_label(msg_id, label):
    r = run([MATON, "gmail", "message", "modify", msg_id, "--remove-label", label])
    return r.returncode == 0, r.stderr

RULES = [
    # (query, action, label_or_none)
    ("from:linkedin.com is:unread", "label", "Label_13"),
    ("from:indeed.com OR from:pnet.co.za OR from:greenhouse-mail.io OR from:placementpartner.com OR from:simplify.hr OR from:jobstellen.de OR from:monks.com is:unread", "label", "Label_15"),
    ("from:fnb.co.za OR from:discoverybank.co.za OR from:discovery.bank OR from:stripe.com OR from:hostinger.com is:unread", "label", "Label_14"),
    ("from:udemy.com OR from:udemymail.com is:unread", "label", "Label_17"),
    ("from:igamingreviews.org OR from:wordpress@igamingreviews.org is:unread", "label", "Label_16"),
    ("from:1password.com OR from:anthropic.com is:unread", "label", "Label_18"),
    ("from:michaelkorsmail.com OR from:checkers.co.za OR from:pnp.co.za OR from:onedealaday.co.za OR from:sunglasshut.com OR from:firstshop.co.za OR from:oldjwauctioneers.com OR from:fanvue.com OR from:stevenslateaudio.com OR from:samuraiguitartheory.com is:unread", "read", None),
]

def main():
    total_label = 0
    total_read = 0
    for query, action, label in RULES:
        msgs = search(query)
        print(f"Query '{query[:50]}...' -> {len(msgs)} messages")
        for m in msgs:
            msg_id = m["id"]
            if action == "label" and label:
                ok, err = add_label(msg_id, label)
                if ok:
                    total_label += 1
                else:
                    print(f"  FAIL label {label}: {err.strip()}")
            elif action == "read":
                ok, err = remove_label(msg_id, "UNREAD")
                if ok:
                    total_read += 1
                else:
                    print(f"  FAIL read: {err.strip()}")
            time.sleep(0.1)
    print(f"\nDone: {total_label} labels applied, {total_read} marked read.")

if __name__ == "__main__":
    main()
