#!/usr/bin/env python3
"""
Club Studio Recommender
Matches Club Studio schedule against calendar free time.
"""

from datetime import datetime, timedelta
from typing import List, Dict
import os
import sys

# Add homebase to path if run standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from features.club_studio.scraper import fetch_daily_schedule
from features.calendar.calendar_aggregator import FamilyCalendarAggregator

def time_str_to_dt(time_str: str, date_str: str) -> datetime:
    """Convert HH:MM and YYYY-MM-DD to a datetime object."""
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

def get_club_studio_suggestions() -> str:
    """
    Fetches the schedule and checks against the calendar for free blocks.
    Returns a formatted message for WhatsApp.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 1. Fetch gym classes
    try:
        classes = fetch_daily_schedule()
    except Exception as e:
        return f"❌ Failed to fetch Club Studio schedule: {e}"
        
    if not classes:
        return "No classes available at Club Studio today."

    # 2. Sync and fetch calendar events
    # We use the current directory if run from homebase root
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    agg = FamilyCalendarAggregator(base_path)
    
    try:
        agg.sync_with_google_calendar()
    except Exception as e:
        print(f"Warning: Calendar sync failed: {e}")
        
    cal_events = agg.get_events_by_date(today_str)
    
    # Filter out "All day" events which usually don't have a specific time block
    time_blocked_events = [e for e in cal_events if e.get("time") and e.get("time") != "All day"]
    
    # Calculate busy blocks with 30-min buffers
    busy_blocks = []
    BUFFER_MINS = 30
    
    for event in time_blocked_events:
        start_time_str = event.get("time")
        end_time_str = event.get("end_time")
        
        if not start_time_str or not end_time_str:
            continue
            
        try:
            event_start = time_str_to_dt(start_time_str, today_str)
            event_end = time_str_to_dt(end_time_str, today_str)
            
            # Apply buffers
            blocked_start = event_start - timedelta(minutes=BUFFER_MINS)
            blocked_end = event_end + timedelta(minutes=BUFFER_MINS)
            
            busy_blocks.append((blocked_start, blocked_end, event.get("title")))
        except Exception:
            continue

    # 3. Match classes against free time
    available_classes = []
    
    for c in classes:
        try:
            class_start = time_str_to_dt(c["time"], today_str)
            class_end = class_start + timedelta(minutes=c["duration_minutes"])
            
            # Check overlap
            overlap = False
            for b_start, b_end, title in busy_blocks:
                # Overlap condition: max(start1, start2) < min(end1, end2)
                if max(class_start, b_start) < min(class_end, b_end):
                    overlap = True
                    break
                    
            # Skip past classes
            if class_start < datetime.now():
                continue
                
            if not overlap:
                available_classes.append(c)
        except Exception:
            continue
            
    # 4. Format Message
    if not available_classes:
        return "NO_REPLY"
        
    lines = [
        "🏋️ *Club Studio Class Suggestions*",
        f"Here are the classes that fit your schedule today ({today_str}):",
        ""
    ]
    
    for c in available_classes:
        end_time_str = (time_str_to_dt(c["time"], today_str) + timedelta(minutes=c["duration_minutes"])).strftime("%I:%M %p")
        start_time_str = time_str_to_dt(c["time"], today_str).strftime("%I:%M %p")
        lines.append(f"• *{c['name']}* at {start_time_str} - {end_time_str} (with {c['instructor']})")
        
    lines.append("")
    lines.append("_Reply to this message if you'd like me to book one of these!_")
    
    return "\n".join(lines)

if __name__ == "__main__":
    print(get_club_studio_suggestions())
