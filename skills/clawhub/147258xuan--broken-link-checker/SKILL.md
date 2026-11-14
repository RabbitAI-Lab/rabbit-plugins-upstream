---
name: broken-link-checker
description: Scan documentation for broken links using curl. Use when validating markdown docs, checking for dead URLs, or before releasing documentation.
---

# Broken Link Checker Skill

Checks for broken or invalid links in documentation and markdown files.

## Usage

```bash
# Check current directory
node skills/broken-link-checker/index.js

# Check specific directory
node skills/broken-link-checker/index.js /path/to/docs
```

## Features

- Recursively scans all markdown files in a directory
- Extracts both markdown-style links `[text](url)` and raw URLs
- Uses curl to check HTTP status codes
- Skips anchor links, relative paths, and non-HTTP URLs
- Reports file location and line number for each broken link
- Configurable timeout and retry logic

## Output

```
=== Broken Link Checker ===
Target: /path/to/project
Time: 2026-06-07T09:26:39.852Z

Summary:
  Files scanned: 12
  Links found: 47
  Links checked: 38
  Broken links: 2
  Skipped: 9

Broken Links:
  docs/api.md:15
    URL: https://example.com/api/v2/users
    Status: 404
  README.md:42
    URL: https://old-docs.example.com/guides
    Status: ERROR: connect ETIMEDOUT

Recommendations:
  - Found 2 broken link(s) - fix or remove them
```

## API

### checkBrokenLinks(targetDir, options)

Returns check results object:
```javascript
{
  timestamp: '2026-06-07T09:26:39.852Z',
  target: '/path/to/project',
  summary: {
    files_scanned: 12,
    links_found: 47,
    links_checked: 38,
    broken_links: 2,
    skipped_external: 9
  },
  files: [...],
  broken: [...],
  recommendations: [...]
}
```

## When to Use

- Before releasing documentation
- During documentation reviews
- In CI/CD pipelines for docs
- Periodic link health checks
- After migrating documentation to new URLs