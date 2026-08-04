> **Scope: this bypasses a GitHub security control. Only use it for a
> confirmed false positive you can point to in the "bypass vs fix" table
> below. Never use it to push a real secret — rotate and fix instead.**

# GitHub Push Protection Bypass for False Positives

When publishing reviewed code to GitHub, secret scanning's push protection
may reject the push for credentials that are **not actual secrets** (installed-app
OAuth client secrets, public test API keys, demo tokens, etc.).

## Diagnosis

The rejection message includes:

```
remote:       —— Google OAuth Client Secret ————————————————————————
remote:        locations:
remote:          - commit: <sha>
remote:            path: gemini_cloudcode.py:31
remote:
remote:        (?) To push, remove secret from commit(s) or follow this URL
remote:            to allow the secret.
remote:            https://github.com/<owner>/<repo>/security/secret-scanning/unblock-secret/<PLACEHOLDER_ID>
```

The `PLACEHOLDER_ID` in the URL is the key — it identifies the detected secret
to the bypass API.

## Per-value verification (required before bypass)

**Category membership in the "bypass vs. fix" table below is not enough by
itself.** The table says which *class* of credential is safe to bypass, but
a real, rotated secret can land in the flagged file under the same class
label (e.g. someone pastes a live client secret into the same variable that
normally holds the public installed-app one). Before calling the bypass API,
diff the *exact* flagged value against a known-public constant sourced
**independently of the flagged commit** for that credential class.

Extract the exact value using the `path` and line number GitHub's rejection
message cited (not a guessed filename or a grep for default-variable names —
either of those can silently match a different assignment than the one
flagged, letting a live secret elsewhere in the file, or under the same
variable name, pass unchecked):

```bash
# Use the exact path and line from the rejection's `path: <path>:<line>`:
git show <sha>:<path-from-rejection> | sed -n '<line-from-rejection>p'
```

Then compare it byte-for-byte against a known-public value from a source
**independent of the flagged file/commit** — e.g. the vendor's published
source (upstream GitHub repo, the installed pip/npm package cache on disk,
official docs) or a commit predating any point where the value could have
been tampered with. Do **not** treat another occurrence of the same variable
in the same working tree as independent verification — if the flagged commit
is where a live value was pasted in, a second read of that same file/commit
will just confirm the tampered value against itself.

```bash
diff <(echo "<value flagged by GitHub>") <(echo "<value from independent source>")
```

Only bypass if that diff is empty. Any difference at all — a changed
character, a different length, a rotated timestamp — means this is not the
known-public value: stop, do not bypass, and rotate/remove the credential
instead.

**If no independent known-public source can be located, treat the value as
unverified: do not bypass.** `references/pre-publication-cleanup.md` §2 does
**not** provide this baseline — it records only truncated placeholders
(`_CLIENT_ID_DEFAULT = "..."`), not the vetted bytes, precisely so it can't be
mistaken for ground truth here.

## Bypass via REST API

Use the `gh api` or `python3` with the user's GitHub token:

```python
import json, urllib.request, os

token = os.popen("gh auth token").read().strip()
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# One bypass per detected secret type. Replace PLACEHOLDER_ID from the URL.
data = {
    "secret_type": "google_oauth_client_id",   # or google_oauth_client_secret
    "reason": "false_positive",
    "placeholder_id": "PLACEHOLDER_ID",
}

req = urllib.request.Request(
    "https://api.github.com/repos/<owner>/<repo>/secret-scanning/push-protection-bypasses",
    data=json.dumps(data).encode(), headers=headers, method="POST",
)
res = urllib.request.urlopen(req)
print(res.status, json.loads(res.read()))
```

**Required fields:**
- `secret_type` — one of the secret types GitHub detected (found in the error
  message heading, e.g. `google_oauth_client_secret`).
- `reason` — must be one of: `false_positive`, `used_in_tests`, `will_fix_later`.
  For installed-app credentials, always `false_positive`.
- `placeholder_id` — the alphanumeric ID extracted from the unblock URL.

**Response (200):**
```json
{"reason": "false_positive", "expire_at": "2026-07-14T04:07:26.544-07:00", "token_type": "GOOGLE_OAUTH_CLIENT_ID"}
```

The bypass expires after ~24h. After creating the bypass, retry the push.

## When to bypass vs. fix

| Scenario | Action |
|----------|--------|
| Installed-app OAuth client secret (Google Cloud Code, etc.) | **Bypass** — these are public by design, not confidential |
| Personal API keys, tokens, passwords | **Fix** — replace with env vars or remove from source |
| Test credentials (obviously fake, like `sk-test`) | **Bypass** — use `used_in_tests` reason |
| Demo/tutorial credentials published by the vendor | **Bypass** — use `false_positive` reason |
| Production credentials | **Fix immediately** — rotate the credential, remove from git history |

## Validated example (2026-07-13)

Project: `hermes-quota-status` — `gemini_cloudcode.py` contained Google Cloud
Code OAuth client ID/secret (installed-app flow, public by design).

**Error:** Push rejected for `google_oauth_client_id` and `google_oauth_client_secret`.

**Solution:** Two API calls (one per secret type) with `reason: false_positive`.
After bypass, push succeeded. The values were already behind `os.environ.get()`
with defaults — the hardcoded fallbacks remain for out-of-the-box usability.

**Alternative (if you prefer no bypass):** Remove the hardcoded values entirely
and require `GOOGLE_CLIENT_ID`/`GOOGLE_CLIENT_SECRET` env vars. This breaks
out-of-the-box OAuth for users who don't set the env vars, which is a worse
experience than the bypass.
