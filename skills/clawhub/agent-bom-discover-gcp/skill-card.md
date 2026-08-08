## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inventory approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and related agentic infrastructure. It produces canonical inventory that can be reviewed locally or scanned with agent-bom when findings are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inventory cloud resources from approved GCP projects and may expose environment details in generated inventory.

Mitigation: Use read-only or short-lived credentials, restrict discovery to operator-approved projects, and review generated inventory before sharing it outside the environment.

Risk: GCP credential material could be mishandled if copied into chat or written to unintended locations.

Mitigation: Keep credentials in the operator environment, do not paste private keys or tokens into chat, and confirm the inventory output path before running discovery.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom Project Homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON inventory output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected inventory JSON and optional local agent-bom scan findings when requested.]

## Skill Version(s):

0.99.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
