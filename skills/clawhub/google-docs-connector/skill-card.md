## Description:

Enables agents to create, edit, format, export, and share Google Docs through AgentPMT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users automate Google Docs workflows, including drafting reports, formatting documents, managing collaboration, and exporting files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exporting a confidential document may disclose its contents.

Mitigation: Require explicit user approval before exporting confidential documents.

Risk: Broad sharing or writer permissions may expose or change a document.

Mitigation: Get explicit approval before sharing, prefer specific user emails and reader or commenter access, and review permissions.

Risk: Raw batch updates or replacements without a tab ID may alter unintended content.

Mitigation: Confirm the target document and tab, preview intended changes, and require approval for broad edits.

Risk: Credentials entered in prompts or logs may be exposed.

Mitigation: Keep AgentPMT and Google credentials out of prompts and logs.

## Reference(s):

- [Google Docs Connector schema](schema.md)
- [ClawHub skill release](https://clawhub.ai/agentpmt/skills/google-docs-connector)
- [AgentPMT Google Docs Connector marketplace listing](https://www.agentpmt.com/marketplace/google-docs-connector)
- [AgentPMT account setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Document content and JSON tool responses; exports support PDF, DOCX, HTML, and other formats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Binary exports may be returned as base64.]

## Skill Version(s):

1.0.2 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
