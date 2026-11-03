## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to validate operator-generated inventory JSON, analyze it locally with agent-bom, and produce findings, graphs, policy results, provenance details, or auditor-ready exports. It is intended for workflows where cloud inventory is collected separately and no direct cloud credentials are given to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional advisory queries may disclose package identities to OSV or GitHub Advisory services.

Mitigation: Review the inventory and disable optional advisory lookups when sharing package identities is not acceptable.

Risk: Pushing an inventory can disclose its contents to an external control plane, and the CLI's schema enforcement and redaction behavior were not included in the reviewed artifact.

Mitigation: Use a trusted agent-bom installation, validate the inventory, and push only to a destination and with an authentication method the operator explicitly approves; inspect exports before sharing them.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, JSON, SARIF, HTML, Markdown, SBOMs]

**Output Format:** [Markdown guidance and shell commands; scan findings and exports in JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires canonical inventory JSON and agent-bom; output files are written to operator-selected paths.]

## Skill Version(s):

0.113.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
