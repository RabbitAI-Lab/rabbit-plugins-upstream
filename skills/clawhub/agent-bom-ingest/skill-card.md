## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors. Use when a user has canonical inventory JSON and wants local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill when an operator has already produced canonical agent-bom inventory JSON. It guides validation, local scanning, and export of findings or audit materials without requiring direct cloud credentials for agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis was partial because a referenced local path was missing, so the benign verdict has medium confidence.

Mitigation: Review the release contents and treat the scan verdict as one input before installation.

Risk: Optional vulnerability lookups contact OSV and GitHub Advisory services, and optional control-plane push uses an operator-provided destination and API token.

Mitigation: Enable these connections only when appropriate for the environment; use an explicitly chosen push destination and never paste or print the API token.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [Project repository](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, SARIF, HTML, Markdown, CycloneDX/SPDX]

**Output Format:** [Markdown guidance with inline shell commands; agent-bom exports in the selected format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Export format and destination path are selected for the consumer.]

## Skill Version(s):

0.115.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
