import datetime
import io
import json
import os
import sys
import time

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

TEMPLATE_ID = "113864423413657511"
API_BASE_URL = "https://api.browseract.com/v3/bots"
API_KEY_URL = "https://www.browseract.com/reception/integrations?co-from=facebook-ads-library-scraper"


def run_task(api_key, search_keyword='Claude Code', region='United States', date_range_days='30', max_ad_count='10'):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "input": {
            "search_keyword": search_keyword,
            "region": region,
            "date_range_days": date_range_days,
            "max_ad_count": max_ad_count,
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
            print("Error: Concurrent task limit reached. Please upgrade your plan at https://www.browseract.com/reception/recharge?co-from=facebook-ads-library-scraper", flush=True)
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
        print("Usage: python facebook_ads_library_scraper_api.py <search_keyword> [region] [date_range_days] [max_ad_count]", flush=True)
        sys.exit(1)

    api_key = os.getenv("BROWSERACT_API_KEY")
    if not api_key:
        print("\n[!] ERROR: BrowserAct API Key is missing.", flush=True)
        print("Please follow these steps:", flush=True)
        print(f"1. Go to: {API_KEY_URL}", flush=True)
        print("2. Copy your API Key.", flush=True)
        print("3. Provide it to me or set it as an environment variable (BROWSERACT_API_KEY).", flush=True)
        sys.exit(1)

    search_keyword = sys.argv[1] if len(sys.argv) > 1 else 'Claude Code'
    region = sys.argv[2] if len(sys.argv) > 2 else 'United States'
    date_range_days = sys.argv[3] if len(sys.argv) > 3 else '30'
    max_ad_count = sys.argv[4] if len(sys.argv) > 4 else '10'
    output = run_task(api_key, search_keyword, region, date_range_days, max_ad_count)
    if output:
        print(output, flush=True)
