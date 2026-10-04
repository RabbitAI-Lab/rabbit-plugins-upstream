## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets, writes canonical agent-bom inventory JSON, and optionally scans that inventory on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory AI and agent-related assets in approved Azure subscriptions. It writes inventory JSON to a chosen path and runs a local findings scan only when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses the operator's Azure identity to enumerate resources.

Mitigation: Use an approved subscription and read-only Azure role; avoid broad production credentials unless that scope is intended.

Risk: Generated inventory may contain sensitive resource information.

Mitigation: Review the inventory before sharing it and choose its output location deliberately.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON inventory]

**Output Format:** [Markdown instructions and commands; JSON inventory and optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discover-only by default; writes inventory to an operator-selected path and scans it only on request.]

## Skill Version(s):

0.108.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
