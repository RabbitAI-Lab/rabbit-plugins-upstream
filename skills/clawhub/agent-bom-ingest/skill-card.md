## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and export of findings without direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security operators use this skill to validate inventory from their collectors, run local agent-bom scans, and prepare findings or auditor-ready exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability lookups may send inventory package details to external advisory services.

Mitigation: Confirm the operator accepts OSV or GitHub advisory lookups before enabling them.

Risk: Optional control-plane push can expose inventory or API tokens to an unintended destination.

Mitigation: Push only to an operator-provided, operator-owned URL; keep tokens in environment variables and out of chat.

## Reference(s):

- [agent-bom project documentation](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides operator-selected local JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports.]

## Skill Version(s):

0.108.2 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
