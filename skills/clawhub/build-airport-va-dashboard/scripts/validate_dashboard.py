#!/usr/bin/env python3
"""Static contract checks for generated Airport VA dashboard HTML files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_TOKENS = {
    "Excel file input": r"<input[^>]+type=[\"']file[\"'][^>]*>",
    "Excel extension filter": r"accept=[\"'][^\"']*\.xlsx",
    "workbook parser": r"\bXLSX\.(?:read|readFile)\b",
    "chart library": r"\b(?:new\s+Chart|Chart\s*\()",
    "parseExcel function": r"\bparseExcel\b",
    "normalizeRows function": r"\bnormalizeRows\b",
    "applyFilters function": r"\bapplyFilters\b",
    "aggregateData function": r"\baggregateData\b",
    "calculateComparison function": r"\bcalculateComparison\b",
    "renderDashboard function": r"\brenderDashboard\b",
    "showDataQuality function": r"\bshowDataQuality\b",
    "camera column": r"Camera_Name",
    "timestamp column": r"Timestamp",
    "gender column": r"Gender",
    "age lower column": r"Age_Lower_Limit",
    "age upper column": r"Age_Up_Limit",
    "eyewear column": r"Glass_style",
    "date-from control": r"dateFrom",
    "date-to control": r"dateTo",
    "hour-from control": r"hourFrom",
    "hour-to control": r"hourTo",
    "comparison control": r"cmpMode",
    "reset control": r"resetBtn",
    "data status": r"Data (?:Quality|Status)",
}

REQUIRED_LABELS = (
    "Total Detections",
    "Peak Hour",
    "Daily Footfall Trend",
    "Hourly Traffic Pattern",
    "Traffic by Day of Week",
    "Gender Distribution",
    "Age Group Distribution",
    "Eyewear Detection",
    "Camera Comparison",
    "Daily Footfall by Camera",
)

WARN_PATTERNS = {
    "hardcoded legacy record total": r"360\s*,\s*228\s+records",
    "hardcoded legacy date range": r"17\s+Jun\s*(?:&ndash;|–|-)\s*24\s+Jun\s+2026",
    "possible demographic proportional scaling": r"(?:gender|age|glass).{0,100}\*\s*scale",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Generated dashboard HTML")
    args = parser.parse_args()

    if not args.html.is_file():
        print(f"ERROR: file not found: {args.html}")
        return 2

    text = args.html.read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []
    warnings: list[str] = []

    if "<html" not in text.lower() or "</html>" not in text.lower():
        errors.append("not a complete HTML document")

    for label, pattern in REQUIRED_TOKENS.items():
        if not re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            errors.append(f"missing {label}")

    plain = re.sub(r"<[^>]+>", " ", text)
    for label in REQUIRED_LABELS:
        if label.lower() not in plain.lower():
            errors.append(f"missing visible section: {label}")

    if not re.search(r"drag|drop", text, re.IGNORECASE):
        errors.append("missing drag-and-drop upload behavior or copy")

    if not re.search(r"partial|incomplete|latest timestamp", text, re.IGNORECASE):
        warnings.append("no obvious partial-day handling/status copy")

    for label, pattern in WARN_PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            warnings.append(label)

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    print(f"Checked {args.html}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
