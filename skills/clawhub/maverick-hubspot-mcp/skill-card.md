## Description:

Search and read HubSpot CRM contacts, companies, deals, tickets, associations, owners, pipelines, campaigns, and conversations via HubSpot's hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick](https://clawhub.ai/user/maverick)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and customer-facing teams use this skill to search and retrieve read-only HubSpot CRM, pipeline, owner, campaign, and customer context through HubSpot's hosted MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OAuth credentials that can read HubSpot CRM data through the connected account.

Mitigation: Treat the refresh token and client secret as sensitive, and revoke HubSpot app access when the integration is no longer needed.

Risk: Tool arguments and results transit HubSpot's hosted MCP server.

Mitigation: Avoid passing unrelated sensitive content as tool arguments and keep use scoped to HubSpot CRM lookup tasks.

Risk: Re-running setup with stale OAuth values can overwrite a newer in-vault refresh token.

Mitigation: Only rotate setup credentials with freshly minted OAuth values from the integration broker or require re-authorization if access is revoked.

## Reference(s):

- [HubSpot MCP server overview and endpoint](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server)
- [HubSpot MCP auth app and required OAuth credentials](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server#create-an-mcp-auth-app)
- [HubSpot OAuth token revocation](https://developers.hubspot.com/docs/api-reference/latest/authentication/oauth-tokens/revoke-token)
- [mcporter config reference](https://github.com/openclaw/mcporter/blob/v0.12.3/docs/config.md)
- [ClawHub skill page](https://clawhub.ai/maverick/skills/maverick-hubspot-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON tool output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HubSpot MCP results are limited by the reviewed tool allowlist and the connected HubSpot OAuth grant.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
