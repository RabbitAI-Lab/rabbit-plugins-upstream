## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, cloud engineers, and security reviewers use this skill to inventory approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and agentic infrastructure. It produces canonical agent-bom inventory JSON and can optionally run a local agent-bom scan when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses operator-provided GCP credentials and may read local GCP configuration or credential files.

Mitigation: Use only approved read-only or scoped credentials, keep credentials in the operator environment, and do not paste service account JSON or tokens into chat.

Risk: Generated inventory can describe cloud resources and workload metadata even when credential-like values are redacted.

Mitigation: Choose the output path deliberately and review generated inventory before sharing it or using scan outputs.

Risk: Authenticated discovery could inventory unintended projects if environment defaults point at the wrong project.

Mitigation: Confirm the project and region before running discovery and limit execution to approved GCP projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; generated inventory and optional scan findings are JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path and expects credential-like values to be redacted before persistence or export.]

## Skill Version(s):

0.101.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
