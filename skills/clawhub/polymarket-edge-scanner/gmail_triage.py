#!/usr/bin/env python3
"""Gmail auto-triage script for Maton/OpenClaw.

Labels messages based on sender patterns and optionally archives them.
Run manually for cleanup or schedule via cron for ongoing triage.
"""

import fcntl
import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

API_KEY = os.environ.get("MATON_API_KEY")
if not API_KEY:
    raise SystemExit("MATON_API_KEY not set")

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gmail_triage.state.json")
LOCK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gmail_triage.lock")

BASE_URL = "https://api.maton.ai/google-mail/gmail/v1/users/me"

LABELS = {
    "INBOX/Jobs": "Label_15",
    "INBOX/Finance": "Label_14",
    "INBOX/LinkedIn": "Label_13",
    "INBOX/Newsletters": "Label_17",
    "INBOX/Tech": "Label_18",
    "INBOX/Promotions": "Label_19",
    "Promotions": "Label_20",
    "INBOX/Security": "Label_21",
    "Security Alerts": "Label_22",
    "Receipts": "Label_6",
    "Work": "Label_9",
    "Idiot": "Label_12",
}

# Rules: (query, label_name, archive)
# archive=True removes the INBOX label (moves out of inbox).
RULES = [
    # Jobs
    ("from:jobalerts-noreply@linkedin.com", "INBOX/Jobs", True),
    ("from:donotreply@match.indeed.com", "INBOX/Jobs", True),
    ("from:info@jobalerts.pnet.co.za", "INBOX/Jobs", True),
    ("from:teamtailor-mail.com", "INBOX/Jobs", True),
    ("from:messages-noreply@linkedin.com", "INBOX/LinkedIn", True),
    ("from:updates-noreply@linkedin.com", "INBOX/LinkedIn", True),
    ("from:newsletters-noreply@linkedin.com", "INBOX/LinkedIn", True),
    # Newsletters & marketing
    ("from:no-reply@e.udemymail.com", "INBOX/Newsletters", True),
    ("from:mail.beehiiv.com", "INBOX/Newsletters", True),
    ("from:newsletter@myclaw.ai", "INBOX/Newsletters", True),
    ("from:aioseo.com", "INBOX/Newsletters", True),
    ("from:moltbook.com", "INBOX/Newsletters", True),
    ("from:roboshadow.com", "INBOX/Newsletters", True),
    ("from:global.fortinet.com", "INBOX/Newsletters", True),
    ("from:premiuminfo.fool.com", "INBOX/Newsletters", True),
    ("from:motley.fool.com", "INBOX/Newsletters", True),
    ("from:samuraiguitartheory.com", "INBOX/Newsletters", True),
    ("from:apollo.io", "INBOX/Newsletters", True),
    ("from:hostinger.com", "INBOX/Newsletters", True),
    # Promotions / shopping
    ("from:michaelkorsmail.com", "Promotions", True),
    ("from:mail.checkers.co.za", "Promotions", True),
    ("from:onedealaday.co.za", "Promotions", True),
    ("from:overloud.com", "Promotions", True),
    ("from:oldjwauctioneers.com", "Promotions", True),
    ("from:stevenslateaudio.com", "Promotions", True),
    # Finance
    ("from:no-reply@discoverybank.co.za", "INBOX/Finance", False),
    ("from:fnbcardemail.co.za", "INBOX/Finance", False),
    ("from:fnb.co.za", "INBOX/Finance", False),
    ("from:stripe.com", "INBOX/Finance", False),
    ("from:paypal.com", "INBOX/Finance", False),
    # Security alerts
    ("from:mail.anthropic.com", "Security Alerts", False),
    ("from:no-reply@accounts.google.com", "Security Alerts", False),
    ("from:binance.com", "Security Alerts", False),
]


def api_request(path, method="GET", data=None):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
        req.data = body
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read()
        if not body:
            return {}
        return json.loads(body.decode("utf-8"))


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def search_messages(query, max_results=100, after_date=None):
    parts = [query]
    if after_date:
        # Gmail after: uses YYYY/MM/DD format.
        parts.append(f"after:{after_date}")
    q = urllib.parse.quote(" ".join(parts))
    result = api_request(f"/messages?q={q}&maxResults={max_results}")
    return result.get("messages", [])


BATCH_SIZE = 100


def batch_modify(msg_ids, add_label, archive):
    data = {
        "ids": msg_ids,
        "addLabelIds": [add_label],
    }
    if archive:
        data["removeLabelIds"] = ["INBOX"]
    return api_request("/messages/batchModify", method="POST", data=data)


class SingleInstance:
    def __enter__(self):
        self.fp = open(LOCK_FILE, "w")
        try:
            fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (IOError, OSError):
            print("Another instance is already running. Exiting.", flush=True)
            sys.exit(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fcntl.lockf(self.fp, fcntl.LOCK_UN)
        self.fp.close()
        try:
            os.remove(LOCK_FILE)
        except OSError:
            pass


def main():
    with SingleInstance():
        state = load_state()
        now = datetime.now(timezone.utc)
        last_run = state.get("last_run")
        after_date = None
        if last_run:
            # Process messages from the day before the last run to avoid missing edge cases.
            after_dt = datetime.fromisoformat(last_run) - timedelta(days=1)
            after_date = after_dt.strftime("%Y/%m/%d")
            print(f"Gmail triage started at {now.isoformat()} (processing since {after_date})", flush=True)
        else:
            print(f"Gmail triage started at {now.isoformat()} (processing all messages)", flush=True)

        total_modified = 0
        for query, label_name, archive in RULES:
            label_id = LABELS[label_name]
            try:
                messages = search_messages(query, after_date=after_date)
            except Exception as e:
                print(f"  Search failed for '{query}': {e}", flush=True)
                continue
            if not messages:
                print(f"  '{query}': no messages found", flush=True)
                continue
            print(f"  '{query}': {len(messages)} messages -> {label_name} (archive={archive})", flush=True)
            ids = [msg["id"] for msg in messages]
            for i in range(0, len(ids), BATCH_SIZE):
                batch = ids[i:i + BATCH_SIZE]
                try:
                    batch_modify(batch, label_id, archive)
                    total_modified += len(batch)
                    print(f"    batch {i // BATCH_SIZE + 1}: {len(batch)} messages", flush=True)
                except Exception as e:
                    print(f"    Failed batch {i // BATCH_SIZE + 1}: {e}", flush=True)

        state["last_run"] = now.isoformat()
        save_state(state)
        print(f"Done. Modified {total_modified} messages.", flush=True)


if __name__ == "__main__":
    main()
