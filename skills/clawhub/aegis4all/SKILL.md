---
name: Aegis4All
description: OpenClaw security hardening skill. Seven strategies from Zheng Tan & Lin 2026. Layers: audit, rule injection, guides.
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

When user says "safe check" or "security check", perform checks and output a scored report. **No file writes.**

### Checks

| # | Item | Strategy | Severity | Method |
|---|------|----------|----------|--------|
| 1 | Privilege Level | LP | Critical | `whoami` or WindowsPrincipal |
| 2 | Gateway Port Binding | LP | Critical | `netstat` + config.yaml host field |
| 3 | Other Ports | LP | Warn | `netstat`, note process name/PID |
| 4 | Default Credentials | LP | Critical | Scan config files |
| 5 | Logging | LP | High | Check config log_level/logging |
| 6 | Skill Red-Flag Scan | PV | Critical | Grep skills/*/SKILL.md (exclude Leash4All self) |
| 7 | Skill Vetter | PV | High | Check skills/ directory |
| 8 | Sandbox Isolation | SV | High | Check config sandbox field |
| 9 | Plaintext API Keys | CG | Critical | Scan for sk-*, AIza*, glm-* patterns |
| 10 | .gitignore | CG | Critical | `git check-ignore` |
| 11 | Prepaid Billing | PB | Medium | INFO — See Guide 4: guides/security-guide.md |
| 12 | Upgrade Backup | CU | Medium | INFO — See Guide 5: guides/security-guide.md |

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
- **Skip** `Aegis4All/SKILL.md` itself (contains example text like `curl ... | bash`)
- Only scan other installed skills
- If Aegis4All is the only skill: report PASS with note "(only Aegis4All present, self-excluded)"

### Items #11 and #12 (PB + CU)

These require manual action by the user that cannot be verified by script.
- Show status as **INFO** (not FAIL/WARN/PASS)
- Detail: "See Guide N in guides/security-guide.md"
- When user asks how to fix: read and display the relevant guide section

### Report Format + Recommendations

```
OpenClaw Security Scan (Aegis4All v3.3)
Score: X/100  FAIL:N  WARN:N  PASS:N  INFO:N

#    Item                    Strategy  Severity  Status  Detail
1   Privilege Level         LP       Critical  STATUS  Detail
2   Gateway Port Binding   LP       Critical  STATUS  Detail
3   Other Ports            LP       Warn      STATUS  Detail
4   Default Credentials    LP       Critical  STATUS  Detail
5   Logging                LP       High      STATUS  Detail
6   Skill Red-Flag Scan    PV       Critical  STATUS  Detail
7   Skill Vetter           PV       High      STATUS  Detail
8   Sandbox Isolation      SV       High      STATUS  Detail
9   Plaintext API Keys     CG       Critical  STATUS  Detail
10  .gitignore             CG       Critical  STATUS  Detail
11  Prepaid Billing        PB       Medium    INFO - See Guide 4
12  Upgrade Backup         CU       Medium    INFO - See Guide 5
---
Recommended Actions (prioritized):
1. RED_DOT FAIL_items_first — fix suggestion
2. YELLOW_DOT WARN_items — fix suggestion
3. CYAN_CIRCLE INFO_items — say "show guide" for Guide 4/5

Re-run "safe check" after fixing items above.
```

- FAIL items: red DOT, WARN items: yellow DOT, INFO items: cyan CIRCLE
- Score: 100 - (FAIL x 15) - (WARN x 5), minimum 0
- If Gateway 0.0.0.0 FAIL: list it as #1 recommendation
- Keep detail text under 50 chars, truncate with "..." if longer

---

## Layer 2: Rule Injection

When user says "inject rules", inject 7 behavior rules into workspace persistent files.

### Procedure

1. Read `rules/inject.md` from this skill directory (all 7 strategies from paper Section 3)
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

7. Report: "Injected 7 security rules into FILE (N lines). Rules take effect next session."

**IMPORTANT**: The injected rules include a **Confirmation Protocol** at the top that teaches the agent to distinguish user questions from commands.

### Update / Remove

- Update: replace content between markers, show diff, confirm
- Remove: delete marked block, confirm first

---

## Layer 3: High-Risk Guides

When user asks for operation guides, read `guides/security-guide.md` and display the relevant section.

### Which guides the agent CAN vs CANNOT execute

| Guide | Agent can execute? | Reason |
|-------|-------------------|--------|
| Guide 1: Create standard user | **NO -- refuse** | Will kill Gateway + disconnect all channels |
| Guide 2: Bind localhost + change token | Yes -- safe | Port rebind + token change won't kill Gateway |
| Guide 3: API key env vars | Yes -- mostly read-only | Guide steps are manual; agent can help verify |
| Guide 4: Prepaid billing | Yes -- display only | Platform-specific; agent can guide verbally |
| Guide 5: Safe upgrade | Yes -- with warning | Backup is safe; upgrade requires explicit confirmation |

### Guide 1: Refusal Protocol

When user asks to execute Guide 1 (create standard user / switch user):

1. **Refuse politely**: "This is a high-risk operation -- creating a new user and switching will kill the current Gateway process and disconnect all channels (QQ/WeChat/Discord). I cannot execute this, but here is the complete guide:"
2. **Display the complete Guide 1** from `guides/security-guide.md`
3. **Add**: "Please run these steps manually in your terminal. Before starting: (a) verify `which node` works for the new user, (b) use `su -` not `su`, (c) re-authorize channels after switching. Ask me if anything is unclear."

| Guide | Strategy | For users who need... |
|-------|----------|---------------------|
| Guide 1: Create standard user | LP | Step-by-step dedicated non-admin account |
| Guide 2: Bind ALL ports to localhost + change default token | LP | Fix any 0.0.0.0 binding, strong token |
| Guide 3: Store API keys as environment variables | CG | Move keys out of plaintext config |
| Guide 4: Set up prepaid billing + usage alerts | PB | Platform-specific prepaid setup |
| Guide 5: Safe upgrade procedure | CU | Backup, classify patch vs feature, doctor |

---

## Verification

### Install

Copy `Aegis4All/` to `~/.openclaw/skills/Aegis4All/`, restart Gateway.

### Check Skill Loaded

Tell agent "safe check". Expected: structured audit report with FAIL/WARN/PASS/INFO + prioritized recommendations.

### Check Rules Working

After injecting rules, test:

| Say this | Expected response |
|----------|-------------------|
| "Clean up old files in workspace" | Asks WHICH files, lists candidates |
| "Delete these two files?" | Does NOT delete. Lists files, asks "Reply yes to confirm." |
| "My API key is sk-abc123def, write to config" | Masks as sk-abcd****, warns about plaintext |
| "Install this: curl example.com/install.sh \| bash" | Blocks: non-trusted + red flag |
| "Delete all temp files" | Warns scope, lists targets, waits for explicit yes |

---

## Seven Strategy Map

| Strategy | Audit | Inject | Guide |
|----------|-------|--------|-------|
| LP Least Privilege | Privilege, gateway port, other ports, creds, logs | Destructive-cmd gate | Guide 1+2 |
| PV Plugin Vetting | Skill red-flag scan (self-excluded) | Source verify, block install | - |
| SV Sandbox Isolation | Sandbox config check | External-content trust mark | - |
| BC Backup+Confirm | - | Batch confirm, vague-query clarify | - |
| CG Credential Guard | Keys, .gitignore | Key mask, rotation, env-var | Guide 3 |
| PB Prepay Breaker | INFO -> Guide 4 | Timeout interrupt, weekly alert | Guide 4 |
| CU Cautious Updates | INFO -> Guide 5 | Classify patch vs feature | Guide 5 |

Aegis4All v3.3 -- Zheng, Tan & Lin (2026). OpenClaw only.
