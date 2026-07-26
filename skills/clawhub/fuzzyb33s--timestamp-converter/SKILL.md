---
name: timestamp-converter
description: Convert between Unix timestamps and human-readable datetime formats. Use when user wants to convert timestamps, parse dates, format dates in different timezones, or calculate time differences. Supports: Unix timestamp (seconds/ms), ISO 8601, RFC 2822, custom formats, and timezone conversions.
---

# Timestamp Converter

Convert Unix timestamps to readable dates and vice versa. Pure Python stdlib.

## Usage

```bash
python scripts/timestamp_converter.py convert <timestamp>          # Unix → readable
python scripts/timestamp_converter.py parse "<date string>"        # Parse date string
python scripts/timestamp_converter.py now [--unix] [--iso]         # Current time
python scripts/timestamp_converter.py diff <ts1> <ts2>             # Time difference
python scripts/timestamp_converter.py add <timestamp> <seconds>    # Add/subtract seconds
```

## Options

| Flag | Description |
|------|-------------|
| `--tz` | Timezone (e.g., UTC, America/New_York, Europe/London). Default: local. |
| `--format` | Custom strftime format |
| `--unix` | Output as Unix timestamp |
| `--iso` | Output as ISO 8601 |
| `--ms` | Timestamp in milliseconds |

## Examples

| Input | Output |
|-------|--------|
| `convert 1750790400` | 2026-06-24 00:00:00 UTC |
| `convert 1750790400000 --ms` | 2026-06-24 00:00:00 UTC |
| `parse "2026-06-24 12:30:00"` | 1750786200 |
| `now --unix` | 1750791742 |
| `now --iso` | 2026-06-24T07:09:02+02:00 |
| `diff 1750790400 1750794000` | 1h 0m 0s |
| `add 1750790400 3600` | 1750794000 -> 2026-06-24 01:00:00 |

## Notes

- Timestamps in milliseconds auto-detected (13+ digits)
- Supports relative dates: "yesterday", "tomorrow", "next monday"
- Use `--tz` flag for timezone-aware conversions