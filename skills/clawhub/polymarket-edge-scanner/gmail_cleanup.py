#!/usr/bin/env python3
"""Targeted cleanup of remaining Gmail unread noise."""
import json
import subprocess
import time

MATON = "./node_modules/.bin/maton"
API_KEY = "v2.fSIdyoTHcoGKwYQnWcS0DBYQNSBCv-FMrmCNeqjTktG9LgZMjo6UAimFGtHmrmH7ztgXj5f5kHmmzGRcElsYQWHw6hShbxkOsG1JwxBWFO3lfviy1xdpp7vS"

def run(cmd):
    env = {"MATON_API_KEY": API_KEY, "HOME": "/root"}
    return subprocess.run(cmd, capture_output=True, text=True, env=env, cwd="/root/.openclaw/workspace")

def api(cmd):
    for attempt in range(5):
        r = run(cmd)
        if r.returncode == 0:
            time.sleep(1.0)
            return r.stdout, None
        if "429" in r.stderr and attempt < 4:
            sleep_time = 3 ** attempt
            print(f"  429 -> sleep {sleep_time}s")
            time.sleep(sleep_time)
        else:
            time.sleep(1.0)
            return r.stdout, r.stderr
    return r.stdout, r.stderr

def list_query(query, max_results=50):
    cmd = [MATON, "gmail", "message", "list", "-L", str(max_results), "--query", query, "--json"]
    stdout, err = api(cmd)
    if err:
        print(f"list failed: {err}")
        return []
    try:
        return json.loads(stdout).get("messages", [])
    except Exception:
        return []

def mark_read(msg_id):
    cmd = [MATON, "gmail", "message", "modify", msg_id, "--remove-label", "UNREAD"]
    stdout, err = api(cmd)
    return err is None

def label(msg_id, label_id):
    cmd = [MATON, "gmail", "message", "modify", msg_id, "--add-label", label_id]
    stdout, err = api(cmd)
    return err is None

# Mark obvious promotional senders as read
PROMO_QUERIES = [
    "is:unread from:michaelkorsmail.com",
    "is:unread from:mail.checkers.co.za",
    "is:unread from:pnp.co.za",
    "is:unread from:global.fortinet.com",
    "is:unread from:samuraiguitartheory.com",
    "is:unread from:firstshop.co.za",
    "is:unread from:oldjwauctioneers.com",
    "is:unread from:e.sunglasshut.com",
    "is:unread from:stevenslateaudio.com",
    "is:unread from:fanvue.com",
    "is:unread from:onedealaday.co.za",
    "is:unread from:premiuminfo.fool.com",
    "is:unread from:motley.fool.com",
]

# Label remaining category messages
LABEL_QUERIES = [
    ("is:unread from:linkedin.com", "Label_13"),      # LinkedIn
    ("is:unread from:indeed.com OR from:pnet.co.za OR from:greenhouse-mail.io OR from:us.greenhouse-jobs.com OR from:monks.com OR from:placementpartner.com OR from:jobstellen.de OR from:glassdoor.com OR from:simplify.hr OR from:orangecyberdefensegroup.teamtailor-mail.com", "Label_15"),  # Jobs
    ("is:unread from:fnb.co.za OR from:discoverybank.co.za OR from:discovery.bank OR from:stripe.com OR from:hostinger.com", "Label_14"),  # Finance
    ("is:unread from:udemy.com OR from:udemymail.com", "Label_17"),  # Newsletters
    ("is:unread from:wordpress@igamingreviews.org OR subject:igaming", "Label_16"),  # iGaming
    ("is:unread from:1password.com OR from:accounts.google.com OR from:anthropic.com", "Label_18"),  # Tech/Security
]

def main():
    total_read = 0
    print("Marking promotional senders as read...")
    for query in PROMO_QUERIES:
        msgs = list_query(query, 50)
        if msgs:
            print(f"  {query}: {len(msgs)} messages")
            for m in msgs:
                if mark_read(m["id"]):
                    total_read += 1
                else:
                    print(f"    FAIL {m['id']}")
    print(f"Marked {total_read} promotional messages as read.")

    total_labeled = 0
    print("\nLabeling remaining category messages...")
    for query, label_id in LABEL_QUERIES:
        msgs = list_query(query, 50)
        if msgs:
            print(f"  {query}: {len(msgs)} messages -> {label_id}")
            for m in msgs:
                if label(m["id"], label_id):
                    total_labeled += 1
                else:
                    print(f"    FAIL {m['id']}")
    print(f"Labeled {total_labeled} messages.")

if __name__ == "__main__":
    main()
