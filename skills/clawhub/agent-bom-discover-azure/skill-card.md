## Description:

Discovers Azure-hosted AI and agent-related assets using the operator's read-only credentials and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory Azure AI and workload resources in approved subscriptions, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure inventory may expose sensitive resource metadata if shared.

Mitigation: Review generated inventory before sharing it and save it only to an operator-selected path.

Risk: Azure credentials may grant access beyond the intended inventory scope.

Mitigation: Use a least-privilege read-only identity for approved subscriptions and avoid long-lived client secrets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON, optional JSON scan findings, and Markdown instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.108.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
