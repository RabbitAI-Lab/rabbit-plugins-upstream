#!/usr/bin/env python3
"""Timestamp Converter — convert between Unix timestamps and human-readable dates."""

import sys
import argparse
from datetime import datetime, timezone, timedelta
import time as time_module
import re


def parse_date_string(date_str: str) -> datetime | None:
    """Try to parse a date string into a datetime object."""
    # Try common formats
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d",
        "%d/%m/%Y %H:%M:%S",
        "%m/%d/%Y %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%b %d, %Y %H:%M:%S",
        "%B %d, %Y %H:%M:%S",
    ]
    # Handle Z suffix
    date_str_clean = date_str.replace('Z', '+00:00')
    for fmt in formats:
        try:
            return datetime.strptime(date_str_clean, fmt)
        except ValueError:
            pass
    return None


def parse_relative_date(date_str: str) -> datetime | None:
    """Parse relative date strings like 'yesterday', 'tomorrow', 'next monday'."""
    now = datetime.now()
    date_str_lower = date_str.strip().lower()
    
    if date_str_lower == "now":
        return now
    if date_str_lower == "today":
        return now.replace(hour=0, minute=0, second=0, microsecond=0)
    if date_str_lower == "yesterday":
        return (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    if date_str_lower == "tomorrow":
        return (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    # "next monday" etc.
    days_map = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
                "friday": 4, "saturday": 5, "sunday": 6}
    for day_name, day_num in days_map.items():
        if date_str_lower == f"next {day_name}":
            current_day = now.weekday()
            days_ahead = day_num - current_day
            if days_ahead <= 0:
                days_ahead += 7
            days_ahead += 7  # next occurrence
            return (now + timedelta(days=days_ahead)).replace(hour=0, minute=0, second=0, microsecond=0)
        if date_str_lower == f"{day_name}":
            current_day = now.weekday()
            days_ahead = day_num - current_day
            if days_ahead <= 0:
                days_ahead += 7
            return (now + timedelta(days=days_ahead)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    return None


def convert_timestamp(ts: str, tz: str | None, output_format: str | None, as_unix: bool, as_iso: bool, as_ms: bool) -> str:
    """Convert a Unix timestamp to human-readable format."""
    ts = ts.strip()
    is_ms = len(ts) >= 13 or as_ms
    
    try:
        if is_ms:
            ts_int = int(ts)
            if ts_int > 1e12:
                ts_int = ts_int // 1000
        else:
            ts_int = int(ts)
    except ValueError:
        return f"Error: '{ts}' is not a valid timestamp"
    
    dt = datetime.fromtimestamp(ts_int, tz=timezone.utc)
    if tz and tz != "UTC":
        from zoneinfo import ZoneInfo
        try:
            dt = dt.astimezone(ZoneInfo(tz))
        except Exception:
            pass  # Keep UTC if timezone is invalid
    
    if as_unix:
        return str(int(dt.timestamp()))
    if as_iso:
        return dt.isoformat()
    if output_format:
        return dt.strftime(output_format)
    
    tz_name = tz if tz else "UTC"
    return f"{dt.strftime('%Y-%m-%d %H:%M:%S')} {tz_name}"


def parse_datetime(date_str: str, tz: str | None, as_unix: bool, as_iso: bool) -> str:
    """Parse a date string and convert to timestamp."""
    dt = parse_date_string(date_str)
    if dt is None:
        dt = parse_relative_date(date_str)
    
    if dt is None:
        # Try letting datetime handle it directly
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except ValueError:
            return f"Error: Could not parse '{date_str}'"
    
    # Make timezone-aware if not already
    if dt.tzinfo is None:
        if tz:
            from zoneinfo import ZoneInfo
            try:
                dt = dt.replace(tzinfo=ZoneInfo(tz))
            except Exception:
                dt = dt.replace(tzinfo=timezone.utc)
        else:
            dt = dt.replace(tzinfo=timezone.utc)
    
    if as_iso:
        return dt.isoformat()
    return str(int(dt.timestamp()))


def get_now(as_unix: bool, as_iso: bool) -> str:
    """Get current timestamp."""
    now = datetime.now(timezone.utc)
    if as_unix:
        return str(int(now.timestamp()))
    if as_iso:
        return now.isoformat()
    return now.strftime("%Y-%m-%d %H:%M:%S UTC")


def diff_timestamps(ts1: str, ts2: str) -> str:
    """Calculate difference between two timestamps."""
    try:
        def parse(ts: str) -> int:
            ts = ts.strip()
            if len(ts) >= 13:
                v = int(ts)
                return v // 1000 if v > 1e12 else v
            return int(ts)
        
        t1, t2 = parse(ts1), parse(ts2)
        diff = abs(t2 - t1)
        
        days = diff // 86400
        hours = (diff % 86400) // 3600
        minutes = (diff % 3600) // 60
        seconds = diff % 60
        
        parts = []
        if days:
            parts.append(f"{days}d")
        if hours or days:
            parts.append(f"{hours}h")
        if minutes or days or hours:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")
        
        return " ".join(parts)
    except ValueError as e:
        return f"Error: {e}"


def add_seconds(ts: str, seconds: str, tz: str | None) -> str:
    """Add or subtract seconds from a timestamp."""
    try:
        ts_int = int(ts.strip())
        if ts_int > 1e12:
            ts_int = ts_int // 1000
        
        add_int = int(seconds)
        new_ts = ts_int + add_int
        
        dt = datetime.fromtimestamp(new_ts, tz=timezone.utc)
        if tz:
            from zoneinfo import ZoneInfo
            try:
                dt = dt.astimezone(ZoneInfo(tz))
                tz_name = tz
            except Exception:
                tz_name = "UTC"
        else:
            tz_name = "UTC"
        
        return f"{new_ts} -> {dt.strftime('%Y-%m-%d %H:%M:%S')} {tz_name}"
    except ValueError as e:
        return f"Error: {e}"


def main():
    parser = argparse.ArgumentParser(description="Timestamp Converter")
    sub = parser.add_subparsers(dest="command", required=True)
    
    conv = sub.add_parser("convert", help="Convert timestamp to readable date")
    conv.add_argument("timestamp", help="Unix timestamp (seconds or milliseconds)")
    conv.add_argument("--tz", default=None, help="Timezone (e.g., America/New_York)")
    conv.add_argument("--format", default=None, help="Custom strftime format")
    conv.add_argument("--unix", action="store_true", help="Output as Unix timestamp")
    conv.add_argument("--iso", action="store_true", help="Output as ISO 8601")
    conv.add_argument("--ms", action="store_true", help="Timestamp is in milliseconds")
    
    parse_cmd = sub.add_parser("parse", help="Parse date string to timestamp")
    parse_cmd.add_argument("date_string", help="Date string to parse")
    parse_cmd.add_argument("--tz", default=None, help="Timezone")
    parse_cmd.add_argument("--unix", action="store_true", help="Output as Unix timestamp")
    parse_cmd.add_argument("--iso", action="store_true", help="Output as ISO 8601")
    
    now_cmd = sub.add_parser("now", help="Current time")
    now_cmd.add_argument("--unix", action="store_true", help="Output as Unix timestamp")
    now_cmd.add_argument("--iso", action="store_true", help="Output as ISO 8601")
    
    diff_cmd = sub.add_parser("diff", help="Time difference between two timestamps")
    diff_cmd.add_argument("ts1", help="First timestamp")
    diff_cmd.add_argument("ts2", help="Second timestamp")
    
    add_cmd = sub.add_parser("add", help="Add seconds to timestamp")
    add_cmd.add_argument("timestamp", help="Base timestamp")
    add_cmd.add_argument("seconds", help="Seconds to add (negative to subtract)")
    add_cmd.add_argument("--tz", default=None, help="Timezone")
    
    args = parser.parse_args()
    
    if args.command == "convert":
        result = convert_timestamp(args.timestamp, args.tz, args.format, args.unix, args.iso, args.ms)
    elif args.command == "parse":
        result = parse_datetime(args.date_string, args.tz, args.unix, args.iso)
    elif args.command == "now":
        result = get_now(args.unix, args.iso)
    elif args.command == "diff":
        result = diff_timestamps(args.ts1, args.ts2)
    elif args.command == "add":
        result = add_seconds(args.timestamp, args.seconds, args.tz)
    else:
        result = "Unknown command"
    
    print(result)


if __name__ == "__main__":
    main()