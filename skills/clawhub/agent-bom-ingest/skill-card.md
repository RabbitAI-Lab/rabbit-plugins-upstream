## Description:

Validates operator-provided agent inventory JSON and guides local scanning and reporting without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to validate operator-provided agent inventories and generate local findings or audit-ready reports without supplying cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory JSON and exported reports may contain sensitive information.

Mitigation: Treat inventory and exports as sensitive and review them before sharing.

Risk: Optional control-plane push could disclose inventory to an untrusted destination.

Mitigation: Push only to an operator-owned URL the user trusts; provide API tokens through environment variables, not chat.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local exports in JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX.]

## Skill Version(s):

0.109.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
