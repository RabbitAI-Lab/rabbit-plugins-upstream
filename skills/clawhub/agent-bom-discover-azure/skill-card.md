## Description:

Discovers Azure-hosted AI and agent-related assets using an operator-approved identity and writes canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory Azure AI and workload assets under approved subscriptions, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure resource enumeration may cover more subscriptions or resources than intended.

Mitigation: Use a read-only Azure role and explicitly approve the subscription before discovery.

Risk: Generated inventory may disclose sensitive details if shared.

Mitigation: Choose the local output path deliberately and review the inventory before sharing it outside your environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom project (skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON inventory]

**Output Format:** [Markdown instructions and a local JSON inventory file; optional JSON scan findings on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory uses an operator-selected output path; credential-like values are redacted.]

## Skill Version(s):

0.108.4 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
