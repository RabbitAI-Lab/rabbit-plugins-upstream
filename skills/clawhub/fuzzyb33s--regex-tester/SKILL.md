---
name: regex-tester
description: Test and debug regular expressions with real-time matching, group extraction, and common pattern library. Use when a user asks to test, debug, validate, or explain a regex pattern, or needs to extract data using regex from text.
---

# regex-tester

Test and debug regular expressions with real-time matching and group extraction.

## Usage

```bash
python scripts/regex_tester.py --pattern "<regex>" [--text "<test string>"] [--flags i|m|s] [--list-patterns]
```

## Arguments

| Argument | Description |
|----------|-------------|
| `--pattern` | Regex pattern to test (required) |
| `--text` | Test string to match against (default: reads from stdin) |
| `--flags` | Flags: `i` (ignore case), `m` (multiline), `s` (dotall) |
| `--json` | Output results as JSON |
| `--list-patterns` | Show common pattern library |

## Exit Codes

- `0` = match found
- `1` = no match
- `2` = invalid regex

## Common Patterns

| Pattern Name | Regex | Description |
|---|---|---|
| `email` | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Email address |
| `url` | `https?://[^\s]+` | HTTP/HTTPS URL |
| `ipv4` | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` | IPv4 address |
| `uuid` | `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` | UUID |
| `phone` | `\+?[\d\s\-()]{10,}` | Phone number |
| `date-iso` | `\d{4}-\d{2}-\d{2}` | ISO date (YYYY-MM-DD) |
| `time-24h` | `([01]?\d|2[0-3]):[0-5]\d` | 24-hour time |
| `hex-color` | `#[0-9a-fA-F]{3,8}` | Hex color code |
| `slug` | `[a-z0-9]+(?:-[a-z0-9]+)*` | URL slug |
| `credit-card` | `\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}` | Credit card number |
| `hashtag` | `#[a-zA-Z0-9_]+` | Hashtag |
| `mention` | `@[a-zA-Z0-9_]+` | @mention |

## Examples

```bash
# Test a pattern interactively
python scripts/regex_tester.py --pattern "[a-z]+" --text "hello world"

# Use common pattern shorthand
python scripts/regex_tester.py --pattern "email" --text "contact@example.com"

# Case-insensitive match
python scripts/regex_tester.py --pattern "hello" --text "HELLO world" --flags i

# Extract all matches from file
python scripts/regex_tester.py --pattern "\d+" --text "order 123 and 456"

# JSON output for scripting
python scripts/regex_tester.py --pattern "\w+" --text "hello world" --json
```

## Pattern Matching Output Format

```
Pattern: [a-z]+
Text:    "hello world"

Matches: 2 found
  [0] "hello" (pos 0-5)
  [1] "world" (pos 6-11)

Groups: none
```

For patterns with capture groups:
```
Pattern: (\w+)@(\w+)
Text:    "user@domain"

Matches: 1 found
  [0] "user@domain" (pos 0-11)
Groups:
  [1] "user"
  [2] "domain"
```
