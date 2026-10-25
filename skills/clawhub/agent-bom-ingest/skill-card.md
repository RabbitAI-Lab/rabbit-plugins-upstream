## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to validate operator-generated agent-bom inventory JSON, review findings locally, and produce graph, policy, provenance, or auditor-ready exports without providing cloud credentials to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability lookups can disclose package identifiers to external services.

Mitigation: Enable OSV or GitHub Advisory lookups only when sharing package identifiers with those services is acceptable.

Risk: An optional inventory upload sends data to the configured control-plane destination.

Mitigation: Enable uploads only for an operator-controlled destination you trust, and provide any API token through the supported environment variable rather than chat.

## Reference(s):

- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OSV vulnerability API](https://api.osv.dev/v1)
- [GitHub Advisory API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, SARIF, HTML, Markdown]

**Output Format:** [Markdown guidance and shell commands for working with JSON inventory and generating local exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output format and destination are selected by the operator.]

## Skill Version(s):

0.110.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
