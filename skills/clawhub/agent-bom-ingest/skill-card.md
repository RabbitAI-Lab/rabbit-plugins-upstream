## Description:

Validates operator-supplied agent-bom inventory and guides local scanning and auditor-ready exports without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and inventory operators use this skill to validate existing agent inventories, review local security findings, and prepare reports for auditors or automation without granting cloud access to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability lookups may send package or advisory lookup data to OSV or GitHub.

Mitigation: Review what may be shared before enabling external enrichment; keep scans local when external lookup is unnecessary.

Risk: Optional control-plane push can send inventory to an unintended destination or expose an API token.

Mitigation: Push only to an operator-approved URL with an operator-managed token; do not paste or print the token.

Risk: Malformed inventory or missing discovery trust fields may produce misleading findings.

Mitigation: Validate against the packaged schema and require the claimed discovery provenance and permissions before scanning.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local exports in JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX formats.]

## Skill Version(s):

0.107.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
