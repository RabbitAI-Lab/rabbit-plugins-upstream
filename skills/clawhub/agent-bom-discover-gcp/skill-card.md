## Description:

Discover GCP-hosted AI agent and MCP-relevant assets, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud engineers use this skill to inventory approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and agentic infrastructure, then optionally scan the resulting canonical inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced GCP adapter is absent from this package, so its credential-redaction behavior is unverified; inventory may contain sensitive resource details.

Mitigation: Obtain and review the adapter from a trusted release, use project-scoped read-only credentials and a private output location, and review inventory before sharing.

## Reference(s):

- [Project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON; optionally JSON scan findings and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; discovery-only by default, with scanning only when requested.]

## Skill Version(s):

0.110.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
