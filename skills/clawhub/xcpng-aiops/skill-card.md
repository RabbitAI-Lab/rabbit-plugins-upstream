## Description:

Helps agents inspect and operate XCP-ng fleets through Xen Orchestra, including health analysis, backups, storage, snapshots, and VM actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to triage XCP-ng fleets managed by Xen Orchestra and, when authorized, perform VM, snapshot, and storage operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-accessible write actions can change or destroy VM and snapshot state without an enforced in-tool approval or read-only gate.

Mitigation: Use a dedicated least-privilege Xen Orchestra account, preferably read-only until workflows are tested; explicitly approve and preview consequential changes.

Risk: A master password placed in plaintext MCP client configuration may expose fleet credentials.

Mitigation: Protect client configuration and avoid storing the master password in plaintext where possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [XCP-ng AIops project documentation](https://github.com/AIops-tools/XCPng-AIops)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and command-line or tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fleet status and diagnostic findings may accompany suggested or executed operations.]

## Skill Version(s):

0.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
