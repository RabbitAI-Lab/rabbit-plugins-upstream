## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials. Use when a user asks to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, or agentic Azure infrastructure as canonical inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud engineers use this skill to discover Azure AI and workload assets as canonical agent-bom inventory, then scan that inventory when requested. It is designed for operator-controlled, read-only Azure access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure inventory files may contain sensitive infrastructure information.

Mitigation: Protect inventory files and store them only at an operator-selected path.

Risk: Azure discovery relies on the permissions of the configured identity.

Mitigation: Use an identity restricted to read-only access in the intended, operator-approved subscription.

Risk: The separately installed agent-bom package or adapter is outside this skill artifact.

Mitigation: Verify the package and adapter before running the workflow.

## Reference(s):

- [agent-bom project repository (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI (listed in skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON with Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected file path; credential-like values are redacted.]

## Skill Version(s):

0.110.0 (source: skill frontmatter; release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
