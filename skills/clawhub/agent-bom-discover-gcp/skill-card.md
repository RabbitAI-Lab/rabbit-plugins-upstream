## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security teams use this skill to inventory AI and workload resources in operator-approved GCP projects, create canonical agent-bom inventory JSON, and optionally scan that inventory locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The inventory adapter is not bundled, so this release's review cannot confirm its redaction or runtime behavior.

Mitigation: Obtain and review the adapter from a trusted, versioned source before running it.

Risk: The resulting inventory contains details about cloud assets.

Mitigation: Use project-scoped read-only credentials, write only to an operator-selected path, and protect the inventory.

## Reference(s):

- [agent-bom repository (skill metadata homepage)](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON files, Shell commands, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON and optional findings JSON; Markdown instructions with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning is optional and performed only when requested.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
