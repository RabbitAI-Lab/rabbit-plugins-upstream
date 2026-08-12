## Description:

Google Docs Connector enables agents to create, edit, format, export, search, and share Google Docs through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to automate Google Docs workflows, including document creation, report generation, template creation, collaborative editing, formatting, export, and permission management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive document content may be exported or exposed through sharing actions.

Mitigation: Confirm the intended document, export format, recipients, roles, and permission type before using export or sharing actions.

Risk: Domain-wide or anyone-access sharing can broaden document access beyond the intended audience.

Mitigation: Require explicit confirmation before changing sharing permissions to domain-wide or anyone access.

Risk: OAuth, account, payment, or wallet secrets may be exposed if placed in prompts or logs.

Mitigation: Keep secrets out of prompts and logs, and use the setup skills or platform credential handling for account connection details.

Risk: Google Docs character indices can shift after edits, which can place later edits in the wrong location.

Mitigation: Refetch the document after edits and use the returned tab IDs and UTF-16 indices for subsequent updates.

## Reference(s):

- [Google Docs Connector marketplace page](https://www.agentpmt.com/marketplace/google-docs-connector)
- [Google Docs Connector ClawHub page](https://clawhub.ai/agentpmt/skills/google-docs-connector)
- [Google Docs Connector generated schema](artifact/schema.md)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote Google Docs actions return JSON success payloads; binary document exports may return base64 content.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
