# Agent DNA

## Purpose

Agent DNA creates a persistent behavioral identity for AI agents.

Instead of trusting every action equally, Agent DNA builds a trust profile from observed behavior and evaluates every future action against that profile.

## Identity Signals

Track:

- Agent ID
- Session ID
- Model
- Organization
- User
- Available Tools
- Permissions

## Behavioral Signals

Observe:

- Tool usage
- Tool sequence
- API frequency
- Prompt changes
- Goal changes
- Context changes
- Risk level
- Approval history
- Previous violations

## Runtime Decision

For every action determine:

- Allow
- Approval Required
- Block

## Risk Indicators

Increase risk when:

- New tools appear unexpectedly
- Agent attempts privileged operations
- Behavior differs from historical profile
- Prompt injection is suspected
- Sensitive data access increases
- Financial actions exceed policy

## Output

Produce:

- Agent DNA Fingerprint
- Behavioral Trust Score
- Risk Score
- Decision
- Explanation

## Principles

- Never trust by default.
- Verify every decision.
- Minimize unnecessary privilege.
- Prefer human approval for high-risk actions.
- Maintain a complete audit trail.


## Examples

### Example 1 — GitHub

Action:
Merge pull request to main

Behavior:
New repository
Outside business hours
High-risk permissions

Decision:
Approval Required

---

### Example 2 — Banking

Action:
Transfer $2,000,000

Behavior:
Amount exceeds policy
No prior approvals

Decision:
Block

---

### Example 3 — Healthcare

Action:
Update patient medication

Behavior:
Sensitive clinical workflow

Decision:
Approval Required

---

### Example 4 — MCP

Action:
Invoke filesystem.delete

Behavior:
First time using destructive tool

Decision:
Approval Required

---

### Example 5 — Normal Operation

Action:
Read documentation

Behavior:
Low risk
Previously observed behavior

Decision:
Allow

Append:

## Current Capabilities

- Inspect Agent DNA
- Generate Behavioral Fingerprint
- Runtime Trust Analysis
- Receipt Verification

## Upcoming

- Compare Agent DNA
- Attest Agent DNA
- Verify Agent DNA
- Drift Detection
