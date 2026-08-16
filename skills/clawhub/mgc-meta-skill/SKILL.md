---
```yaml
name: MGC Blackbox (Zero‑Exposure Edition)
id: mgc-blackbox
version: 1.4.10
author: MirginCipher Team
description: Local encrypted credential and script management for AI agents. Zero‑exposure execution layer for storing tokens, passwords, configs, and scripts without plaintext leakage.
tags:
  - security
  - credentials
  - encryption
  - zero-exposure
  - mgc
  - blackbox
mcp_tools:
  - mgc_save
  - mgc_get
  - mgc_run
  - mgc_seal
  - mgc_list
  - mgc_open_webui
install: pip install mgc-blackbox
runtime: mgc
port: 57219
keywords:
  - credential management
  - secret management
  - token storage
  - zero trust
  - encrypted execution
```

---

# 1. Overview — What MGC Blackbox Is

**MGC Blackbox is a local encrypted execution layer.**

It lets AI agents, system scripts, and human users **store, execute, and delegate sensitive information or scripts without ever exposing plaintext.**

The core promise:

- **Store** sensitive data (tokens, passwords, configs).
- **Store** scripts (logic, workflows, automation).
- **Execute** stored scripts with structured `argparse` parameters.
- **Seal** scripts for delegated execution — the original owner keeps control.
- **List** stored entries (metadata only, never plaintext).
- **Open WebUI** for human operations.

All data is encrypted locally with AES-256. **AI can execute but can never read the plaintext.**

---

# 2. Typical Scenarios — Why You'd Use MGC

> Read this section first. These three scenarios are the reason MGC exists.
> The rest of the document is the technical reference.

---

## Scenario A — Zero-Exposure API Keys

Store an API key in MGC once. Reference it from your script by name at runtime.
**The plaintext key never appears in your script source, your working directory, or your command line.**

### The script (this is what you actually write)

```python
import os
import requests
import openai

# Read MGC access token (one-time; store outside any shared location)
with open(os.path.expanduser("~/.mgc/database/mgc_black_box/.mgc_token")) as f:
    MGC_TOKEN = f.read().strip()

# Look up the API key from MGC at runtime — never write it in plaintext
resp = requests.post(
    "http://127.0.0.1:57219/api/mgc/sensitive/get",
    headers={"X-MGC-Token": MGC_TOKEN},
    json={"info_type": "token", "info_owner": "openai_api_key"},
)
resp.raise_for_status()
key = resp.json()["data"]

client = openai.OpenAI(api_key=key)
client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "hello"}],
)
```

**What you get:**

- The script source contains **zero** references to the actual API key.
- You can email the script, commit it to git, share it on Slack — the key is safe.
- The key only exists in **plaintext inside the MGC process boundary**, which is encrypted at rest.
- The `MGC_TOKEN` itself grants *retrieval* access, not the secret value — keep it on the same host as MGC.

> MGC exposes a REST API (see §9), not a Python client module. To retrieve an entry from a Python script, call the HTTP endpoint directly using `requests` (or `httpx`).

---

## Scenario B — AI Agents Calling Your Scripts Without Seeing Them

Store your script with `info_type='script'`. MGC parses the script's `argparse` arguments and stores them as a structured `ext02` field. **The AI agent then calls `mgc_run` with just an owner name and runtime args — it never sees the script source, the embedded credentials, or the storage internals.**

### Step 1: You store the script (one-time)

```bash
mgc_save(
    info_type="script",
    info_owner="weather_report",
    ext01="python",
    content='
import argparse, requests
parser = argparse.ArgumentParser()
parser.add_argument("--city", default="Beijing")
parser.add_argument("--api_key", default=__import__("os").environ["OPENAI_KEY"])
args = parser.parse_args()
print(requests.get(f"https://wttr.in/{args.city}?format=j1", headers={"X-API-Key": args.api_key}).text)
'
)
# MGC auto-fills ext02 with ["--city", "Beijing"]
```

### Step 2: The AI agent calls it (anytime, zero visibility)

```text
AI: "Give me the weather for Shanghai."
Agent: mgc_find(info_owner="weather")          # discover entry + see default ext02
        mgc_run(info_owner="weather_report",
                ext02='["--city", "Shanghai"]') # override args at runtime
        → { "pid": 12345, "status": "started" }
```

**What the AI sees:**

- The script name (`weather_report`).
- The runtime args it passed (`--city Shanghai`).
- The status (`started`).

**What the AI does NOT see:**

- The script source.
- The API key retrieval logic (`os.environ["OPENAI_KEY"]`).
- How MGC encrypts or stores the data.

You maintain the script. AI drives it. Neither side exposes the other.

---

## Scenario C — Distribute a Sealed Script Across MGC Nodes

This is the killer feature for team workflows. Encrypt your script + dependencies so a target MGC node can **execute but cannot modify, redistribute, or read the plaintext**.

### The flow

```
You (Node A)                        Target Node B
─────────────                       ─────────────
1. mgc_get(NODE_PUB)                (already has RSA keypair)
   → returns Node B's public key

2. mgc_seal(                        (nothing to do on B yet)
     info_owner="my_report",
     ext04=<Node B's public key>,
     info_type="script",
   )
   → returns sealed capsule:
     - AES-encrypted script body
     - AES key wrapped with Node B's RSA public key

3. Hand over capsule
   (email / USB / any channel)

                                     4. mgc_save(
                                          info_type="script",
                                          info_owner="my_report",
                                          content=<sealed capsule>,
                                          ext01="python",
                                          ext03=<RSA-wrapped AES key>,
                                        )
                                     → encrypted bytes stored as-is

                                     5. mgc_run(info_owner="my_report")
                                        → Node B decrypts and runs.
                                          Node B can execute but:
                                          • cannot read plaintext script
                                          • cannot modify the body
                                          • cannot re-seal for Node C
                                          (because the AES key is bound to B's RSA key)
```

### Cross-platform note

Cross-platform sealed scripts: be aware of semantic differences between
operating systems (path separators, shell behavior, available tools).
Use `pathlib.Path` or `/` for paths, and avoid platform-specific APIs
in the script body.

### Why this matters

- **Execute-only licenses**: distribute a script to a contractor, vendor, or partner without giving them source or transferable rights.
- **No DRM server**: the cryptographic binding is intrinsic to the capsule. Works offline.
- **Ownership retained**: you can re-seal with a new target key. Old copies become unusable.

---

# 3. Installation & Runtime — How to Install and Run MGC

## 3.1 Requirements

- An MCP-compatible agent runtime (Claude Desktop, Cursor, Trae, etc.) for AI integration.
- A modern browser for WebUI access.

### Supported Python × OS matrix

| OS | Python 3.10 | Python 3.11 | Python 3.12 |
|---|---|---|---|
| Windows | ✅ | ✅ | ✅ |
| Linux (Ubuntu) | ✅ | ✅ | ✅ |
| macOS 14+ (Apple Silicon) | ✅ | ✅ | ❌ not supported |

## 3.2 Install MGC Blackbox

```bash
pip install mgc-blackbox
```

Ensure installation happens in the same Python environment where your MCP agent runs.

## 3.3 Run MGC in normal mode

Start MGC as a standalone local service:

```bash
mgc
```

Default behavior:

- Starts HTTP server at `http://127.0.0.1:57219`
- Initializes encrypted database on first run
- Generates access token at `~/.mgc/database/mgc_black_box/.mgc_token`

This token is required for all REST API calls.

## 3.4 Run MGC as an MCP server

If your agent supports MCP, configure:

```json
{
  "mcpServers": {
    "mgc-blackbox": {
      "command": "mgc",
      "args": ["--mcp"],
      "env": { "PYTHONIOENCODING": "utf-8" }
    }
  }
}
```

In MCP mode, MGC exposes six tools: `mgc_save`, `mgc_get`, `mgc_run`, `mgc_list`, `mgc_seal`, `mgc_open_webui`. AI interacts **only** through MCP tools. The REST API remains available for system scripts.

### Sandbox mode

MGC supports sandboxed environments, but a sandboxed agent cannot use the MGC MCP tools if MGC itself is also running in sandbox mode (some sandbox agents run MCP in the system environment rather than inside the sandbox). To use the MCP tools, install MGC in the system environment, or call the FastAPI directly.

## 3.5 WebUI access

WebUI is available at:

```
http://127.0.0.1:57218
```

Use the WebUI for initialization, manual storage, metadata inspection, database audit, and logs.

---

# 4. The `ext_*` Protocol — Field Meanings

| Field | Role | Used by |
|-------|------|---------|
| **ext01** | Startup command (e.g. `"python"`) | `mgc_save` (required for scripts), `mgc_run` |
| **ext02** | Runtime args (JSON array string) | `mgc_save` (auto-filled by parser), `mgc_run` (override) |
| **ext03** | Sealed AES key (RSA-encrypted) | `mgc_save` (after `mgc_seal`), `mgc_run` (sealed scripts) |
| **ext04** | Target node public key (PEM) | `mgc_seal` only |

### Rules

- All `ext01`–`ext30` fields are dynamically passed through MCP / API / WebUI.
- `ext02` is a **JSON array string** when manually set, e.g. `'["--start", "2026-08-08"]'`. MGC passes it to `subprocess.run()` verbatim.
- `ext04` is required only when sealing (it identifies the recipient).

---

# 5. MCP Tools — Quick Reference

> For full argument schemas and field types, see the MCP server's auto-generated schema
> (every MCP client surfaces it; AI agents read it directly).
> This section documents the **intent** of each tool — when to reach for which.

---

## MCP Tools — Quick Reference

> For full argument schemas, field types, and return shapes, see the MCP server's auto-generated schema (every MCP client surfaces it; AI agents read it directly). This table documents **intent** and **the most important caveats only**.

| MCP tool | Describe | Notice |
|----------|----------|--------|
| `mgc_save` | Store a token, password, script, or config. For scripts, MGC parses `argparse` and auto-fills `ext02`. | See §8 *Script Args* for auto-extraction behavior. |
| `mgc_get` | Retrieve decrypted content of an entry. Also supports `action=run` for script execution. | Legacy for script execution — prefer `mgc_run`. Multi-match returns **metadata list only**, never plaintext. |
| `mgc_run` | Execute a stored script. Equivalent to `mgc_get action=run` but first-class for clearer intent. | Returns `pid + status` only — no script body or output. Override args via `ext02`; omit to use stored value. |
| `mgc_list` | List stored entries (metadata only, no plaintext). Supports raw LIKE wildcards (`%test%`). | For new code, prefer `mgc_find` (auto-applies wildcards). |
| `mgc_find` | Fuzzy-search entries. `match_mode` (substring / prefix / suffix / exact) auto-applies LIKE wildcards; `limit` defaults to 100. | **v1.4.10** — preferred over `mgc_list` for fuzzy lookup. Never returns plaintext. |
| `mgc_seal` | Encrypt a script with AES + wrap the AES key with target node's RSA public key. | See Scenario C in §2 for full flow. Capsule must be re-fed to `mgc_save` for storage. |
| `mgc_open_webui` | Open `http://127.0.0.1:57218` in the default browser. | Port is 57218 (or lower if occupied). |

---

## 5.1 Recommended Workflows

To look up or run an entry / script, first use `mgc_find` for a fuzzy search to discover its metadata (e.g. `ext01`, `ext02`), then proceed with `mgc_get` to read content or `mgc_run` to launch. For exact match, `mgc_list` is also available.

---

## 5.2 API: LIKE patterns

The `/api/mgc/sensitive/get` endpoint accepts SQL LIKE wildcards. For programmatic access:

| Pattern | Matches |
|---------|---------|
| `test` | exact match |
| `%test%` | contains `test` (substring) |
| `test%` | starts with `test` (prefix) |
| `%test` | ends with `test` (suffix) |

> MCP users should prefer `mgc_find` (auto-applies wildcards via `match_mode`) over raw LIKE.

---

# 6. Invocation Model — Who Uses MGC and How

| Caller | Channel | Typical use |
|--------|---------|-------------|
| AI agent | MCP tools | Store / retrieve / run / seal via structured function calls |
| System script | REST API | Embed MGC lookups in CI jobs, scheduled tasks, internal services |
| Human | WebUI | First-time setup, manual entry, audit, deletion, logs |

All three channels share the same encrypted backend; nothing is plaintext on the wire between them and the database.

---

# 7. Trigger Rules — When AI Should Use Which Tool

| User intent | Reach for |
|-------------|-----------|
| "Save this token / password / script" | `mgc_save` |
| "Run my script X" | `mgc_run` (preferred) |
| "What do I have stored?" | `mgc_list` |
| "Find entries matching X" (fuzzy) | `mgc_find` |
| "Seal this script for node B" | `mgc_seal` |
| "Open the interface" | `mgc_open_webui` |
| "Read the value of entry X" | `mgc_get` |

---

# 8. Script Args — How to Use

> This section is its own chapter because script execution with `argparse` parameters is
> the most common interaction shape between AI and MGC.

## 8.1 On store (`mgc_save`)

When you save a Python script with `info_type='script'`, **MGC automatically parses the script and assembles its `argparse` args** into a structured `ext02` field. You do **not** need to manually set `ext02` for script entries.

The parser supports:

- `type=str/int/float/bool`, `default=<literal>`
- `action='store_true' / 'store_false' / 'append' / 'store_const' / 'count'`
- `nargs='+' / '*' / '?' / N`, `choices=`
- `required`, `metavar`, `help`, `dest`

It cannot statically evaluate **dynamic defaults** such as:

```python
default = today.strftime('%Y-%m-%d')        # ast.Call
default = get_default_output_dir()          # ast.Call
default = my_var                            # ast.Name reference
```

For these, MGC detects the dynamic expression, extracts only the static args, and surfaces a `dynamic_args_detected` warning. You can then either re-save the script with literal defaults, or supply your own `ext02` manually.

## 8.2 Recommended workflow at runtime

1. **List the entry** to see its current `ext02`:
   - MCP: `mgc_list` (or call `mgc_get` / `api get` with empty params for the full list)
2. **Inspect `ext02`** — it is a JSON list of strings, e.g. `["--start", "2026-08-08 00:00:00", "--verbose"]`. Each item is one argv token.
3. **Launch with current args** (uses the stored `ext02` as-is):
   - MCP: `mgc_run(info_owner=..., ext01=...)` (omit `ext02` to use the stored value)
   - API: `action='run'` without `ext02` in the request body
   - WebUI: click the green **Run** button — it launches directly with the stored args
4. **Launch with modified args** (when needed):
   - MCP: `mgc_run(info_owner=..., ext01=..., ext02='["--start", "2026-12-25 09:00:00"]')`
   - API: `action='run'` with `ext02` set in the request body
   - WebUI: click the amber **Run with Args** button (shown next to Run when `ext02` is non-empty) to open the JSON editor modal, edit, then click **Run** in the modal.

## 8.3 Format rules for manual `ext02`

When you choose to enter `ext02` manually (rather than letting MGC auto-extract), the value MUST be a valid JSON array string, e.g. `'["--start", "2026-08-08 00:00:00"]'`.

- The WebUI save form enforces this with a JSON validation check before submission.
- The MCP `mgc_save` schema documents the same requirement.
- A legacy string (non-JSON) is still accepted by the API for backward compatibility but will trigger `split()` fallback at runtime.

## 8.4 Notes

- MGC stores the JSON list as-is and passes it directly to `subprocess.run()`, so values containing spaces (e.g. `"2026-08-08 00:00:00"`) are preserved correctly.
- The auto-generated `ext02` is regenerated on every `mgc_save` from the script body.
- Manual `ext02` overrides are **per call only** — they do not mutate the stored entry. To persist a new ext02, re-save the script with `ext02` in the request body.

---

# 9. REST API — System / Script Integration

**Base URL:** `http://127.0.0.1:57219`

**Header:** `X-MGC-Token: <token>`

Token file: `~/.mgc/database/mgc_black_box/.mgc_token`

| Endpoint | Purpose |
|----------|---------|
| `POST /api/mgc/sensitive/save` | Store an entry (mirrors `mgc_save`) |
| `POST /api/mgc/sensitive/get` | Retrieve / list / run an entry (mirrors `mgc_get` / `mgc_list` / `mgc_run`) |
| `POST /api/mgc/sensitive/get` (empty body) | List all stored entries (metadata only) |

> **No interactive API docs** — MGC explicitly disables `/docs` and `/redoc` for security. For full request / response shapes, see the MCP server schema (MCP clients surface it directly to AI agents; for direct API use, see the source code in `mgc/presentation/web/router/`).

---

# 10. Security Model — How MGC Protects Data

- **All data is encrypted locally** (AES-256 at rest).
- **AI can execute but never read plaintext.**
- **Seal is irreversible**: once sealed, the original owner can re-seal with a new key but cannot extract the script back.
- **Execution rights ≠ ownership**: a sealed node can execute but cannot transfer the capsule to a third node.
- **Content never leaves the device in plaintext.**
- **Script execution happens inside the encrypted boundary** — subprocess inherits the encrypted state.

---

# 11. Delete Policy 

Delete functionality is available **via WebUI only** to prevent accidental AI-driven deletion.

---

# 12. Error Handling

| Status | Meaning | AI action |
|--------|---------|-----------|
| `NOT_FOUND` | Entry not found | Use `mgc_list` or ask user |
| `MULTIPLE_MATCHES` | Partial match | Present filtered list to user, ask for refinement |
| Connection failed | MGC not running | MCP auto-starts (or instruct user to run `mgc`) |
| Initialization required | First-time setup | Call `mgc_open_webui` |
| `args_not_recognized` | Script `argparse` parser couldn't identify default args | Verify script has `add_argument(..., default=<literal>)` |
| `dynamic_args_detected` | Script has computed defaults MGC cannot statically evaluate | Re-save with literal defaults, or supply `ext02` manually |

---