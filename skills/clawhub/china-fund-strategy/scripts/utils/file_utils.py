"""
File Utilities

Provides file and directory operations for the fund analysis system.
"""

import os
import json
from pathlib import Path
from datetime import datetime


def ensure_directories(base_path, fund_code):
    """
    Ensure directory structure exists for fund analysis.
    
    Args:
        base_path: Base path for analysis data
        fund_code: Fund code to create directories for
        
    Returns:
        tuple: (base_dir, today_dir) Path objects
    """
    base_dir = Path(base_path) / fund_code
    today_dir = base_dir / datetime.now().strftime("%Y-%m-%d")
    
    base_dir.mkdir(parents=True, exist_ok=True)
    today_dir.mkdir(exist_ok=True)
    
    return base_dir, today_dir


def save_report(report_content, base_dir, fund_code, suffix=""):
    """
    Save analysis report to file.
    
    Args:
        report_content: Complete report text
        base_dir: Base directory for the fund
        fund_code: Fund code
        suffix: Optional suffix for filename (e.g., "_akshare")
        
    Returns:
        Path: Path to the saved report file
    """
    today_dir = base_dir / datetime.now().strftime("%Y-%m-%d")
    today_dir.mkdir(exist_ok=True)
    
    # Main report in fund directory
    main_report_file = base_dir / f"{fund_code}_analysis.md"
    with open(main_report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    # Dated report with suffix
    dated_report_file = today_dir / f"{fund_code}_analysis{suffix}.md"
    with open(dated_report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return main_report_file


def save_raw_data(data, source, fund_code, base_dir):
    """
    Save raw data from data source.
    
    Args:
        data: Raw data records
        source: Data source identifier
        fund_code: Fund code
        base_dir: Base directory for the fund
        
    Returns:
        Path: Path to the saved raw data file
    """
    today_dir = base_dir / datetime.now().strftime("%Y-%m-%d")
    today_dir.mkdir(exist_ok=True)
    
    raw_data_path = today_dir / f"raw_data_{source}.json"
    with open(raw_data_path, 'w', encoding='utf-8') as f:
        json.dump({
            'source': source,
            'fund_code': fund_code,
            'fetch_time': datetime.now().isoformat(),
            'records': data
        }, f, ensure_ascii=False, indent=2)
    
    return raw_data_path