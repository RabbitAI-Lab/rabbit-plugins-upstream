## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and exports without direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to validate inventory supplied by their own collectors, review local security findings, and prepare audit-ready exports without granting cloud credentials to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability lookups may send inventory metadata to OSV or GitHub Advisories.

Mitigation: Review the inventory and enable external lookups only when those destinations are acceptable.

Risk: Optional control-plane push may transmit inventory to an operator-provided destination and requires an API token.

Mitigation: Push only to a trusted, explicitly provided URL; keep tokens in environment variables, not chat or exported output.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local validation and scanning; suggests JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports according to the consumer.]

## Skill Version(s):

0.108.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
