# Pre-Publication Adversarial Review

**Context:** Before pushing a project to a public GitHub repo, run an adversarial review
focused on two dimensions that the standard review doesn't emphasize equally:
**personal info leaks** and **concept bugs**. This reference captures the workflow
validated on the `hermes-quota-status` plugin (2026-07-13).

## Workflow

### Phase 0: Privacy Pre-Scan (before the adversarial review)

Run this before the adversarial pipeline to catch hardcoded personal info early.
Any hits here are a blocker — fix before proceeding.

```bash
cd /path/to/project

# Hardcoded user home paths
grep -rn "/home/$USER\|$HOME" --include="*.py" --include="*.yaml" --include="*.json" \
  --include="*.toml" --include="*.md" . 2>/dev/null | \
  grep -v ".git/\|__pycache__/\|.pytest_cache/\|.adversarial"

# Emails, API keys, tokens, phone numbers, personal names
grep -rn "@.*\.com\|api_key\|API_KEY\|secret\|token\|password\|telephone\|phone\|adresse" \
  --include="*.py" --include="*.yaml" --include="*.json" . 2>/dev/null | \
  grep -v ".git/\|__pycache__/\|.pytest_cache/\|.adversarial"
```

Ignore hits in:
- `.adversarial-*` artifact directories (already in `.gitignore`)
- `__pycache__/`, `.pytest_cache/`, `.git/`
- Test files that use fake credentials (check they're actually fake, not real ones)

**Common sources of leaks:**
- Hardcoded `Path.home()` / `~/.hermes/` paths in source files
- OAuth client secrets embedded in source (acceptable for installed-app flows but
  needs a provenance comment — see N2 pattern below)
- Personal names, email addresses in comments, docstrings, or logging statements
- Machine-specific hostnames in config or constants

### Phase 1: Adversarial Review — Focused Prompting

Run `adversarial_review.py --project-dir` with explicit focus dimensions.
The personas already steer toward architecture/bugs, but for pre-publication,
the prompt should emphasize:

1. **Privacy exposure** — hardcoded paths, personal credentials, environment coupling
2. **Concept bugs** — structural flaws that would misrepresent state or fail silently
3. **External coupling** — assumptions about the host environment (tmux sessions, keyring,
   OAuth flows, filesystem paths) that don't survive on another machine

**Multi-model pairing (validated 2026-07-13):**

```bash
cd /path/to/adversarial-code-review/scripts

python3 adversarial_review.py \
  --project-dir /path/to/project \
  --a-cmd "python3 /path/to/claude-tmux.py --yolo --model best --timeout 600 --hard-timeout 1200" \
  --b-cmd "codex exec -C /path/to/project" \
  --synth-cmd "python3 /path/to/claude-tmux.py --yolo --model best --timeout 600 --hard-timeout 1200" \
  --out /tmp/acr-publish-<project> \
  --timeout 900
```

- **Architect (Claude):** architecture, security, privacy, design, environmental coupling
- **Inspector (Codex):** bugs, edge cases, error handling, NaN/Infinity, parse failures
- **Synthesis (Claude):** consolidates both perspectives; cross-validates findings

### Phase 2: Review the Output

The synthesis report (`05_synthesis.txt`) classifies findings by severity.
For pre-publication, the critical checklist is:

| Class | Must fix before publishing | Can defer |
|-------|---------------------------|-----------|
| **Blocker** | Hardcoded paths, personal API keys, personal info | — |
| **Blocker** | Fabricated healthy state on parse failure (C1) | — |
| **Major** | Auth failure misclassification resetting suppression (C2) | — |
| **Major** | Shared mutable state collisions (tmux session names) (C3) | — |
| **Major** | NaN/Infinity passing validation (C7) | — |
| **Major** | Transport failures rendered as credential errors (C8) | — |
| **Major** | Unbounded blocking under global lock (C4) | — |
| **Major** | Partial data treated as authoritative, suppressing fallbacks (C5) | — |
| **Minor/Nit** | Code smells, dead code, missing comments | ✓ |

### Output Directory Strategy

Use `/tmp/acr-publish-<project>/` for the review output instead of writing
into the project directory. This:
- Keeps the git working tree clean (no review artifacts to gitignore or stash)
- Avoids polluting file listings and tree walking
- Makes it easy to `rm -rf` after fixing

The cleaner the project at review time, the fewer false positives from
review artifacts in the source listing.

## Validated Example: hermes-quota-status (2026-07-13)

**Project:** user Hermes plugin (~2580 LOC, 4 source files)
**Models used:** Claude Fable 5 (Architect + Synthesis), Codex GPT-5.6-Sol (Inspector)
**Findings:** 10 major, 5 minor, 2 nit
**Privacy scan:** clean — no personal paths or credentials in source
**Output:** `/tmp/acr-quota-publish/`

**Notable findings from this review that generalize:**

- **C1 — Parse failure → fabricated healthy state (blocker):** When a TUI scraper
  regex fails to match, initializing defaults to `remaining_pct=100` converts any
  parse miss into a "fully available" report. **Fix:** fail closed — return
  `None`/skip on parse miss; never default to healthy.

- **C2 — Auth failure misclassification (blocker):** HTTP 401/403 collapsed to
  `missing_token`, which bypasses the auth-failure suppression counter. A transient
  bad credential resets the counter, not increments it. **Fix:** preserve error type
  through the entire failure path; verify suppression logic against the spec.

- **C7 — NaN/Infinity pass numeric validation (major):** `json.loads` accepts bare
  NaN tokens by default; `min/max` clamps NaN used-percentage to 0% (falsely
  healthy). **Fix:** insert `math.isfinite()` check after `json_number_or_none()`.

- **C3 — Shared tmux session name (major):** A fixed session name with unconditional
  `kill-session` causes cross-process collisions when two Hermes instances refresh
  concurrently. **Fix:** PID/UUID-suffixed names + `try/finally` lifecycle.

## Pitfalls

1. **Don't rely solely on the adversarial review for privacy.** The persona focuses on
   architecture and bugs, not explicitly on "is there a hardcoded /home/user path."
   Always run the Phase 0 grep scan first — it's deterministic and catches things the
   LLM might gloss over.

2. **The privacy pre-scan can have false positives.** OAuth client secrets embedded
   for installed-app flows (Google Cloud Code, etc.) are standard practice — flag
   them but distinguish from personal credentials. Test fixture credentials are also
   expected; verify with `git diff HEAD~1` that they're not real secrets committed
   in the past.

3. **Test files can codify the wrong behaviour.** The review found one test
   (`test_missing_credentials_reset_auth_failure_counter`) that locked in buggy
   behaviour matching the spec violation (C2). When the fix contradicts a test,
   the test must change too — never fix the code around a wrong test.

4. **The `/tmp/` output survives reboots on most Linux systems, but gets cleaned
   by `tmpreaper`/`systemd-tmpfiles` after 10 days.** Copy the final report
   (`review.md` / `final.json`) elsewhere if you need it longer.

5. **Codex with `reasoning=high` is slow on pipe-stdin prompts** (3+ min silence
   before output starts). Don't kill the process — it's not hung. For the Inspector
   role, use timeout ≥ 900s and monitor with `notify_on_complete=true`.
