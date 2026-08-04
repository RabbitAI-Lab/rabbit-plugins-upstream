# Pre-publication Cleanup Checklist

Before pushing any Hermes skill or plugin to a public GitHub repo, run
through this checklist. It catches the leaks and structure issues that
block pushes and embarrass downstream users.

## 1. Privacy scan

Search all source files for hardcoded personal information. Derive your
username at scan time — a literal `<your-username>` placeholder in a
checklist matches nothing; only `$(whoami)`/`$USER` expands to the value
that could actually be sitting in a file:

```bash
grep -rn --exclude-dir=.git "$(whoami)" .
grep -rn "/home/$USER\|votre-email\|adresse\|telephone" \
  --include="*.py" --include="*.md" --include="*.yaml" --include="*.json" \
  --include="*.toml" --include="*.cfg" --include="*.ini" .
```

Distinguish config defaults from real leaks: `os.environ.get("VAR")` patterns
are config, not secrets. Literal `password = "hunter2"` is a leak.

**A clean working-tree scan only prevents FUTURE leaks.** It says nothing
about history: every past commit's author handle and email are already
public the moment the repo has a public URL (`git log --format='%an <%ae>'`
shows them, and GitHub renders them on every commit page). Removing a
leak from the current files does not remove it from history — that needs
`git filter-repo`/BFG plus a force-push, which is a separate, higher-risk
step this checklist does not perform.

## 2. Secret scanning bypass (Google OAuth)

GitHub's push protection flags Google OAuth client IDs and secrets. The
adversarial skills and quota plugin contain **third-party installed-app
credentials** (from gcloud/gemini-cli/AGY). Two approaches:

**A. Replace with placeholders** (preferred):
```python
_CLIENT_ID_DEFAULT = "..."  # truncated to lose the full pattern
_CLIENT_SECRET_DEFAULT = "..."
CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", _CLIENT_ID_DEFAULT)
```

**B. API bypass** via `secret-scanning/push-protection-bypasses` with
`reason: "false_positive"` and `placeholder_id` from the error message.

**⛔ Don't claim a credential is "safe" or "public" without verification.**
Even well-known installed-app credentials belong to someone else's project.
When in doubt, remove them. Add a comment pointing to the local installation
file where the real value lives.

## 3. Tracking audit — what is actually committed?

List every tracked file and audit each category:

```bash
git ls-files | sort
```

Classify each file by its purpose. Remove local or generated artifacts, but keep
curated documentation that is intended to explain or support the published
project.

**Personal / dev artifacts:**
- `IMPLEMENTATION_PLAN.md`, `plan.md`, `spec.md` — development roadmaps, not repo content
- `_retrospective/`, `ISSUES.md` — remove private journals; keep deliberately curated project history
- `references/` — keep vetted project research and operational guidance; remove personal notes and unverified experiments
- `templates/` — project-specific scaffolding that doesn't belong in the repo

**Pipeline / review outputs:**
- `.adversarial-loop/`, `.adversarial-review-*/`, `.adversarial-*/` — intermediate pipeline artifacts (specs, reviews, fixes, verdicts, state)
- `TEST_*.md`, `final.md`, `final.json` in arbitrary directories

**Backups:**
- `*.before`, `*.orig`, `*.rej`, `*.bak` — backup copies (git history already has them)
- `SKILL.md.before`, `scripts/*.py.before`, `scripts/*.py.orig`

**Secrets / bypass docs:**
- Inspect files mentioning OAuth, API keys, credentials, or push-protection
  bypass techniques. Documentation may be publishable, but real credentials,
  account identifiers, and instructions tied to private infrastructure are not.

**Language-mismatched content:**
- Files with French accented characters (or any non-English language) in repos that should be English-only — the pipeline-internal convention is English.

Quick French detection:
```bash
git ls-files | xargs grep -l '[éèêëàâùûüôöîïç]' 2>/dev/null
```

## 4. .gitignore hygiene

After removing local files, add narrowly scoped patterns to `.gitignore` so
they stay untracked. Do not ignore `references/` or `_retrospective/` wholesale
when they contain curated material that is intentionally part of the project.
Common additions for local-only artifacts include:

```
templates/
IMPLEMENTATION_PLAN.md
*.before
*.orig
*.bak
.adversarial-review-git-mode/
.adversarial-review-meta/
```

Must also have these baseline entries at minimum:
```
__pycache__/
*.py[cod]
.venv/
.pytest_cache/
.adversarial-loop/
```

Test: `touch .venv/bin/python __pycache__/foo.pyc` then `git status --short`
should show nothing.

## 5. README + LICENSE

Each published repo needs a name, description, install instructions, and
LICENSE file (MIT recommended).

## 6. Remote URL check

```bash
git remote -v  # confirm origin == github.com/<you>/<repo>
```
