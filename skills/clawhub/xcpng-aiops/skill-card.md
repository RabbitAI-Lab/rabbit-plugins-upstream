## Description:

XCP-ng AIops helps agents operate XCP-ng virtualization fleets through Xen Orchestra with fleet health summaries, RCA workflows, audited read tools, and governed write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and infrastructure operators use this skill to triage XCP-ng fleets managed by Xen Orchestra, diagnose VM, storage, backup, and pool issues, and execute audited operations such as VM lifecycle changes and snapshot handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact Xen Orchestra write actions and has no internal read-only or approval gate.

Mitigation: Use a dedicated least-privilege Xen Orchestra account, prefer read-only ACLs for triage, and treat write tools as capable of stopping, rebooting, migrating, deleting snapshots, or reverting VMs whenever the token permits it.

Risk: Credential handling is required for Xen Orchestra access.

Mitigation: Avoid storing the master password plainly in MCP configuration and do not pass Xen Orchestra tokens on the command line.

Risk: Production use can execute sensitive infrastructure changes.

Mitigation: Review the skill before installing in production, pin the package version that was reviewed, and require operator review for destructive workflows.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [capabilities.md](references/capabilities.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)
- [cli-reference.md](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP and CLI workflows may return dry-run previews, undo identifiers, audit context, and truncation flags.]

## Skill Version(s):

0.8.1 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
