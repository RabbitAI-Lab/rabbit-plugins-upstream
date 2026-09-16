---
name: json-formatter
description: Format, minify, and validate JSON data. Use when you need to pretty-print JSON, compact JSON for transport, verify JSON syntax, or process JSON from files or stdin.
---

# JSON Formatter

Format, minify, and validate JSON with a single script.

## Quick Reference

```bash
# Format (pretty-print)
python3 scripts/json_tool.py format [file] [--indent 2]

# Minify (remove whitespace)
python3 scripts/json_tool.py minify [file]

# Validate (check syntax only)
python3 scripts/json_tool.py validate [file]
```

If `file` is omitted, reads from stdin.

## Examples

```bash
# Format a file
python3 scripts/json_tool.py format config.json --indent 4

# Minify a file and save
python3 scripts/json_tool.py minify data.json > min.json

# Validate stdin
echo '{"a":1}' | python3 scripts/json_tool.py validate

# Pipe through format
cat api-response.json | python3 scripts/json_tool.py format
```
