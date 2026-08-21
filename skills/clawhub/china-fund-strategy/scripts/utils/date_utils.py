"""
Date Utilities

Provides date parsing and handling functions for the fund analysis system.
"""

from datetime import datetime


def parse_date(date_str, fmt='%Y-%m-%d'):
    """
    Parse a date string into a datetime object.
    
    Args:
        date_str: Date string to parse
        fmt: Expected format of the date string
        
    Returns:
        datetime: Parsed datetime object, or None if parsing fails
    """
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None


def format_date(date_obj, fmt='%Y-%m-%d'):
    """
    Format a datetime object as a string.
    
    Args:
        date_obj: datetime object to format
        fmt: Desired output format
        
    Returns:
        str: Formatted date string, or empty string if input is None
    """
    if date_obj is None:
        return ""
    return date_obj.strftime(fmt)


def days_between(start_date, end_date):
    """
    Calculate the number of days between two dates.
    
    Args:
        start_date: Start date (datetime object)
        end_date: End date (datetime object)
        
    Returns:
        int: Number of days between dates
    """
    return (end_date - start_date).days


def estimate_trading_days(days_diff):
    """
    Estimate trading days from calendar days (rough estimate).
    
    Args:
        days_diff: Number of calendar days
        
    Returns:
        int: Estimated number of trading days
    """
    return int(days_diff * 5 / 7)