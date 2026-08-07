## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and optionally scan that inventory without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agentic Azure infrastructure as schema-valid agent-bom inventory for local review and optional scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inventories Azure resources using the operator's Azure identity.

Mitigation: Use a least-privilege read-only identity scoped to approved subscriptions and do not use credentials that can modify Azure resources.

Risk: Generated inventory can contain sensitive resource metadata.

Mitigation: Write inventory only to an operator-selected path, review the JSON before sharing, and rely on redaction for credential-like values.

Risk: The workflow depends on an external agent-bom adapter or package.

Mitigation: Verify the external agent-bom repository or PyPI package before running its adapter script.

## Reference(s):

- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes operator-selected inventory JSON and optional scan findings JSON.]

## Skill Version(s):

0.99.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
