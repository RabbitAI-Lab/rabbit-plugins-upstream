## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related GCP agent infrastructure as canonical agent-bom JSON. It supports read-only discovery with optional local scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads local GCP credential configuration and uses authenticated Google APIs.

Mitigation: Use scoped read-only credentials, do not paste credential JSON into chat, and keep credential values out of generated inventory and logs.

Risk: Generated inventory can describe sensitive cloud assets and permissions.

Mitigation: Review generated inventory before sharing it outside the operator environment.

Risk: Discovery against unintended projects could expose more cloud metadata than planned.

Mitigation: Run discovery only for operator-approved GCP projects and write output only to an operator-selected path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected inventory JSON and optional local scan findings JSON.]

## Skill Version(s):

0.100.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
