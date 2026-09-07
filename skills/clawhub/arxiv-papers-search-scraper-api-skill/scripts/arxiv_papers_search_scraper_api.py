import os
import time
import requests
import json
import sys
import datetime
import io

# Force UTF-8 encoding for standard output and error streams
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# API Configuration
TEMPLATE_ID = '113866388981961639'
API_BASE_URL = "https://api.browseract.com/v3/bots"
API_KEY_URL = 'https://www.browseract.com/reception/integrations?co-from=arxiv-papers-search-scraper'


def run_arxiv_papers_search_scraper_task(api_key, base_url='https://arxiv.org', keyword='large language model', search_type='all', count='20'):
    """
    Starts a BrowserAct template task and polls for completion.
    Returns structured data as a string, or None on failure.
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "input": {
            "base_url": base_url,
            "keyword": keyword,
            "search_type": search_type,
            "count": count,
        }
    }

    # 1. Start Task
    print("Start Task", flush=True)
    try:
        res = requests.post(
            f"{API_BASE_URL}/templates/{TEMPLATE_ID}/runs",
            json=payload, headers=headers, timeout=30
        ).json()
    except Exception as e:
        print(f"Error: Connection to API failed - {e}", flush=True)
        return None

    task_id = res.get("task_id") or res.get("id")
    if not task_id:
        res_str = str(res)
        if "Invalid authorization" in res_str:
            print("Error: Invalid authorization. Please check your BrowserAct API Key.", flush=True)
        elif "concurrent" in res_str.lower() or "too many running tasks" in res_str.lower():
            print("Error: Concurrent task limit reached. Please upgrade your plan at https://www.browseract.com/reception/recharge", flush=True)
        else:
            print(f"Error: Could not start task. Response: {res}", flush=True)
        return None

    print(f"Task started. ID: {task_id}", flush=True)

    # 2. Poll for Completion
    max_poll_time = 900
    poll_start = time.time()
    finished = False
    while time.time() - poll_start < max_poll_time:
        try:
            status_res = requests.get(
                f"{API_BASE_URL}/runs/{task_id}/status",
                headers=headers, timeout=30
            ).json()
            status = status_res.get("status")

            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Task Status: {status}", flush=True)

            if status == "finished":
                print(f"[{timestamp}] Task finished successfully.", flush=True)
                finished = True
                break
            elif status in ["failed", "canceled"]:
                print(f"Error: Task {status}. Please check your BrowserAct dashboard.", flush=True)
                return None
        except Exception as e:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Polling error: {e}. Retrying...", flush=True)

        time.sleep(10)

    if not finished:
        print(f"Error: Task polling timed out after {max_poll_time} seconds.", flush=True)
        return None

    # 3. Get Results
    try:
        task_info = requests.get(
            f"{API_BASE_URL}/runs/{task_id}",
            headers=headers, timeout=30
        ).json()
        return json.dumps(task_info, ensure_ascii=False)
    except Exception as e:
        print(f"Error: Failed to retrieve results - {e}", flush=True)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python arxiv_papers_search_scraper_api.py <base_url> [keyword] [search_type] [count]", flush=True)
        sys.exit(1)

    api_key = os.getenv("BROWSERACT_API_KEY")
    if not api_key:
        print("\n[!] ERROR: BrowserAct API Key is missing.", flush=True)
        print("Please follow these steps:", flush=True)
        print(f"1. Go to: {API_KEY_URL}", flush=True)
        print("2. Copy your API Key.", flush=True)
        print("3. Provide it to me or set it as an environment variable (BROWSERACT_API_KEY).", flush=True)
        sys.exit(1)

    base_url = sys.argv[1] if len(sys.argv) > 1 else 'https://arxiv.org'
    keyword = sys.argv[2] if len(sys.argv) > 2 else 'large language model'
    search_type = sys.argv[3] if len(sys.argv) > 3 else 'all'
    count = sys.argv[4] if len(sys.argv) > 4 else '20'

    result = run_arxiv_papers_search_scraper_task(api_key, base_url, keyword, search_type, count)
    if result:
        print(result, flush=True)
