## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, engineers, and operators use this skill to validate canonical inventory JSON, run a local agent-bom scan, and produce graph, policy, provenance, or auditor-ready exports without providing direct cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because a referenced local path could not be matched to a bundled artifact.

Mitigation: Check that the expected path or file is present and review the inventory and resulting findings before relying on the scan.

Risk: Optional vulnerability lookups contact external services, and optional control-plane push sends data to an operator-provided endpoint.

Mitigation: Enable these options only when they fit your requirements; confirm the destination and authentication method before pushing inventory.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Guidance]

**Output Format:** [JSON, SARIF, HTML, and Markdown export files, with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The operator selects the export path and format.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
