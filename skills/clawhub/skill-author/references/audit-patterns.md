# ClawHub Audit Pattern → Fix Mapping

Distilled from two real remediation cases (epic-novel-writer 1.2.1, image-with-comfyui 1.7.1, 2026-09).

Audit page structure: **static pattern scan (hard findings, with `file:line`) + LLM review (soft findings, with confidence)**.
Hard findings must be fixed in code/config. Soft findings: judge by confidence, then fix docs/flows. False positives: keep the code and explain.

## 1. Command injection (Insecure Skill Coding Practices)

**Pattern**: a user-controlled value (title / path / filename) is interpolated unquoted and unvalidated into a shell command example.
**Case (epic-novel-writer, Medium)**: `cat chapters/vol-*/chapter-*.txt > [小说标题]_全文.txt` — a title containing `;`, `$(`, `>` executes as shell syntax. Attack path: malicious title → user later asks to archive → agent runs the templated command.

**Fix (all four, none optional)**:
1. **Allowlist sanitize**, abort on failure:
   ```bash
   safe_title=$(printf '%s' "$title" | tr -cd '[:alnum:] _.-')
   if [ -z "$safe_title" ]; then
     echo "Error: empty title after sanitization" >&2; exit 1
   fi
   ```
2. **Quote every expansion**: `"${safe_title}_full.txt"` — no bare expansions
3. **Verify the destination** stays inside the intended directory before writing (blocks `..` / symlink escape)
4. **Prefer file tools over constructed shell commands** wherever possible
5. Add a "⚠️ Safety Rules" section to the docs so the agent must follow these at run time

## 2. Undisclosed data egress (common High finding)

**Pattern**: bundled config defaults to a non-loopback endpoint (private network / public); the skill transmits prompts or user files there while the docs call it "local".
**Case (image-with-comfyui, High)**: `config.json` default `http://10.71.253.215:31577` (LAN); I2I/I2V upload full source images in plaintext.

**Fix**:
1. **Ship a loopback-only default**: `"comfyui_url": "http://127.0.0.1:8188"`
2. **Before changing the default, verify how the real endpoint is configured** — `env | grep`, `OPENCLAW_SERVICE_MANAGED_ENV_KEYS`, shell rc files. If the real endpoint arrives via env var, changing the shipped default is safe for the author's own setup
3. **Runtime disclosure**: after loading config, if the endpoint is non-loopback, print a one-line warning to stderr ("prompts and full images will be sent to this host")
4. **Document the data flow**: a "Data & Privacy" section — what is transmitted (prompts / workflow JSON / source images), where outputs are written, HTTPS for remote, never credentials in URLs or logs
5. Never silently fall back to a hardcoded LAN address

## 3. Supply chain: unpinned third-party install instructions (common Medium finding)

**Pattern**: docs instruct `git clone` of a mutable default branch plus `pip install -r requirements.txt` with no lock. Audited state is not reproducible; a later compromise of the repo propagates to installers.
**Case (image-with-comfyui, Medium)**: three custom-node install commands, all unpinned — and two URLs were already dead (repos renamed/migrated).

**Fix**:
1. **Pin reviewed commits**, use `git checkout --detach <full-sha>`
2. **Verify repos still exist before publishing** — `git ls-remote` fails on auth issues; the GitHub API is more reliable:
   ```bash
   curl -s "https://api.github.com/repos/<owner>/<repo>/commits?per_page=1" \
     | python3 -c "import json,sys; d=json.load(sys.stdin); print(d[0]['sha'] if isinstance(d,list) and d else d.get('message'))"
   ```
   `Not Found` → the repo was renamed/deleted. Search `users/<owner>/repos` for the new address and note "renamed from X" in the docs.
3. **Lock dependencies**: lockfile / `pip install --require-hashes`; at minimum, note "review the dependency list before installing"
4. **Install environment**: recommend a venv + non-root; explicitly say "do not install as root"
5. The skill itself **never executes `git clone`** ("the script never runs git clone itself") — it only reports

## 4. Language / locale policy

**Pattern**: docs force a single language (all-Chinese with no statement; "must write in English") — flagged as a locale policy violation.
**Fix**:
- Add a **language note**: why docs are in a specific language (domain-driven, e.g. Chinese web novels), and that **output language follows the user/project**
- "Must use X language" → "X language usually works better; not forced"

## 5. Intent contradictions / vague triggers

**Pattern**: docs say "read-only / only on explicit request" on one hand and put the dangerous operation into the standard workflow on the other; trigger conditions use fuzzy words ("similar phrasing", "looks like").
**Fix**:
- Dangerous steps become "**requires explicit user confirmation, not an automatic step**"
- Narrow triggers to **imperative phrasing only**, with counter-examples ("this chapter reads well" is **not** an archive request; when in doubt, ask)
- Contradictory pairs ("archives are read-only" vs "reverse merge can overwrite") → keep both, but require "state the diff scope + explicit confirmation + backup recommended" for the overwriting path

## 6. Doc ↔ code inconsistency

**Pattern**: docstrings/README declare functionality that doesn't match the code (under- or over-claiming).
**Case**: docstring said "T2I / I2I" but code had a `wan2.2` I2V subcommand; docs referenced a nonexistent `sd35` subcommand, a `test_all_workflows.py` that doesn't exist, and `COMFYUI_TIMEOUT`/`COMFYUI_OUTPUT_DIR` env vars the script never read.
**Fix (pick one direction, unify it)**:
- Code has it, docs don't → **add it to the docs** (complete feature disclosure)
- Docs have it, code doesn't → implement it in code **or delete the doc reference** (no phantom references)
- Grep-verify every env var / subcommand / file named in docs

## 7. Excessive agency / consent

**Pattern**: the skill makes the agent auto-reuse the user's prior data, auto-run batch file operations, or maintain persistent staging directories — with no consent checks.
**Fix**:
- Auto-reusing user data → **scope limit**: same user, same session, time window only; never across users or sessions
- Batch file operations → confirm scope with the user before executing
- Persistent staging directories → "delete after successful use" rule

## 8. False positives (recognize + handle)

| Flagged content | Why it's a false positive | Handling |
|---|---|---|
| `sanitize_filename` docstring mentioning `../../../etc/passwd` | Documents **defense against** path traversal; read as "credential file access" | Keep it; note in the report that it is protective code |
| Reading the skill's own workflow JSON | Read as "memory poisoning / context stuffing" | Keep it; normal file loading |
| Docs describing error categories | Read as "abnormal behavior" | Keep it |

Principle: **never delete a guard to "fix" a finding** — deleting the guard *creates* the vulnerability. List false positives in a separate section of the remediation report.

## 9. Post-remediation verification

- Script changed → `python3 -m py_compile <file>` + run the skill's own `test` entry (or minimal repro)
- Config changed → `python3 -c "import json; json.load(open('config.json'))"` + print the key fields
- Docs changed → `grep` for leftover old values / dead links / dead URLs (e.g. `grep -rn "10.71.253.215" .`)
- New safety mechanism → run it once to prove it fires (e.g. the non-loopback warning actually prints)
