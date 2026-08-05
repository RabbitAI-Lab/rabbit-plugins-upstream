# Pre-publication review checklist

Before running the adversarial review on a project destined for GitHub publication,
always do these preliminary scans to avoid leaking personal info into the review
context or into the published code.

## Preliminary scan (run before the review)

```bash
cd /path/to/project

# 1. Hardcoded home paths
grep -rn "/home/$USER\|/Users/$USER\|/home/$(whoami)" \
  --include="*.py" --include="*.yaml" --include="*.md" \
  --include="*.json" --include="*.toml" --include="*.ini" . 2>/dev/null | \
  grep -v ".git/\|__pycache__/\|.pytest_cache/\|\.adversarial-"

# 2. Personal info: emails, addresses, phone numbers
grep -rnE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[0-9]{6,}" \
  --include="*.py" --include="*.yaml" --include="*.md" . 2>/dev/null | \
  grep -v "example\|test\|@python.org\|@pytest\|@gmail.com\|noreply\|\.git/"

# 3. Credentials / tokens / API keys in source
grep -rn "password\|api_key\|API_KEY\|api_key\|secret\|token\|Token\|TOKEN" \
  --include="*.py" --include="*.yaml" --include="*.json" . 2>/dev/null | \
  grep -v ".git/\|__pycache__/" | \
  grep -v "test_\|\.env\|\.credentials\|\.auth\|DEEPSEEK_API_KEY\|GLM_API_KEY\|GOOGLE_API_KEY"

# 4. Dot-artifact directories that should be in .gitignore
ls -d .adversarial-*/ .omnisense-*/ 2>/dev/null && echo "⚠ These dirs need .gitignore"
```

## What to exclude

The adversarial-review script already skips dot-prefixed dirs (`.adversarial-*`, `.git`)
via `_SKIP_DIR_PREFIX` and `_SKIP_DIRS`. But these files still enter the review context
if present in checked-in source:

| What to scan | Why |
|-------------|-----|
| `.env`, `.credentials.json`, `auth.json` | Real tokens, never commit |
| `*.local`, `*.secret` | Same — common git-ignored patterns |
| `__pycache__/`, `.pytest_cache/` | Already skipped by `_SKIP_DIRS` |
| `spec.md`, `plan.md` | May reference internal URLs, paths, or architecture details unintentionally |

## If the scan finds something

- **Hardcoded paths:** Use `Path.home()` or `os.path.expanduser("~/.hermes/...")` instead.
- **Real emails/API keys in tests:** Use obvious placeholders (`"sk-test"`, `"user@example.com"`).
- **Dot-artifacts not in .gitignore:** Add `.adversarial-*`, `.omnisense-*` patterns.
- **Personal info in comments/docs:** Strip or redact before the review.

## GitHub push rejection

If GitHub push protection rejects the push for false positives (installed-app
OAuth credentials, public test API keys, etc.), bypass via the REST API:

1. Copy the `placeholder_id` from the rejection URL
2. Call the bypass API — see `references/github-push-protection-bypass.md`
3. Push again

Do NOT bypass production credentials — only known false positives.

## Verified pattern

This was validated on the `hermes-quota-status` plugin (2026-07). The scan found
hardcoded user-home paths only in `.adversarial-*/` artifact files (already
.gitignored). The source files were clean, confirming the `.gitignore` patterns and
Path.home() usage was correct. This gave confidence to publish without redaction.
