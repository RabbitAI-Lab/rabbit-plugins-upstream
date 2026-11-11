## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud engineers use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and other agent-related GCP resources in canonical agent-bom JSON. It defaults to discovery only; scanning is optional and runs only when the operator requests findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses existing operator GCP credentials for authenticated resource discovery, and scan evidence notes that a referenced local Python file was unavailable.

Mitigation: Use only operator-approved projects with read-only or short-lived credentials, never paste or print credential values, and review the referenced adapter and complete source package before running the workflow.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, Shell commands]

**Output Format:** [Canonical JSON inventory files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery-only by default; scanning is optional and requires an operator request.]

## Skill Version(s):

0.114.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
