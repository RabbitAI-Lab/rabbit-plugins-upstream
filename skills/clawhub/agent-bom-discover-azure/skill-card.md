## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory Azure OpenAI and other Azure AI or workload resources using an operator-approved, read-only Azure identity. They can save canonical inventory JSON for local scanning when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately supplied Azure discovery script is not bundled here, so its behavior could not be checked from this artifact.

Mitigation: Verify the discovery script before running it and use a read-only identity limited to the intended subscription.

Risk: Azure inventory may contain sensitive resource details that should not be shared broadly.

Mitigation: Choose a private output location and review the inventory for sensitive details before sharing it.

## Reference(s):

- [agent-bom project repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON files, Analysis, Guidance, Shell commands]

**Output Format:** [Canonical inventory JSON and, when requested, JSON scan findings; Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and performed only when requested.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
