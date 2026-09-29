## Description:

Discovers Azure-hosted AI and agent-related assets, writes agent-bom inventory JSON, and optionally scans that inventory when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and operators use this skill to inventory AI and agent-related resources in approved Azure subscriptions and optionally scan the resulting inventory with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure discovery accesses subscription metadata through the operator's identity.

Mitigation: Use an approved, least-privilege read-only Azure identity and limit discovery to approved subscriptions.

Risk: Generated inventory may contain sensitive resource metadata.

Mitigation: Choose the local output path and review the inventory before sharing or scanning it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Shell commands and canonical inventory JSON; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes inventory to an operator-selected local path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.106.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
