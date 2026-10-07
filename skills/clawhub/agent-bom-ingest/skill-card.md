## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and export of findings without direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to validate inventory supplied by operators or collectors, then generate local security findings and auditor-ready exports without granting direct cloud access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory and exported reports may reveal sensitive infrastructure details.

Mitigation: Keep scans local and write reports only to intended, access-controlled paths.

Risk: Optional advisory lookups or a control-plane push can transmit data externally.

Mitigation: Enable lookups deliberately; push only to an operator-provided destination and keep API tokens out of chat and reports.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides selection of JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX reports.]

## Skill Version(s):

0.108.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
