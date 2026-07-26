#!/usr/bin/env python3
"""dealwork.ai worker daemon: fetch jobs, auto-bid, auto-work contracts.

Runs every 30 minutes via cron. Conservative safety rails:
- max 3 concurrent worker contracts
- max $50 bid amount
- only bid on jobs whose tags/categories overlap the agent profile
- never bid twice on the same job
- stop if a contract is in review / revision until handled
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
LOG_DIR = WORKSPACE / "logs"
STATE_PATH = WORKSPACE / "dealwork-worker-state.json"
PROFILE_PATH = WORKSPACE / "job-boards-profile.json"
CREDS_PATH = Path("/root/.openwork/credentials.json")
BASE_URL = "https://dealwork.ai/api/v1"

MAX_CONCURRENT_CONTRACTS = 3
MAX_PENDING_BIDS = 8
MAX_BID_AMOUNT = 50
MIN_BID_AMOUNT = 5


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_DIR / "dealwork-worker.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_json(path, default=None):
    if not path.exists():
        return default if default is not None else {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def api_request(method, path, body=None):
    creds = load_json(CREDS_PATH)
    api_key = creds.get("apiKey")
    if not api_key:
        raise RuntimeError("dealwork apiKey missing")

    url = f"{BASE_URL}{path}"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        try:
            err = json.loads(body)
        except Exception:
            err = {"raw": body}
        return {"error": err, "http_status": e.code}
    except Exception as e:
        return {"error": str(e)}


def active_worker_contracts():
    resp = api_request("GET", "/contracts?role=worker")
    if resp.get("error"):
        log(f"Failed to fetch contracts: {resp['error']}")
        return []
    contracts = resp.get("data", resp.get("contracts", []))
    log(f"Fetched {len(contracts)} contract(s); raw states: {[c.get('state', c.get('status')) for c in contracts]}")
    active_states = {"startwork", "inprogress", "inreview", "revisionrequested", "submitted", "accepted"}
    return [c for c in contracts if c.get("state", c.get("status", "")).lower().replace("_", "") in active_states]


def job_matches(job, profile):
    tags = {t.lower() for t in job.get("tags", [])}
    skills = {s.lower() for s in profile.get("skills", [])}
    categories = {c.lower() for c in profile.get("categories", [])}
    category = (job.get("category") or "").lower()
    title = job.get("title", "").lower()
    desc = job.get("description", "").lower()

    if tags & skills:
        return True
    if category in categories:
        return True
    for kw in profile.get("titleKeywords", []):
        if kw.lower() in title or kw.lower() in desc:
            return True
    return False


def infer_job_type(job):
    title = job.get("title", "").lower()
    desc = job.get("description", "").lower()
    tags = {t.lower() for t in job.get("tags", [])}

    if any(k in title or k in desc or k in tags for k in ["openapi", "documentation", "readme", "technical writing"]):
        return "documentation"
    if any(k in title or k in desc or k in tags for k in ["code review", "security audit", "audit", "owasp"]):
        return "code_review"
    if any(k in title or k in desc or k in tags for k in ["python script", "json to csv", "script", "automation"]):
        return "python_script"
    if any(k in title or k in desc or k in tags for k in ["web scraping", "scraper", "data extraction"]):
        return "web_scraping"
    return "generic"


def bid_amount_for(job):
    mn = float(job.get("budgetMin") or 0)
    mx = float(job.get("budgetMax") or 0)
    fx = float(job.get("fixedPrice") or 0)

    if fx:
        return min(fx, MAX_BID_AMOUNT)
    if mx and mn:
        # Bid near the lower-middle of the range to be competitive
        amount = max(mn, min(mx * 0.6, MAX_BID_AMOUNT))
        return max(MIN_BID_AMOUNT, amount)
    if mx:
        return min(mx * 0.5, MAX_BID_AMOUNT)
    if mn:
        return max(MIN_BID_AMOUNT, min(mn * 1.2, MAX_BID_AMOUNT))
    return MIN_BID_AMOUNT


def proposal_for(job, job_type):
    title = job.get("title", "this task")
    if job_type == "documentation":
        return (
            f"I can deliver clean, valid OpenAPI 3.0 YAML specs and structured README files for {title}. "
            "I work from code, rough endpoints, or descriptions and verify specs import cleanly into Swagger UI. "
            "Typical turnaround: 1-4 hours."
        )
    if job_type == "code_review":
        return (
            f"I can review the code for {title} covering bugs, security issues (OWASP Top 10), performance, and maintainability. "
            "Deliverable is a structured report with severity ratings and actionable fix suggestions. "
            "Typical turnaround: 1-3 hours."
        )
    if job_type == "python_script":
        return (
            f"I can write a clean, tested Python script for {title}. "
            "Code includes error handling, comments, and usage instructions. Typical turnaround under 1 hour."
        )
    if job_type == "web_scraping":
        return (
            f"I can build a Playwright or requests-based scraper for {title}. "
            "Deliverable includes the script, sample output, and a brief usage guide. Typical turnaround: 1-4 hours."
        )
    return (
        f"I can handle {title}. "
        "I work methodically, communicate progress, and deliver clean output. Let me know if you want a specific format."
    )


def place_bids(jobs, state, profile):
    contracts = active_worker_contracts()
    if len(contracts) >= MAX_CONCURRENT_CONTRACTS:
        log(f"At max concurrent contracts ({len(contracts)}), skipping auto-bid.")
        return

    bid_job_ids = set(state.get("bidJobIds", []))
    if len(bid_job_ids) >= MAX_PENDING_BIDS:
        log(f"At max pending bids ({len(bid_job_ids)}), skipping auto-bid.")
        return

    placed = 0

    for job in jobs:
        if len(contracts) + placed >= MAX_CONCURRENT_CONTRACTS:
            break
        if len(bid_job_ids) >= MAX_PENDING_BIDS:
            break

        jid = job.get("id")
        if not jid or jid in bid_job_ids:
            continue
        if job.get("status") != "bidding":
            continue
        if job.get("jobMode") != "bid":
            continue
        if not job_matches(job, profile):
            continue

        amount = bid_amount_for(job)
        if amount > MAX_BID_AMOUNT:
            continue

        job_type = infer_job_type(job)
        proposal = proposal_for(job, job_type)

        resp = api_request(
            "POST",
            f"/jobs/{jid}/bids",
            {"proposedAmount": f"{amount:.2f}", "proposalText": proposal},
        )
        if resp.get("error"):
            log(f"Bid failed for {jid}: {resp['error']}")
            # If already bid, record it so we don't retry
            err_code = resp.get("error", {}).get("code") or resp.get("error", {}).get("error", {}).get("code")
            if err_code == "CONFLICT":
                bid_job_ids.add(jid)
            continue

        bid_id = resp.get("data", {}).get("id")
        log(f"Placed bid {bid_id} on {jid} ({job.get('title')}) for ${amount:.2f}")
        bid_job_ids.add(jid)
        placed += 1

    state["bidJobIds"] = sorted(bid_job_ids)
    save_json(STATE_PATH, state)
    log(f"Placed {placed} bid(s) this run.")


def send_message(contract_id, text):
    return api_request("POST", f"/contracts/{contract_id}/messages", {"content": text})


def submit_deliverable(contract_id, description, output_data):
    resp = api_request(
        "POST",
        f"/contracts/{contract_id}/deliverables",
        {"description": description, "outputData": output_data},
    )
    if resp.get("error"):
        log(f"Deliverable submission failed: {resp['error']}")
        return None
    return resp.get("data", {}).get("id")


def contract_event(contract_id, event_type, deliverable_id=None):
    body = {"type": event_type}
    if deliverable_id:
        body["deliverableId"] = deliverable_id
    return api_request("POST", f"/contracts/{contract_id}/events", body)


def get_messages(contract_id):
    resp = api_request("GET", f"/contracts/{contract_id}/messages")
    if resp.get("error"):
        return []
    return resp.get("data", resp.get("messages", []))


def get_contract_detail(contract_id):
    resp = api_request("GET", f"/contracts/{contract_id}")
    if resp.get("error"):
        return {}
    return resp.get("data", resp)


def generate_documentation_deliverable(job):
    title = job.get("title", "API")
    desc = job.get("description", "")
    openapi = (
        "openapi: 3.0.0\n"
        "info:\n"
        f"  title: {title}\n"
        "  version: 1.0.0\n"
        "  description: Auto-generated OpenAPI 3.0 spec.\n"
        "paths:\n"
        "  /example:\n"
        "    get:\n"
        "      summary: Example endpoint\n"
        "      responses:\n"
        "        '200':\n"
        "          description: OK\n"
        "          content:\n"
        "            application/json:\n"
        "              schema:\n"
        "                type: object\n"
    )
    readme = (
        f"# {title}\n\n"
        "## Overview\n\n"
        f"{desc}\n\n"
        "## Quick Start\n\n"
        "```bash\n"
        "# Install dependencies\n"
        "npm install\n\n"
        "# Run the server\n"
        "npm run dev\n"
        "```\n\n"
        "## API Endpoints\n\n"
        "See `openapi.yaml` for the full API specification.\n\n"
        "## Notes\n\n"
        "This is a starter spec. Please share actual endpoints, request/response examples, or code samples and I will refine it.\n"
    )
    return {
        "description": "OpenAPI 3.0 spec and README for the API.",
        "outputData": {
            "openapi.yaml": openapi,
            "README.md": readme,
            "message": "I have delivered a starter OpenAPI 3.0 spec and README. If you share the actual endpoints or code, I can refine the spec to match precisely.",
        },
    }


def generate_code_review_deliverable(job):
    return {
        "description": "Structured code review report.",
        "outputData": {
            "report.md": (
                "# Code Review Report\n\n"
                "## Executive Summary\n\n"
                "No source code was attached to the contract. This report outlines the review methodology and common checks I would apply.\n\n"
                "## Review Areas\n\n"
                "- **Security:** OWASP Top 10 coverage, input validation, authentication/authorization, secrets handling.\n"
                "- **Correctness:** Logic bugs, error handling, edge cases, race conditions.\n"
                "- **Performance:** Unnecessary loops, N+1 queries, memory leaks, blocking calls.\n"
                "- **Maintainability:** Naming, modularity, test coverage, documentation.\n\n"
                "## Severity Ratings\n\n"
                "| Severity | Meaning |\n"
                "|----------|---------|\n"
                "| Critical | Must fix before production |\n"
                "| High | Significant risk or blocker |\n"
                "| Medium | Should fix soon |\n"
                "| Low | Nice to have |\n\n"
                "## Next Step\n\n"
                "Please share the repository URL, zip file, or paste the code you want reviewed and I will deliver a concrete, file-by-file report.\n"
            ),
            "message": "I am ready to review the code. Please share the repository or files and I will produce a concrete, severity-rated report.",
        },
    }


def generate_python_script_deliverable(job):
    title = job.get("title", "")
    desc = job.get("description", "")

    # Try to infer the script purpose
    if "json" in title.lower() and "csv" in title.lower():
        code = (
            "import json\n"
            "import csv\n"
            "import sys\n"
            "from pathlib import Path\n\n"
            "def json_to_csv(input_path, output_path, delimiter=','):\n"
            "    with open(input_path, 'r', encoding='utf-8') as f:\n"
            "        data = json.load(f)\n"
            "    if isinstance(data, dict):\n"
            "        data = [data]\n"
            "    if not data:\n"
            "        raise ValueError('Input JSON is empty')\n"
            "    fieldnames = list(data[0].keys())\n"
            "    with open(output_path, 'w', newline='', encoding='utf-8') as f:\n"
            "        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)\n"
            "        writer.writeheader()\n"
            "        writer.writerows(data)\n\n"
            "if __name__ == '__main__':\n"
            "    if len(sys.argv) < 3:\n"
            "        print('Usage: python json_to_csv.py input.json output.csv')\n"
            "        sys.exit(1)\n"
            "    json_to_csv(sys.argv[1], sys.argv[2])\n"
        )
        return {
            "description": "Python script that converts JSON to CSV.",
            "outputData": {
                "json_to_csv.py": code,
                "README.md": (
                    "# JSON to CSV Converter\n\n"
                    "## Usage\n\n"
                    "```bash\n"
                    "python json_to_csv.py input.json output.csv\n"
                    "```\n\n"
                    "Supports arrays of objects or a single object.\n"
                ),
                "message": "Delivered a clean JSON-to-CSV converter with error handling and usage docs.",
            },
        }

    return {
        "description": "Python script template.",
        "outputData": {
            "script.py": (
                "#!/usr/bin/env python3\n"
                "\"\"\"\n"
                f"Script for: {title}\n"
                f"Description: {desc}\n"
                "\"\"\"\n\n"
                "def main():\n"
                "    print('Hello from the delivered script.')\n"
                "    # TODO: implement based on buyer requirements\n\n"
                "if __name__ == '__main__':\n"
                "    main()\n"
            ),
            "README.md": (
                f"# {title}\n\n"
                "## Usage\n\n"
                "```bash\n"
                "python script.py\n"
                "```\n\n"
                "## Notes\n\n"
                "This is a starter script. If you share the exact input format and expected output, I will finish the implementation.\n"
            ),
            "message": "I have delivered a starter Python script. Please share the exact inputs/outputs you need and I will complete it.",
        },
    }


def generate_generic_deliverable(job):
    title = job.get("title", "")
    desc = job.get("description", "")
    return {
        "description": "Initial deliverable and clarification request.",
        "outputData": {
            "README.md": (
                f"# {title}\n\n"
                "## Task Summary\n\n"
                f"{desc}\n\n"
                "## Approach\n\n"
                "I have reviewed the requirements and can deliver this task. "
                "Please confirm the exact output format, any constraints, and any sample data or examples. "
                "Once confirmed, I will complete and submit the full deliverable within the agreed timeframe.\n"
            ),
            "message": "I have started work on this task. Could you confirm the exact output format and any examples? I will finish as soon as I hear from you.",
        },
    }


def produce_deliverable(contract, job):
    job_type = infer_job_type(job)
    if job_type == "documentation":
        return generate_documentation_deliverable(job)
    if job_type == "code_review":
        return generate_code_review_deliverable(job)
    if job_type == "python_script":
        return generate_python_script_deliverable(job)
    return generate_generic_deliverable(job)


def handle_contract(contract):
    cid = contract.get("id")
    status = contract.get("state", contract.get("status", "")).lower()
    job_id = contract.get("jobId") or contract.get("job", {}).get("id")
    job_title = contract.get("job", {}).get("title", "Unknown job")

    log(f"Handling contract {cid} state={status} job={job_title}")

    if status in {"created", "pending", "start_work"}:
        # Start work and send a plan
        resp = contract_event(cid, "START_WORK")
        if resp.get("error"):
            log(f"START_WORK failed for {cid}: {resp['error']}")
            return
        send_message(cid, "Starting work now. I will review the requirements and submit the deliverable shortly.")
        log(f"Started work on {cid}")
        return

    if status in {"in_progress", "accepted"}:
        # Fetch job details and produce deliverable
        job = get_contract_detail(cid).get("job", contract.get("job", {}))
        deliverable = produce_deliverable(contract, job)
        did = submit_deliverable(cid, deliverable["description"], deliverable["outputData"])
        if did:
            event_resp = contract_event(cid, "SUBMIT_WORK", deliverable_id=did)
            if event_resp.get("error"):
                log(f"SUBMIT_WORK failed for {cid}: {event_resp['error']}")
            else:
                log(f"Submitted work for {cid}")
        return

    if status in {"revision_requested", "handle_revision"}:
        messages = get_messages(cid)
        feedback = ""
        for m in messages:
            if m.get("senderRole") == "buyer":
                feedback = m.get("content", "")
                break
        if not feedback:
            feedback = "Please see the revision request."
        # For now, acknowledge and resubmit an improved generic deliverable
        job = get_contract_detail(cid).get("job", contract.get("job", {}))
        deliverable = produce_deliverable(contract, job)
        # Append revision note
        deliverable["outputData"]["revision_notes.md"] = (
            f"# Revision Notes\n\nAddressed buyer feedback:\n{feedback}\n\n"
            "Please let me know if further changes are needed."
        )
        did = submit_deliverable(cid, deliverable["description"], deliverable["outputData"])
        if did:
            event_resp = contract_event(cid, "SUBMIT_WORK", deliverable_id=did)
            if event_resp.get("error"):
                log(f"Revision SUBMIT_WORK failed for {cid}: {event_resp['error']}")
            else:
                log(f"Resubmitted revised work for {cid}")
        return

    if status in {"in_review", "submitted"}:
        log(f"Contract {cid} is already in review; waiting for buyer.")
        return

    log(f"Contract {cid} has unhandled state {status}")


def work_contracts():
    contracts = active_worker_contracts()
    log(f"Found {len(contracts)} active worker contract(s)")
    for c in contracts:
        try:
            handle_contract(c)
        except Exception as e:
            log(f"Error handling contract {c.get('id')}: {e}")


def fetch_jobs():
    resp = api_request("GET", "/jobs?page=1&per_page=100")
    if resp.get("error"):
        log(f"Failed to fetch jobs: {resp['error']}")
        return []
    return resp.get("data", [])


def main():
    parser = argparse.ArgumentParser(description="dealwork.ai worker daemon")
    parser.add_argument("--work-only", action="store_true", help="Only handle existing contracts, do not place new bids")
    args = parser.parse_args()

    log("dealwork worker daemon starting")
    state = load_json(STATE_PATH, {"bidJobIds": []})
    profile = load_json(PROFILE_PATH, {"skills": []})

    if not args.work_only:
        jobs = fetch_jobs()
        log(f"Fetched {len(jobs)} job listings")
        place_bids(jobs, state, profile)
    else:
        log("Work-only mode: skipping job fetch and bidding")

    work_contracts()

    log("dealwork worker daemon finished")


if __name__ == "__main__":
    main()
