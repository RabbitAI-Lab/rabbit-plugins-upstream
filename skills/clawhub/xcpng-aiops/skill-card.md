## Description:

xcpng-aiops helps agents inspect and operate XCP-ng fleets through Xen Orchestra, covering fleet health, VM, host, pool, storage, snapshot, backup, and task views plus RCA workflows and governed writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to triage and operate XCP-ng environments managed by Xen Orchestra. It is intended for fleet health checks, VM and storage RCA, backup failure analysis, patch and HA posture review, and guarded operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run external package code with Xen Orchestra credentials.

Mitigation: Pin and verify the xcpng-aiops package where possible, run it under a dedicated local account, and connect with a least-privilege XO user until write access is explicitly needed.

Risk: VM, migration, and snapshot write actions can affect a live XCP-ng fleet, and snapshot delete or revert actions are irreversible.

Mitigation: Start from read-only XO permissions for triage, require operator review before writes, use dry-run previews, and rely on CLI double confirmation for destructive actions.

Risk: XO tokens and the master password can be exposed if placed in command lines or persistent configuration files.

Mitigation: Use the encrypted secret store, keep secrets out of command arguments and durable config, and provide the master password only through controlled runtime environment handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [xcpng-aiops - Capabilities](references/capabilities.md)
- [xcpng-aiops - Setup & security guide](references/setup-guide.md)
- [xcpng-aiops - CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured command guidance, with JSON returned by CLI and MCP operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run previews, RCA findings, audit-oriented guidance, and configuration snippets for Xen Orchestra connectivity.]

## Skill Version(s):

0.8.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
