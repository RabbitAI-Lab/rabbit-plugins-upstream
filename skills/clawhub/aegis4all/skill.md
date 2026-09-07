---
name: Aegis4All
version: 4.1
description: OpenClaw security hardening skill. Seven strategies from Zheng Tan & Lin 2026. Layers: audit, rule injection, guides. v4.1 adds 8 new checks + official audit integration + defense mapping.
---

# Aegis4All for OpenClaw

Zheng, J., Tan, J., & Lin, J. (2026). Understanding and mitigating the risks of OpenClaw for non-technical users: A practical guide with Skill. arXiv preprint arXiv:2606.11007. https://arxiv.org/abs/2606.11007


## Trigger Phrases

| Phrase | Action |
|--------|--------|
| "safe check" / "security check" | Layer 1: Audit |
| "inject rules" | Layer 2: Inject |
| "security guide" / "show guide" | Layer 3: Guide |

---

## Layer 1: Config Audit (Read-Only)

When user says "safe check" or "security check", perform checks and output a scored report. **No file writes.** The entire report MUST be output as a single message — do not split across multiple messages, do not output checkpoints one by one.

### Scoring Formula (v4.1)

Total: 100 points. Each checkpoint is weighted by severity:

| Severity | points per item | count | total |
|----------|-----------------|-------|-------|
| Critical | 7 | 10 | 70 |
| High     | 4 | 6 | 24 |
| Warn     | 3 | 2 | 6 |
| INFO | 0               | 2 | 0 |

**Rule:** FAIL → deduct full points. WARN → deduct half points. PASS → no deduction. Score = 100 − sum of deductions. Items #11 and #12 remain INFO (no deduction) per original design.

### Official Audit Integration (v4.1)

Before running the paper-defined checks, invoke `openclaw security audit --json`. Parse the output and match official checkIds to paper checkpoints by prefix:

| Paper # | Official checkId prefix | Notes |
|---------|------------------------|-------|
| 1 | `gateway.process` | Process privilege (uid/Administrator) |
| 2 | `gateway.bind` | Port binding mode |
| 4 | `gateway.auth` | Auth token strength |
| 8 | `sandbox` | Sandbox mode + workspaceAccess + Docker binds |
| 9 | `credential` | Plaintext key scan |
| 13 | `session.dm` | DM pairing policy |
| 14 | `session.group` | Group allowlists + mention gating |
| 15 | `nodes.pairing` | Node auto-pairing + CIDRs |
| 16 | `browser` | Browser control + CDP + SSRF |
| 17 | `tools` | Control-plane tool access |
| 18 | `discovery` | mDNS mode + Tailscale Funnel |
| 19 | `dangerous` | All `dangerously*` configuration keys |

If a matching official checkId is found, use its status and detail. If no match, fall back to the paper hardcoded detection. Paper-only items (#3, #5, #6, #7, #10, #11, #12, #20) always use paper detection.

If `openclaw security audit --json` is not available, all items fall back to the decision rules below, and the report notes that the official audit was unavailable.

**Determinism rule: every checkpoint MUST be evaluated by the exact rule in the "Checkpoint decision rules" section below. Read the stated field or file, compare against the stated condition, assign exactly the stated status. Never guess, never interpret, never improvise. If a field cannot be found, use the rule's fallback case (WARN or absent-case).**

### Checks

| # | Item | Strategy | Severity | Method |
|---|------|----------|----------|--------|
| 1 | Privilege Level | LP | Critical | `whoami` or WindowsPrincipal |
| 2 | Gateway Port Binding | LP | Critical | `netstat` + config.yaml host field |
| 3 | Other Ports | LP | Warn | `netstat`, note process name/PID |
| 4 | Default Credentials | LP | Critical | Scan config files |
| 5 | Logging | LP | High | Check config log_level/logging |
| 6 | Skill Red-Flag Scan | PV | Critical | Grep skills/*/SKILL.md (exclude Aegis4All self) |
| 7 | Skill Vetter | PV | High | Check skills/ directory |
| 8 | Sandbox Isolation | SV | High | Check config sandbox field |
| 9 | Plaintext API Keys | CG | Critical | Scan for sk-*, AIza*, glm-* patterns |
| 10 | .gitignore | CG | Critical | `git check-ignore` |
| 11 | Prepaid Billing | PB | Medium | INFO — See Guide 4: guides/security-guide.md |
| 12 | Upgrade Backup | CU | Medium | INFO — See Guide 5: guides/security-guide.md |
| 13 | DM Pairing Policy | LP | Critical | Check session.dmScope + channel dmPolicy |
| 14 | Group Allowlists & Mention Gating | LP | High | Check groupPolicy, requireMention, groupAllowFrom |
| 15 | Node Pairing Exposure | LP | Critical | Check autoApproveCidrs + node commands |
| 16 | Browser Control Exposure | SV | High | Check dangerouslyAllowPrivateNetwork + CDP ports |
| 17 | Control-Plane Tool Lockdown | LP | High | Check tools.deny for gateway/cron/sessions_spawn/sessions_send |
| 18 | Network Exposure Beyond Ports | LP | Warn | Check mDNS mode + Tailscale Funnel |
| 19 | Dangerous Flags Scan | SV | Critical | Scan all `dangerously*` keys in config |
| 20 | CVE Version Check | CU | Critical | Compare current version vs CVEs (jgamblin/OpenClawCVEs) |

### Checkpoint decision rules (deterministic - follow exactly, do not interpret or improvise)

For every checkpoint, read the specified field or file, compare against the rule below, and assign exactly the stated status. Do not add your own judgement. Do not invent values.

**1. Privilege Level** (LP, Critical)
- Read: process owner via whoami command (Linux: also id)
- PASS: output is not root or Administrator
- FAIL: output is root or Administrator

**2. Gateway Port Binding** (LP, Critical)
- Read: gateway.bind field in openclaw.json (or config.yaml)
- PASS: value is exactly loopback
- FAIL: value is lan or custom
- WARN: field is absent

**3. Other Ports** (LP, Warn)
- Read: listening ports via netstat (read-only command)
- PASS: none of ports 3306, 445, 135, 2375, 2376 is listening on 0.0.0.0
- WARN: any of those ports is listening on 0.0.0.0 (note process name and PID in Detail)

**4. Default Credentials** (LP, Critical)
- Read: the gateway auth token field in openclaw.json
- PASS: token length is 20 characters or more and does not match known defaults
- FAIL: token length is under 20 characters or matches a known default
- WARN: field is absent

**5. Logging** (LP, High)
- Read: tools.logging and session.logging fields in openclaw.json
- PASS: both fields present and set to true
- WARN: either field is absent or set to false

**6. Skill Red-Flag Scan** (PV, Critical)
- Read: every installed skill's SKILL.md file (skip Aegis4All itself)
- Scan for: remote-install pipe patterns, recursive deletion patterns, dynamic evaluation patterns, dangerously-prefixed keys, unsafe external content flags
- PASS: no pattern found in any skill
- FAIL: at least one pattern found (name the skill in Detail)
- If Aegis4All is the only installed skill: PASS with note (only Aegis4All present, self-excluded)

**7. Skill Vetter Installed** (PV, High)
- Read: the skills directory listing
- PASS: a skill-vetter package is present
- WARN: no skill-vetter package found

**8. Sandbox Isolation** (SV, High)
- Read: agents.defaults.sandbox.mode and workspaceAccess fields in openclaw.json
- PASS: mode is all and workspaceAccess is ro (read-only is the maximum safe setting)
- FAIL: mode is off or the field is absent
- WARN: mode is all but workspaceAccess is rw
- CRITICAL: workspaceAccess set to none is NEVER a passing state (the agent must read its workspace); if found, set FAIL and instruct to change it to ro
- Additionally: if any Docker bind mounts a blocked path (etc, proc, sys, ssh keys directory), set FAIL

**9. Plaintext API Keys** (CG, Critical)
- Read: openclaw.json and workspace text files
- Scan for: sk-, sk-ant-, org-, api_key=, Bearer
- PASS: no pattern found
- FAIL: any pattern found (name the file in Detail)

**10. .gitignore** (CG, Critical)
- Read: workspace root directory listing
- PASS: .gitignore exists and contains .env, *.key, *.pem, credentials.json, secrets.*
- FAIL: no .gitignore file exists
- WARN: file exists but is missing at least one required entry

**11. Prepaid Billing** (PB, Medium)
- Always INFO. Detail: See Guide 4.

**12. Upgrade Backup** (CU, Medium)
- Always INFO. Detail: See Guide 5.

**13. DM Pairing Policy** (LP, Critical)
- Read: each channel's dmPolicy field in openclaw.json
- PASS: every channel dmPolicy is pairing or allowlist
- FAIL: any channel dmPolicy is open or absent
- WARN: dmPolicy restricted but session.dmScope not set to a per-channel value

**14. Group Allowlists** (LP, High)
- Read: groupPolicy, requireMention, groupAllowFrom fields in openclaw.json
- PASS: groupAllowFrom contains explicit user identifiers and requireMention is true
- FAIL: groupPolicy is open without mention gating
- WARN: groupAllowFrom is empty or wildcard

**15. Node Pairing Exposure** (LP, Critical)
- Read: gateway.nodes.pairing.autoApproveCidrs and node commands allow list
- PASS: autoApproveCidrs is empty or absent, and system.run is not allowed without a deny entry
- FAIL: autoApproveCidrs contains any CIDR, or system.run allowed without a deny entry

**16. Browser Control Exposure** (SV, High)
- Read: browser.ssrfPolicy.dangerouslyAllowPrivateNetwork and browser CDP or relay port settings
- PASS: dangerouslyAllowPrivateNetwork is false or absent, and no CDP or relay port bound beyond loopback
- FAIL: a CDP or relay port bound to a non-loopback address
- WARN: dangerouslyAllowPrivateNetwork is true

**17. Control-Plane Tool Lockdown** (LP, High)
- Read: tools.deny field in openclaw.json
- CRITICAL SAFETY: gateway, cron, sessions_spawn, sessions_send are required for the agent itself to operate. NEVER mark FAIL just because the main agent's deny list does not include them. Do NOT add them to the main agent's deny list.
- PASS: the main agent's deny list does not disable its own required tools (gateway, cron, sessions_*), OR the deny list exists for dedicated untrusted-content agents only
- WARN: tools.deny is configured in a way that disables the main agent's own control-plane tools

**18. Network Exposure Beyond Ports** (LP, Warn)
- Read: discovery.mdns.mode and Tailscale Funnel settings
- PASS: mdns mode is off, minimal, or absent, and Funnel is disabled
- WARN: mdns mode is full or Funnel is enabled

**19. Dangerous Flags Scan** (SV, Critical)
- Read: every key in openclaw.json starting with dangerously, and allowUnsafeExternalContent keys in hooks
- PASS: no such key exists, or all such keys are false
- FAIL: any such key present with value true

**20. CVE Version Check** (CU, Critical)
- Read: current OpenClaw version via the version command
- Compare: CVE-2026-25253 requires 2026.1.29 or later; CVE-2026-44112 and CVE-2026-41295 require versions stated in the official advisory (full list at jgamblin/OpenClawCVEs)
- PASS: current version meets or exceeds every listed fixed version
- FAIL: current version below any fixed version (name the CVE and required version in Detail)

### Execution Rule: COLLECT ALL, OUTPUT ONCE

**CRITICAL: Do NOT output any text to the user during the collection phase. Your first message to the user must be the complete report.**

This means:
- The user sees exactly ONE message from you, containing the full report
- No "Running checks...", no "Checking item 1...", no progress updates
- No "Part 1 of 3", no "Continuing...", no "(continued)"
- Run all checks silently. Only speak when the full report is ready.

Execution order:
1. Run `openclaw security audit --json` (silently, no output to user). For each checkpoint with a matching official checkId prefix (see mapping above), use the official status directly.
2. For checkpoints without an official match, evaluate using the exact rules in "Checkpoint decision rules" below (silently, no output to user).
3. Collect all 20 results into one data structure in memory.
4. Assign each item: status + source + detail string (≤50 chars)
5. Compute the score using the weighted formula
6. Build the recommended actions from the Defense Mapping table
7. **NOW output the complete report as a single code block**

**The complete report (all 20 rows) is generated and sent in ONE message. Do not shorten anything, do not compress, do not send partial rows first. NEVER output the report twice: if any part of the report has already been sent, do not resend the full report. The report is sent exactly once.**

### Fix Follow-up (repair loop)

After outputting the complete report, the agent MUST offer to fix the detected problems. This is the repair loop that actually changes the score — the report alone cannot.

**After the report, continue the conversation freely.** Offer to fix the detected problems in natural language, e.g., "I found 6 fixable issues. Do you want me to fix them?" — adapt the wording to the conversation. Then wait for the user's reply. Do NOT execute any fix before the user confirms.

**When the user replies with a fix request:**
1. Read the fix instruction for the requested item from the Defense Mapping table
2. Confirm the exact change with the user: "I will set X to Y in openclaw.json. Proceed?"
3. On confirmation, apply the change (config edits are allowed after user confirmation — this is the repair loop)
4. Re-run `safe check` and report the new score
5. If the score improved, state the improvement: "Score: X → Y. Fixed: <items>."

**Rules for the repair loop:**
- Never apply a fix without explicit user confirmation (Guide 1 is always REFUSED, see Layer 3)
- NEVER restart the Gateway as part of a fix. Config edits take effect on the next user-initiated restart; instruct the user to restart manually instead.
- NEVER disable the agent's own required tools (gateway, cron, sessions_spawn, sessions_send) on the main agent. Fixing item 17 means verifying deny lists are applied only to dedicated untrusted-content agents, not adding deny entries to the main agent.
- NEVER modify the Gateway's own communication channel, port binding, or channel credentials as part of a fix (that is Guide 1/2 territory — REFUSED, display the guide instead)
- After a successful fix, always re-run `safe check` so the user sees the new score
- Fixable items: only those rated EXECUTABLE or CONDITIONAL (precondition met) in the Defense Mapping table. Items rated ADVISORY or REFUSED are shown as guides, never applied automatically. `fix all` applies only EXECUTABLE/CONDITIONAL items and always displays the guides for the rest.
- If the user asks for a fix that requires a manual step (Guide 1/4/5), display the guide instead of refusing silently

**The report itself is output exactly once. After the report, the agent continues the conversation freely: summary, comparison with previous runs, plain-language risk explanation, and a question offering to fix the found items. Never resend the report.

### Port Binding Rule (Items #2 and #3)

**ALL listening ports must be bound to 127.0.0.1.**

Step 1: Read OpenClaw config.yaml to find expected gateway port(s).

Step 2: Run `netstat -an` (Windows) or `netstat -tlnp` (Linux). For each listening port:

- **If port matches OpenClaw gateway AND bound to 0.0.0.0**:
  - Report as **FAIL [LP-Critical]** in item #2
  - This is the #1 attack vector — anyone can reach your Agent
  - Recommendation: "Fix immediately -> See Guide 2 in guides/security-guide.md"

- **If port is NOT OpenClaw gateway but bound to 0.0.0.0**:
  - Report as **WARN [LP-Warn]** in item #3
  - Note the owning process name and PID
  - Recommendation: either bind to localhost, or add firewall rule to restrict source IPs

- **If port is on 127.0.0.1 or [::1]**:
  - Report as PASS

### Self-Exclusion for Red-Flag Scan (Item #6)

When scanning skills for red-flag patterns:
- **Skip** `Aegis4All/SKILL.md` itself (contains example text of remote-install pipe patterns)
- Only scan other installed skills
- If Aegis4All is the only skill: report PASS with note "(only Aegis4All present, self-excluded)"

### Items #11 and #12 (PB + CU)

These require manual action by the user that cannot be verified by script.
- Show status as **INFO** (not FAIL/WARN/PASS)
- Detail: "See Guide N in guides/security-guide.md"
- When user asks how to fix: read and display the relevant guide section

### Report Format + Recommendations

**The entire report is ONE message in ONE code block. Copy the EXACT template below and only replace the STATUS and DETAIL values. Do not change column names, do not reorder rows, do not abbreviate item names, do not add or remove rows.**

**Version placement rule: the report title line must NOT contain the skill name or version. The skill name and version appear only at the very end, after the closing line.**

```
Score: X/100  FAIL:N  WARN:N  PASS:N  INFO:N

#  Checkpoint                    Status      Detail
1  Privilege Level               PASS        Running as ubuntu (uid=1000)
2  Gateway Port Binding          PASS        bind = loopback
3  Other Ports                   PASS        No risky ports on 0.0.0.0
4  Default Credentials           PASS        Custom token, length OK
5  Logging                       WARN        tools.logging absent
6  Skill Red-Flag Scan           PASS        No dangerous patterns
7  Skill Vetter                  WARN        Not installed
8  Sandbox Isolation             FAIL        sandbox.mode absent
9  Plaintext API Keys            PASS        No key patterns found
10 .gitignore                    FAIL        No .gitignore file
11 Prepaid Billing               INFO        See Guide 4
12 Upgrade Backup                INFO        See Guide 5
13 DM Pairing Policy             FAIL        dmPolicy = open
14 Group Allowlists              FAIL        groupPolicy = open
15 Node Pairing Exposure         PASS        No autoApproveCidrs
16 Browser Control Exposure      WARN        dangerouslyAllowPrivateNetwork = true
17 Control-Plane Tool Lockdown   FAIL        tools.deny missing 4 entries
18 Network Exposure              PASS        mDNS off, Funnel inactive
19 Dangerous Flags Scan          FAIL        dangerouslyAllowPrivateNetwork = true
20 CVE Version Check             PASS        version meets CVE fixes

Fix (N items):
1. FAIL: <item name> -> <fix from Defense Mapping>
2. FAIL: <item name> -> <fix from Defense Mapping>

Also fix (N WARN + N INFO): <comma-separated item names>. Type "show guide".

Re-run "safe check" after fixing items above.

Aegis4All v4.1
```

**Rules for filling the template:**
- **Score line:** exactly `Score: X/100  FAIL:N  WARN:N  PASS:N  INFO:N`. FAIL and CRIT FAIL both count in FAIL. INFO items count in INFO. No other labels on this line.
- **Status column values (exactly one of):** `PASS`, `FAIL`, `WARN`, `INFO`. Status implies severity (CRIT FAIL=Critical, FAIL=High, WARN=Warn, INFO=Info). Do not write "CRIT FAIL" in the Status column — the severity is not shown in the report.
- **Item names:** use EXACTLY the names in the template above. Never abbreviate, never add suffixes like "/Mention".
- **Detail column:** ≤30 chars. If longer, truncate with "..." . Never blank.
- **Status markers in Fix list:** FAIL items listed first with `->` fix text from Defense Mapping. WARN and INFO items merged into one "Also fix" line.
- **After the closing line and version line, offer fixes in natural language** (see Fix Follow-up section above).
- **Never output the report twice. Never continue the report in a second message. The report is ONE message, sent once.**

**The report is always output in full. Never shorten Detail, never merge rows, never split across messages.**

### Defense Mapping (v4.2 — fix instruction per checkpoint, safety-rated)

Every FAIL or WARN in the Recommended Actions must reference the fix instruction below. This is the single source of truth for "how to fix."

**Fix safety rating:**
- **EXECUTABLE** — safe for the agent to apply automatically (config edits, file creation). No restart needed, no risk of locking the agent out.
- **CONDITIONAL** — safe ONLY if the stated precondition holds (e.g., the current user is on the allowlist). Verify the precondition first; if it fails, downgrade to ADVISORY.
- **ADVISORY** — display the guide, the user performs it manually. Do NOT attempt automatically.
- **REFUSED** — never perform. Display the guide with a refusal explanation.

| # | Fix instruction | Rating | Guide |
|---|----------------|--------|-------|
| 1 | Create a dedicated standard user account | REFUSED | Guide 1 |
| 2 | Set `gateway.bind` to `"loopback"` | ADVISORY — changing bind requires a Gateway restart and may disconnect the agent; user must do it in a terminal | Guide 2 |
| 3 | Close unnecessary ports or bind them to `127.0.0.1` | ADVISORY — may affect non-OpenClaw services; user decides | — |
| 4 | Rotate the gateway auth token | REFUSED — rotating the token invalidates the agent's own current authentication; user must run it in a terminal | Guide 2 |
| 5 | Enable `tools.logging` and `session.logging` | EXECUTABLE — config edit only | — |
| 6 | Remove or quarantine the flagged skill | CONDITIONAL — list the exact skill first, confirm with user, never remove Aegis4All itself | — |
| 7 | Install the Skill Vetter package | ADVISORY — requires network install from ClawHub; user confirms | — |
| 8 | Enable sandbox mode | CONDITIONAL — set `workspaceAccess` to `"ro"` at most, NEVER `"none"` (the agent must read its workspace); only set `mode` to `"all"` if a sandbox runtime (e.g., Docker) is present, otherwise WARN and show guide | — |
| 9 | Move API keys to a `.env` file | ADVISORY — if the `.env` is not loaded correctly, the agent loses model access and stops responding; user performs with verification | Guide 3 |
| 10 | Create `.gitignore` | EXECUTABLE — file creation only | — |
| 11 | Switch to prepaid billing | ADVISORY — third-party platform | Guide 4 |
| 12 | Back up config and workspace | EXECUTABLE — copy operation only | Guide 5 |
| 13 | Set `dmPolicy` to `"pairing"` or `"allowlist"` | CONDITIONAL — first verify the current user's ID is on the allowlist, otherwise the agent locks itself out of its own DM channel; if not verifiable, downgrade to ADVISORY | Guide 6 |
| 14 | Set `groupAllowFrom` and enable `requireMention` | CONDITIONAL — first verify the current user's ID is included in groupAllowFrom, otherwise the agent can no longer hear group messages; if not verifiable, downgrade to ADVISORY | Guide 6 |
| 15 | Clear `autoApproveCidrs` and deny `system.run` on nodes | EXECUTABLE — config edit only | Guide 6 |
| 16 | Set `dangerouslyAllowPrivateNetwork` to `false` | EXECUTABLE — config edit only | — |
| 17 | Control-plane tool deny lists | CONDITIONAL — NEVER add deny entries for gateway/cron/sessions_* on the main agent; deny lists apply only to dedicated untrusted-content agents | — |
| 18 | Set mDNS mode and disable Tailscale Funnel | EXECUTABLE — config edit only | Guide 6 |
| 19 | Remove `dangerously*` keys set to true | EXECUTABLE — config edit only; do not touch keys required by the running Gateway | — |
| 20 | Upgrade OpenClaw to the required version | ADVISORY — upgrade requires restart and may change behavior; user performs with backup | Guide 5 |

**Safety rules for automatic fixes (MUST NOT be violated):**
1. A fix must NEVER remove the agent's ability to: call its model (API keys), read its workspace, use its own tools, or receive messages from the current user.
2. A fix must NEVER restart the Gateway. Config changes take effect on the next user-initiated restart.
3. A fix that touches the agent's own communication channel (bind, auth token, dmPolicy, groupAllowFrom) must be verified against the current user first; unverifiable changes are downgraded to ADVISORY or REFUSED.
4. Only EXECUTABLE and CONDITIONAL (precondition met) items may be applied by `fix all`. ADVISORY and REFUSED items are always shown as guides.

## Layer 2: Rule Injection

When user says "inject rules", inject 8 behavior rules into workspace persistent files.

### Procedure

1. Read `rules/inject.md` from this skill directory (all 8 strategies from paper Section 3)
2. Read target file: try `TOOLS.md` first, then `AGENTS.md`, then `MEMORY.md`
3. Check if Aegis4All rules already exist in target file
4. Show what will be added (or diff if updating)
5. Ask user to confirm: "About to write N lines to FILE. Proceed?"
6. On confirmation: append content from `rules/inject.md` wrapped with markers:

```
## Aegis4All Security Rules

[content from rules/inject.md]

## END Aegis4All RULES
```

7. Report: "Injected 8 security rules into FILE (N lines). Rules take effect next session."

**IMPORTANT**: The injected rules include a **Confirmation Protocol** at the top that teaches the agent to distinguish user questions from commands.

### Update / Remove

- Update: replace content between markers, show diff, confirm
- Remove: delete marked block, confirm first

---

## Layer 3: High-Risk Guides

When user says "show guide" or "security guide", output a compact index of ALL 6 guides in ONE message. Do NOT read `guides/security-guide.md` for the index — the full file is too long and will cause splitting. Only read the file when user asks for a specific guide by number.

### Guide Index (ONE message, compact format)

```
Guide 1 — Create Standard User — REFUSED
  Create a non-admin OS account and restart Gateway under it.
  See full guide: "show guide 1"

Guide 2 — Bind Localhost + Rotate Token — EXECUTABLE
  Set gateway.bind to loopback and generate a strong auth token.
  See full guide: "show guide 2"

Guide 3 — Move API Keys to .env — EXECUTABLE
  Store secrets in .env file; keep settings in main JSON config.
  See full guide: "show guide 3"

Guide 4 — Prepaid Billing — ADVISORY (third-party platform)
  Switch to prepaid credits with monthly hard limit.
  See full guide: "show guide 4"

Guide 5 — Safe Update — ADVISORY (manual judgment)
  Backup config, read changelog, update early for security.
  See full guide: "show guide 5"

Guide 6 — Lock Down DM & Group — EXECUTABLE
  Enable pairing, set allowlists, disable node auto-pairing, tighten mDNS.
  See full guide: "show guide 6"

Type "show guide N" for full instructions on any guide.

Aegis4All v4.1
```

**Output rule:** The entire guide index is ONE message. Never split. Never output guides one by one unless user asks for a specific number.

### Which guides the agent CAN vs CANNOT execute

| Guide | Agent can execute? | Reason |
|-------|-------------------|--------|
| Guide 1: Create standard user | **NO -- refuse** | Will kill Gateway + disconnect all channels |
| Guide 2: Bind localhost + change token | Yes -- safe | Port rebind + token change won't kill Gateway |
| Guide 3: API key env vars | Yes -- mostly read-only | Guide steps are manual; agent can help verify |
| Guide 4: Prepaid billing | Yes -- display only | Platform-specific; agent can guide verbally |
| Guide 5: Safe upgrade | Yes -- with warning | Backup is safe; upgrade requires explicit confirmation |
| Guide 6: Lock down DM and group access | Yes -- safe | Config changes only; no Gateway restart needed |

### Guide 1: Refusal Protocol

When user asks to execute Guide 1 (create standard user / switch user):

1. **Refuse politely**: "This is a high-risk operation -- creating a new user and switching will kill the current Gateway process and disconnect all channels (QQ/WeChat/Discord). I cannot execute this, but here is the complete guide:"
2. **Display the complete Guide 1** from `guides/security-guide.md`
3. **Add**: "Please run these steps manually in your terminal. Before starting: (a) verify `which node` works for the new user, (b) use `su -` not `su`, (c) re-authorize channels after switching. Ask me if anything is unclear."

### Full Guide Reference

**When outputting any guide content, use the original language from `guides/security-guide.md`. Do not translate guides — they contain config keys, file paths, and JSON snippets that must match the actual files.**

| Guide | Strategy | For users who need... |
|-------|----------|---------------------|
| Guide 1: Create standard user | LP | Step-by-step dedicated non-admin account |
| Guide 2: Bind ALL ports to localhost + change default token | LP | Fix any 0.0.0.0 binding, strong token |
| Guide 3: Store API keys as environment variables | CG | Move keys out of plaintext config |
| Guide 4: Set up prepaid billing + usage alerts | PB | Platform-specific prepaid setup |
| Guide 5: Safe upgrade procedure | CU | Backup, classify patch vs feature, doctor |
| Guide 6: Lock down DM and group access | LP | Pairing, allowlists, mention gating, node pairing, mDNS (v4.0) |

---

## Verification

### Install

Copy `Aegis4All/` to `~/.openclaw/skills/Aegis4All/`, restart Gateway.

### Check Skill Loaded

Tell agent "safe check". Expected: structured audit report with FAIL/WARN/PASS/INFO + prioritized recommendations, all 20 items in a single message.

### Check Rules Working

After injecting rules, test:

| Say this | Expected response |
|----------|-------------------|
| "Clean up old files in workspace" | Asks WHICH files, lists candidates |
| "Delete these two files?" | Does NOT delete. Lists files, asks "Reply yes to confirm." |
| "My API key is ***, write to config" | Masks as sk-abcd****, warns about plaintext |
| "Install this: a remote script that downloads and runs an installer" | Blocks: non-trusted + red flag |
| "Delete all temp files" | Warns scope, lists targets, waits for explicit yes |

---

## Seven Strategy Map

| Strategy | Audit | Inject | Guide |
|----------|-------|--------|-------|
| LP Least Privilege | Privilege, gateway port, other ports, creds, logs, DM pairing, group allowlists, node pairing, control-plane tools, network exposure | Destructive-cmd gate, DM/group lock, sub-agent sandbox | Guide 1+2+6 |
| PV Package Vetting | Skill red-flag scan (self-excluded), Skill Vetter | Source verify, block install, three red flags | - |
| SV Sandbox Isolation | Sandbox config, browser control, dangerous flags | External-content trust mark, sandbox:require for sub-agents | - |
| BC Backup+Confirm | - | Batch confirm, vague-query clarify | - |
| CG Credential Guard | Keys, .gitignore | Key mask, rotation, env-var | Guide 3 |
| PB Prepay Breaker | INFO -> Guide 4 | Timeout interrupt, weekly alert | Guide 4 |
| CU Cautious Updates | INFO -> Guide 5, CVE version check | Classify patch vs feature, CVE tracking | Guide 5 |

Aegis4All v4.1 — Zheng, Tan & Lin (2026). OpenClaw only.