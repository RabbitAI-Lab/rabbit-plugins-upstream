## Description:

Discovers Azure-hosted AI and agent infrastructure, writes a sanitized agent-bom inventory, and optionally scans it for findings at the operator's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory agent-related Azure resources using an approved read-only identity. They can review the resulting inventory and request a local scan for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure discovery uses the operator's existing identity to access cloud resource metadata.

Mitigation: Approve the subscription and use a least-privilege, read-only Azure role.

Risk: Generated inventory can contain sensitive cloud resource metadata even after credential redaction.

Mitigation: Choose the output path yourself and review the inventory before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [Project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI (skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON inventory, JSON scan findings, Shell commands, Guidance]

**Output Format:** [JSON files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is sanitized; scanning is optional and requires an operator request.]

## Skill Version(s):

0.107.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
