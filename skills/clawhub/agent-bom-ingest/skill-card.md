## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to validate canonical inventory JSON, run local agent-bom scans, and prepare findings, graphs, policy results, provenance, or auditor-ready reports without providing cloud credentials to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory reports may contain sensitive details.

Mitigation: Review exports before sharing and choose report paths deliberately.

Risk: An optional control-plane upload sends inventory to a remote service.

Mitigation: Enable uploads only for a service and destination explicitly chosen by the operator.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, SARIF, HTML, Markdown]

**Output Format:** [Markdown instructions and shell commands; agent-bom reports can be exported as JSON, SARIF, HTML, or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.11+ and agent-bom 0.84.4+. Optional vulnerability lookups and control-plane uploads use disclosed network endpoints; uploads require an operator-configured destination and token.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
