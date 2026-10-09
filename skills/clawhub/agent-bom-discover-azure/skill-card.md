## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets in approved subscriptions and writes canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI services and workloads in approved Azure subscriptions, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventorying subscriptions beyond the intended scope or with excessive permissions.

Mitigation: Limit discovery to operator-approved subscriptions and use a read-only Azure identity.

Risk: Azure inventory can contain sensitive resource metadata even when credentials are redacted.

Mitigation: Review the generated inventory before sharing it and keep output at an operator-selected path.

Risk: An unverified agent-bom installation could affect the safety of local discovery or scanning.

Mitigation: Verify the agent-bom package and source before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory files, JSON scan findings, Guidance]

**Output Format:** [Markdown instructions with shell commands; JSON inventory and optional scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.108.3 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
