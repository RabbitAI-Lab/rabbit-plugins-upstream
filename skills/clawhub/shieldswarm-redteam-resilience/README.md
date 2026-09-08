# 🛡️ shieldswarm-redteam-resilience

**Categories:** security, operations, agents  
**Public tags:** #security, #red-team, #resilience, #secops, #multi-agent

## ✨ Functionalities

Defensive multi-agent SRE/SecOps red-team/purple-team resilience commander
with **working** tooling: deterministic mode selection, a fail-closed command
validator, an append-only approval gate with separation of duties, a
machine-readable model quality-floor matrix (cloud-only policy), evidence
redaction checklists, and a self-improvement feedback loop. Defensive-only,
authorization-gated.

v2.1.0 ships the four operational scripts that v2.0.1 only referenced
(`mode_selector.sh`, `shieldswarm_validate.sh`, `approval_gate.sh`,
`quality_floor_check.sh`), five lazy-loaded reference playbooks, the flat
`quality_floor_matrix.yaml`, and `self_improve.py`. The bundled
`tools/shieldswarm_selftest.py` now performs 12 offline check groups,
including functional PASS/FAIL smoke tests of every script.

The authoritative agent-facing instructions live in `SKILL.md` (command
contracts, hard safety rules, quality floor, load map). Detailed playbooks
are in `references/`; 25 workflow templates are in `templates/`.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/shieldswarm-redteam-resilience
```

Representative commands (all offline, deterministic, `--help` supported):

```bash
# 1. Pick the mode for a symptom
bash scripts/mode_selector.sh --symptom "cannot login" --evidence public
# -> mode=support_without_login action=collect_user_side_evidence required=templates/no_login_diagnostic.md

# 2. Validate a proposed command (fail-closed)
bash scripts/shieldswarm_validate.sh --command "curl -s https://status.example.com" --mode operator
# -> check=... lines, then verdict=PASS

# 3. Record a high-risk approval (approver must differ from owner + operator)
bash scripts/approval_gate.sh --scope "restart gateway" --risk high \
     --rollback-owner alice --approver bob

# 4. Gate a model choice against the quality floor (cloud-only)
bash scripts/quality_floor_check.sh --task "security code review" --proposed-model "claude-opus-5"
# -> verdict=PASS  (below-floor or local models -> verdict=FAIL)

# 5. Verify the whole package offline
python3 tools/shieldswarm_selftest.py
# -> ALL CHECKS PASSED
```

Define authorization and rules of engagement first, choose the defensive
workflow, record approvals, run bounded checks, and retain
rollback/postmortem evidence.

## 🔐 Permissions & Requirements

• Runs local defensive scripts (bash 3.2+, coreutils; python3 stdlib for
  tools) and templates — **no network calls from the skill itself**
• May append approval records to a local JSONL file (`approval.jsonl`,
  chmod 600) and feedback events to `feedback.jsonl`
• Authorization-gated: requires explicit approvals (separation of duties for
  high-risk changes)

All permissions above are capability requirements, not blanket
authorization. Grant only what the selected workflow needs, scope
filesystem access to the working directory, and do not elevate privileges
unless SKILL.md explicitly requires and explains it.

## 🔒 Security & Privacy

- Defensive-only and authorization-gated by design.
- Approval logs and feedback logs are written locally and never uploaded.
- No secrets beyond what you configure; scripts reject commands containing
  credential patterns (fail-closed).
- Use only on systems you are authorized to test.
- **Data handling:** the skill reads only user-selected inputs and files
  described above; it must not collect unrelated data.
- **Storage/logging:** `approval.jsonl` (chmod 600) and `feedback.jsonl`
  can contain operational context; protect them and redact before sharing.
- **Network boundary:** the skill makes no network requests; any external
  calls come from your own operational commands, which must pass the
  validator.
- **Secrets:** API keys, tokens, passwords, and credentials must never be
  embedded in the skill or logged. Store required secrets in chmod-600
  credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before
  installation, use least privilege, and verify all generated output before
  relying on it.

## ✅ Verification Hash

sha256 of all package files except `README.md` and server-managed files
(`.clawhub/`, `_meta.json`), computed at publish time:

```
80ac87d2782ae970370acfe46adfb64646a5aa711a14ae84368fe333ebe40d38
```

Verify after install (run from the skill folder):

```bash
find . -type f ! -name "README.md" ! -path "./.clawhub/*" ! -name "_meta.json" \
  | sed 's|^\./||' | LC_ALL=C sort | xargs sha256sum | sha256sum | awk '{print $1}'
```
