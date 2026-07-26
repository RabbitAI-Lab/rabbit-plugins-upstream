from __future__ import annotations

from typing import Optional

from scripts.call_api import call_api
from scripts.config import settings

def get_current_time(
    timezone: str
) -> Dict[str, Any]:
    """
    Get current time in a specific timezones
    
    Args:
        timezone: IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use 'Etc/UTC' as local timezone if no timezone provided by the user.
    
    Returns:
        
    """
    arguments = {
        "timezone": timezone
    }
    
    return call_api("1777419077074947", "get_current_time", arguments)

def convert_time(
    source_timezone: str,
    time: str,
    target_timezone: str
) -> Dict[str, Any]:
    """
    Convert time between timezones
    
    Args:
        source_timezone: Source IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use 'Etc/UTC' as local timezone if no source timezone provided by the user.
        time: Time to convert in 24-hour format (HH:MM)
        target_timezone: Target IANA timezone name (e.g., 'Asia/Tokyo', 'America/San_Francisco'). Use 'Etc/UTC' as local timezone if no target timezone provided by the user.
    
    Returns:
        
    """
    arguments = {
        "source_timezone": source_timezone,
        "time": time,
        "target_timezone": target_timezone
    }
    
    return call_api("1777419077074947", "convert_time", arguments)

