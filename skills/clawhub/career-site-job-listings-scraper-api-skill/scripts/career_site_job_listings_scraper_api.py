import datetime
import io
import json
import os
import sys
import time

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

TEMPLATE_ID = "113866428018349479"
API_BASE_URL = "https://api.browseract.com/v3/bots"
API_KEY_URL = "https://www.browseract.com/reception/integrations?co-from=career-site-job-listings-scraper"


def run_task(api_key, company_career_url='https://openai.com/careers', count='1'):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "input": {
            "company_career_url": company_career_url,
            "count": count,
        }
    }

    print("Start Task", flush=True)
    try:
        response = requests.post(
            f"{API_BASE_URL}/templates/{TEMPLATE_ID}/runs",
            json=payload,
            headers=headers,
            timeout=30,
        ).json()
    except Exception as exc:
        print(f"Error: Connection to API failed - {exc}", flush=True)
        return None

    task_id = response.get("task_id") or response.get("id")
    if not task_id:
        response_text = str(response)
        if "Invalid authorization" in response_text:
            print("Error: Invalid authorization. Please check your BrowserAct API Key.", flush=True)
        elif "concurrent" in response_text.lower() or "too many running tasks" in response_text.lower():
            print("Error: Concurrent task limit reached. Please upgrade your plan at https://www.browseract.com/reception/recharge?co-from=career-site-job-listings-scraper", flush=True)
        else:
            print(f"Error: Could not start task. Response: {response}", flush=True)
        return None

    print(f"Task started. ID: {task_id}", flush=True)
    deadline = time.time() + 900
    while time.time() < deadline:
        try:
            status_response = requests.get(
                f"{API_BASE_URL}/runs/{task_id}/status",
                headers=headers,
                timeout=30,
            ).json()
            status = status_response.get("status")
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Task Status: {status}", flush=True)

            if status == "finished":
                print(f"[{timestamp}] Task finished successfully.", flush=True)
                break
            if status in ["failed", "canceled"]:
                print(f"Error: Task {status}. Please check your BrowserAct dashboard.", flush=True)
                return None
        except Exception as exc:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Polling error: {exc}. Retrying...", flush=True)
        time.sleep(10)
    else:
        print("Error: Task polling timed out after 900 seconds.", flush=True)
        return None

    try:
        result = requests.get(
            f"{API_BASE_URL}/runs/{task_id}",
            headers=headers,
            timeout=30,
        ).json()
        return json.dumps(result, ensure_ascii=False)
    except Exception as exc:
        print(f"Error: Failed to retrieve results - {exc}", flush=True)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python career_site_job_listings_scraper_api.py <company_career_url> [count]", flush=True)
        sys.exit(1)

    api_key = os.getenv("BROWSERACT_API_KEY")
    if not api_key:
        print("\n[!] ERROR: BrowserAct API Key is missing.", flush=True)
        print("Please follow these steps:", flush=True)
        print(f"1. Go to: {API_KEY_URL}", flush=True)
        print("2. Copy your API Key.", flush=True)
        print("3. Provide it to me or set it as an environment variable (BROWSERACT_API_KEY).", flush=True)
        sys.exit(1)

    company_career_url = sys.argv[1] if len(sys.argv) > 1 else 'https://openai.com/careers'
    count = sys.argv[2] if len(sys.argv) > 2 else '1'
    output = run_task(api_key, company_career_url, count)
    if output:
        print(output, flush=True)
