## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform or security engineers use this skill to validate operator-generated inventory JSON, run local scans, and produce graph, policy, provenance, or auditor-ready exports without supplying direct cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory files and exports may contain sensitive infrastructure details.

Mitigation: Protect inventory files and exports, and review them before sharing.

Risk: Optional vulnerability lookups may disclose package identifiers to advisory services.

Mitigation: Confirm network settings before enabling advisory queries.

Risk: An optional control-plane push sends inventory to the configured destination.

Mitigation: Upload only to an explicitly selected control plane and configure its URL and authentication deliberately.

Risk: The external agent-bom executable's validation and redaction guarantees were not verified in this review.

Mitigation: Use a trusted release and protect inventory files and exports.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; JSON, SARIF, HTML, or Markdown inventory exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts schema-conforming inventory JSON; output format and destination are operator-selected.]

## Skill Version(s):

0.113.2 (source: artifact frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
