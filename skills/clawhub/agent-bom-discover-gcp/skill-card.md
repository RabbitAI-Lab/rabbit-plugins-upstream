## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials. Use when a user asks to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, or agentic GCP infrastructure as canonical inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory AI and workload resources in operator-approved GCP projects with read-only credentials. It writes canonical inventory JSON locally and supports an optional scan when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required GCP discovery adapter is not included, so this release does not establish its runtime behavior or credential redaction.

Mitigation: Obtain the adapter from a verified source and inspect it before execution, as advised by the security guidance.

Risk: The resulting cloud inventory may contain sensitive environment details.

Mitigation: Use operator-approved projects and read-only credentials, choose the output location, and protect the resulting inventory.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON and Markdown instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; credential-like values are described as redacted before persistence or export.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
