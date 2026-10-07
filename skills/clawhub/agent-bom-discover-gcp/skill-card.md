## Description:

Discovers GCP-hosted AI agent and MCP-related assets in approved projects and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI agents and related workloads across approved GCP projects, then optionally scan the resulting inventory with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing GCP credentials may expose resources outside the intended inventory scope.

Mitigation: Use scoped, read-only credentials and inventory only operator-approved projects.

Risk: Generated inventory may contain sensitive cloud resource metadata.

Mitigation: Choose the output path yourself and review inventory before sharing it.

## Reference(s):

- [agent-bom project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package (skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory, Guidance]

**Output Format:** [Markdown guidance with shell commands; canonical JSON inventory when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; produces scan findings only on request.]

## Skill Version(s):

0.108.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
