## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and export without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to validate operator-generated agent inventories, scan them locally, and prepare findings or auditor-ready exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability enrichment can share package or advisory query data with OSV or GitHub.

Mitigation: Review the data-sharing implications before enabling network enrichment.

Risk: An optional control-plane push sends inventory to an operator-selected endpoint.

Mitigation: Enable push only after explicitly specifying and trusting the destination URL and authentication method; do not disclose tokens in chat or output.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [agent-bom ingest release](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports.]

## Skill Version(s):

0.106.1 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
