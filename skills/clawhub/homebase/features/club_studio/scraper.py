#!/usr/bin/env python3
"""
Club Studio Scraper
Fetches the daily schedule for Club Studio Irvine.
Uses Playwright via system python3 to bypass bot protection.
"""

import json
import subprocess
from datetime import datetime
from typing import List, Dict

def fetch_daily_schedule() -> List[Dict]:
    """
    Fetches today's schedule for Club Studio Irvine (Club ID 1347).
    """
    today = datetime.now().strftime("%Y-%m-%d")
    script = '''
import json
import re
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page.goto('https://www.clubstudiofitness.com/Pages/ClassReservation.aspx?clubid=1347', timeout=60000)
        page.wait_for_timeout(2000)
        html = page.content()
        browser.close()
        
        times = re.findall(r'<p class="time-v">([^<]+)</p>', html)
        names = re.findall(r'<span[^>]*class="ClassNameColor"[^>]*>([^<]+)</span>', html)
        instructors = re.findall(r'</h4>[\\s\\S]*?<h4>([^<]+)</h4>', html)
        
        classes = []
        for i in range(min(len(times), len(names))):
            try:
                # Basic duration assumption
                name_lower = names[i].lower()
                duration = 45 if ("ride" in name_lower or "cycle" in name_lower or "hiit" in name_lower) else 60
                
                inst = instructors[i].strip() if i < len(instructors) else "TBD"
                
                classes.append({
                    "name": names[i].strip(),
                    "time": times[i].strip(),
                    "duration_minutes": duration,
                    "instructor": inst
                })
            except Exception:
                pass
        
        print(json.dumps(classes))

if __name__ == '__main__':
    run()
'''
    try:
        # Run using global python3 which has playwright installed
        result = subprocess.run(["python3", "-c", script], capture_output=True, text=True, check=True)
        raw_classes = json.loads(result.stdout.strip())
        
        processed = []
        last_dt = None
        
        for c in raw_classes:
            try:
                dt = datetime.strptime(c["time"], "%I:%M %p")
                
                # Detect if we crossed into tomorrow (e.g. went from 8PM back to 5AM)
                if last_dt and dt < last_dt and (last_dt - dt).total_seconds() > 3600 * 4:
                    break
                
                last_dt = dt
                
                c["time"] = dt.strftime("%H:%M")
                c["date"] = today
                processed.append(c)
            except Exception:
                pass
                
        return processed
    except Exception as e:
        print(f"Failed to fetch schedule: {e}")
        if isinstance(e, subprocess.CalledProcessError):
            print("Stderr:", e.stderr)
        return []

if __name__ == "__main__":
    print(json.dumps(fetch_daily_schedule(), indent=2))
