## Description:

Read DocuSign account, envelope, recipient, template, and signing-status data through DocuSign's official developer MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick](https://clawhub.ai/user/maverick)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect DocuSign accounts, envelopes, recipients, templates, and signing status through a hosted read-only MCP integration without changing DocuSign data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth access and refresh tokens are stored in mcporter's local vault and sent to DocuSign developer MCP/token endpoints over HTTPS.

Mitigation: Use a DocuSign developer or demo account intended for agent inspection, rotate or revoke credentials when access is no longer needed, and avoid production data unless separately approved.

Risk: The read-only tools can expose DocuSign account, envelope, recipient, template, and signing-status data to the agent session.

Mitigation: Limit the connected account and OAuth grant to data the agent is allowed to inspect, and avoid passing unrelated sensitive content through these tools.

Risk: Setup reseeds the local OAuth vault from environment-supplied credential values.

Mitigation: Run setup only when the supplied environment contains the freshest credential state so a rotated refresh token is not overwritten by stale values.

## Reference(s):

- [DocuSign MCP overview](https://developers.docusign.com/tools/mcp-server/)
- [DocuSign developer MCP endpoint](https://mcp-d.docusign.com/mcp)
- [mcporter MCP CLI](https://github.com/openclaw/mcporter)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only DocuSign MCP responses; limited to the six allowed tools in mcporter.json and requires OAuth credentials.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
