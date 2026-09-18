---
name: json-toolkit
description: Efficient JSON data processing with jq — query, transform, validate, merge, and compare JSON files through copy-pasteable bash recipes
metadata: {"openclaw": {"emoji": "🔧"}}
---

# JSON Toolkit

Process JSON data quickly with `jq` and standard Unix tools. Every recipe below is
copy-pasteable; replace the placeholder file names and filters as needed.

## Prerequisites

```bash
# jq is required. Check:
jq --version

# Install if missing (Debian/Ubuntu):
sudo apt-get install -y jq

# Install if missing (macOS):
brew install jq
```

## 1. Quick Start — Validate & Pretty-Print

```bash
# Validate and pretty-print a JSON file:
jq . data.json

# Validate only (no output on success):
jq empty data.json && echo "valid JSON"

# Validate every .json file in a directory:
find . -name '*.json' -exec sh -c 'jq empty "$1" || echo "INVALID: $1"' _ {} \;
```

## 2. Querying with jq Filters

```bash
# Extract a single field:
jq '.name' data.json

# Extract nested field:
jq '.user.address.city' data.json

# Get all keys of an object:
jq 'keys' data.json

# Get values at all paths matching a pattern:
jq '.. | .email? // empty' data.json

# Find all objects where a condition holds:
jq '.users[] | select(.active == true)' data.json

# Filter array items by numeric comparison:
jq '.items[] | select(.price > 100)' data.json

# Pick specific fields from each array element:
jq '.users[] | {name, email}' data.json

# Chain filters — extract then count:
jq '.users[].name' data.json | wc -l
```

## 3. Transforming JSON

```bash
# Rename a key:
jq 'with_entries(if .key == "old_name" then .key = "new_name" else . end)' data.json

# Flatten nested object (dot-notation keys):
jq '[paths(scalars) as $p | {($p | join(".")): getpath($p)}] | add' data.json

# Add a computed field:
jq '.users[] | . + {active: (.login_count > 0)}' data.json

# String interpolation:
jq '.users[] | {label: "\(.first_name) \(.last_name)", email}' data.json

# Convert to array of values from a single key:
jq '[.users[].name]' data.json

# Map over arrays and transform:
jq '.items | map(.price * 0.8)' data.json

# Remove null/empty fields recursively:
jq '[.. | objects | to_entries | map(select(.value != null)) | from_entries] | .[0]' data.json

# Sort an array of objects by a field:
jq 'sort_by(.age)' data.json

# Group by a key:
jq 'group_by(.category) | map({key: .[0].category, count: length})' data.json
```

## 4. Merging and Comparing JSON Files

```bash
# Merge two JSON objects (second file's keys override first):
jq -s '.[0] * .[1]' a.json b.json

# Deep merge multiple files:
jq -s 'reduce .[] as $item ({}; . * $item)' *.json

# Merge arrays from multiple files:
jq -s 'add' a.json b.json

# Type-safe merge (only merge objects, concatenate arrays):
jq -s 'def merge(a; b):
  if (a|type) == "object" and (b|type) == "object"
  then reduce (b|keys_unsorted[]) as $k (a;
    .[$k] = merge(.[$k] // null; b[$k]))
  elif (a|type) == "array" and (b|type) == "array"
  then a + b
  else b end;
  reduce .[1:][] as $item (.[0]; merge(.; $item))' a.json b.json c.json

# Compare two JSON files semantically (ignoring key order):
diff <(jq -S . a.json) <(jq -S . b.json)

# Find keys present in one file but not the other:
jq -n '($a | keys) - ($b | keys)' --argjson a "$(cat a.json)" --argjson b "$(cat b.json)"
```

## 5. Working with Large JSON Files

```bash
# Pretty-print only the first 50 lines:
head -c 1000000 large.json | jq . | head -50

# Stream and filter object-by-object (works with files > 1 GB):
jq -c '.items[] | select(.active == true)' huge.json > active.jsonl

# Count array elements without loading the whole file:
jq '.items | length' huge.json

# Paginate an array (page 2, 10 items per page):
jq '.items[10:20]' huge.json

# Extract a page and convert to NDJSON:
jq -c '.items[1000:2000][]' huge.json | head -100

# Use jq's streaming parser for very large top-level values:
jq -cn --stream 'fromstream(1 | truncate_stream(inputs))' huge.json > flattened.json

# Check file size before processing:
ls -lh huge.json && jq . huge.json > /dev/null
```

## 6. Common jq Recipes

| Task | Command |
|------|---------|
| Pretty-print | `jq . file.json` |
| Validate JSON | `jq empty file.json` |
| Get all keys | `jq 'keys' file.json` |
| Extract field | `jq '.field' file.json` |
| Query nested | `jq '.a.b[0].c' file.json` |
| Filter array | `jq '.[] \| select(.x > 5)' file.json` |
| Rename key | `jq 'with_entries(select(.key=="a").key="b")' file.json` |
| Count items | `jq 'length' file.json` |
| Sort by field | `jq 'sort_by(.field)' file.json` |
| Group by field | `jq 'group_by(.field)' file.json` |
| Merge two files | `jq -s '.[0] * .[1]' a.json b.json` |
| Compare files | `diff <(jq -S . a.json) <(jq -S . b.json)` |
| JSON → CSV | `jq -r '.\[0] | keys_unsorted, (.[] \| [.[keys_unsorted\[\]][]]) \| @csv' file.json` |
| CSV → JSON | `jq -R 'split(",")' file.csv` |
| Remove nulls | `jq 'walk(if type=="object" then with_entries(select(.value!=null)) else . end)' file.json` |
| Flatten object | `jq '[paths(scalars) as $p \| {($p\|join(".")): getpath($p)}] \| add' file.json` |

## 7. Troubleshooting

### "jq: command not found"
```bash
# Install jq:
sudo apt-get install -y jq   # Debian/Ubuntu
brew install jq              # macOS
```

### "parse error: Invalid numeric literal"
```bash
# The file is not valid JSON. Check for trailing commas or comments:
head -20 suspect.json

# Remove // comments (not valid JSON):
sed 's://.*$::' suspect.json | jq .

# Remove trailing commas before } or ]:
sed -E 's/,([[:space:]]*[}\]])/\1/g' suspect.json | jq .
```

### "memory exhausted" on large files
```bash
# Use streaming mode instead:
jq -cn --stream 'fromstream(inputs)' huge.json

# Or filter early to reduce output size:
jq -c '.items[] | select(.active == true)' huge.json

# Pipe through head to stop processing early:
jq -c '.items[]' huge.json | head -100
```

### "syntax error, unexpected $end"
```bash
# Check for unclosed brackets/quotes. Validate each section:
jq '.field' <(head -c 500 data.json; echo '}')
```

### Special characters in keys
```bash
# Quote keys with dots or spaces:
jq '.["key.with.dots"]' data.json

# Use bracket notation for dynamic keys:
jq --arg k "field" '.[$k]' data.json
```
