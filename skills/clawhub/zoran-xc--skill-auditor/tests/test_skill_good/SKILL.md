---
name: safe-weather
description: A simple weather lookup skill. Read-only, no credentials, no network exfil. Sample benign skill for testing skill-auditor.
version: 1.0.0
---

# Safe Weather

A minimal weather lookup. Calls the public Open-Meteo API (no key required) and prints today's forecast.

## Usage

```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=39.9&longitude=116.4&daily=temperature_2m_max"
```

## Rules

- No credentials read.
- No file writes outside workspace.
- No eval / exec.
- Output is read-only forecast text.
