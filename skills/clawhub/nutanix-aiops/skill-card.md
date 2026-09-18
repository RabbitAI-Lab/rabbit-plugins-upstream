## Description:

Governed Nutanix Prism Central v4 operations for estate health, cluster and VM lifecycle, storage, networking, data protection, alerts, LCM upgrades, capacity forecasting, and diagnostics/RCA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, infrastructure operators, and SRE teams use this skill to inspect and operate Nutanix Prism Central v4 estates through governed CLI and MCP workflows. It supports read-only diagnosis as well as audited, dry-run-capable infrastructure changes when the connected account has suitable permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Nutanix infrastructure changes when connected with a sufficiently privileged Prism Central account.

Mitigation: Start with a Viewer/read-only Prism Central account, require explicit operator approval before destructive MCP actions, and use dry-run previews before executing changes.

Risk: The skill has no enforced read-only mode or built-in approval gate.

Mitigation: Use Prism Central role permissions as the authorization boundary and keep an external approval process for write and destructive operations.

Risk: Credential exposure could grant broad access to Prism Central operations.

Mitigation: Keep the master password out of logs and shell history, prefer the encrypted secret store, and avoid privileged credentials until workflows are tested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/nutanix-aiops)
- [Project Homepage](https://github.com/AIops-tools/Nutanix-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call governed Nutanix CLI or MCP tools that return text, tables, task identifiers, or JSON-like operational results.]

## Skill Version(s):

0.11.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
