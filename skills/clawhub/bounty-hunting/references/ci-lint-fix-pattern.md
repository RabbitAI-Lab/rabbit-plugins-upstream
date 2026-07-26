# CI Lint/Format Failure Fix Pattern

When CI shows `lint: FAILURE` with no clear error in annotations:

## Step 1: Identify the linter
```bash
gh api repos/OWNER/REPO/contents/Makefile --jq '.content' | base64 -d | grep -A 5 "lint"
# Common: ruff check + ruff format --check, black --check, eslint
```

## Step 2: Reproduce locally
```bash
uv pip install ruff  # or black, eslint
ruff check path/to/file.py
ruff format --check path/to/file.py
# If format fails:
ruff format path/to/file.py
```

## Step 3: Push fix + reply to maintainer
- Re-upload formatted file via GitHub API
- Reply: "Fixed! Applied [linter] formatting."
- Update Obsidian note

## Common Gotchas
- `ruff check` and `ruff format` are SEPARATE — both must pass
- Annotations may show only "exit code 1" — reproduce locally for details
