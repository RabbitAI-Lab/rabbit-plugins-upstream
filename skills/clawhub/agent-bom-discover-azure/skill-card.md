## Description:

Discovers Azure-hosted AI and agent-related assets, writes canonical agent-bom inventory JSON, and optionally scans the inventory on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory approved Azure subscriptions and, when requested, scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory discovery accesses the operator's Azure identity and subscription metadata.

Mitigation: Use an existing read-only identity scoped to approved subscriptions; do not share secrets or tokens.

Risk: Inventory files or subsequent exports may disclose infrastructure details.

Mitigation: Review the output path and inventory before sharing it; run scans that push or export data only with explicit approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [Project homepage listed in skill metadata](https://github.com/msaad00/agent-bom)
- [agent-bom package listed in skill metadata](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON files, Guidance]

**Output Format:** [Markdown guidance and canonical inventory JSON; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scans only on request.]

## Skill Version(s):

0.108.2 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
