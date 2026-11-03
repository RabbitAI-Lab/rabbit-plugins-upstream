## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials. Use when a user asks to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, or agentic Azure infrastructure as canonical inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to discover Azure AI and workload assets with an operator-controlled, read-only identity, then save them as canonical agent-bom inventory. They can request a separate scan of that inventory when they need findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow references an Azure discovery adapter that is absent from the reviewed package, so its credential handling, redaction, and network behavior were not reviewed.

Mitigation: Obtain and review the adapter from a trusted source before running it; scope the Azure identity to read-only access on intended subscriptions.

Risk: Generated inventory may contain sensitive infrastructure information.

Mitigation: Protect inventory files and write them only to an operator-selected location.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom source repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands]

**Output Format:** [Canonical JSON inventory files; shell commands are shown in Markdown code blocks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path. Scanning is optional and should occur only when requested.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
