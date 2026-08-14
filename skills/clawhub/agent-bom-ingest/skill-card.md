## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and auditors use this skill to validate canonical agent-bom inventory JSON, run local scans, and produce review or automation exports. It is intended for operator-provided inventory where provenance, permissions, and credential posture must remain explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory files may contain sensitive infrastructure and security details.

Mitigation: Validate inventory locally, choose output paths carefully, and share generated exports only with intended reviewers.

Risk: Optional control-plane push can expose data or tokens if sent to the wrong destination.

Mitigation: Push only to an operator-owned URL with an operator-provided token, and do not print or paste token values.

Risk: Malformed or incomplete inventory can produce misleading findings.

Mitigation: Stop when schema validation or required trust fields fail, and ask the operator to regenerate canonical inventory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OSV API](https://api.osv.dev/v1)
- [GitHub Advisory Database API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files, Configuration]

**Output Format:** [Markdown with shell commands and export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports JSON, SARIF, HTML, Markdown, CycloneDX, and SPDX exports through agent-bom.]

## Skill Version(s):

0.100.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
