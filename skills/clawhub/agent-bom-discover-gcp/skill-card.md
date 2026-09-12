## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related GCP infrastructure as canonical agent-bom inventory before optional local scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enumerate selected GCP projects using operator-controlled credentials.

Mitigation: Use read-only, scoped, preferably short-lived credentials and approve only the projects intended for inventory.

Risk: Generated inventory may contain sensitive infrastructure details even after credential-like values are redacted.

Mitigation: Review the inventory JSON before sharing it or pushing it to another system.

Risk: Supplying broad owner or administrator credentials could expose more GCP resources than intended.

Mitigation: Avoid broad owner/admin credentials and prefer least-privilege service accounts or workload identity.

## Reference(s):

- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected canonical inventory JSON and optional local agent-bom scan findings JSON.]

## Skill Version(s):

0.104.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
