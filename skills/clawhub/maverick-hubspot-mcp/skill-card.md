## Description: <br>
Search and read HubSpot CRM contacts, companies, deals, tickets, associations, owners, pipelines, campaigns, and conversations via HubSpot's hosted MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maverick](https://clawhub.ai/user/maverick) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external operators, and developers use this skill to search and retrieve read-only HubSpot CRM, pipeline, owner, campaign, conversation, and customer context through a reviewed MCP tool allowlist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected HubSpot OAuth grant can expose account data through read-only tool calls. <br>
Mitigation: Install only when the user is comfortable granting read access to the connected HubSpot account, and keep requests scoped to relevant CRM data. <br>
Risk: OAuth credentials are sensitive and are written into the local mcporter vault during setup. <br>
Mitigation: Treat the refresh token, access token, client ID, and client secret as secrets, and avoid logging or sharing their values. <br>
Risk: Rerunning setup with stale OAuth values can overwrite a newer vault entry and break the integration. <br>
Mitigation: Rerun setup only with freshly minted OAuth credentials or after intentional credential rotation. <br>
Risk: Tool arguments and results transit HubSpot's hosted MCP server. <br>
Mitigation: Do not include unrelated sensitive content in HubSpot tool arguments. <br>


## Reference(s): <br>
- [HubSpot MCP server overview and endpoint](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server) <br>
- [HubSpot MCP auth app and required OAuth credentials](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server#create-an-mcp-auth-app) <br>
- [HubSpot OAuth token revocation](https://developers.hubspot.com/docs/api-reference/latest/authentication/oauth-tokens/revoke-token) <br>
- [mcporter config reference](https://github.com/openclaw/mcporter/blob/v0.12.3/docs/config.md) <br>
- [ClawHub skill page](https://clawhub.ai/maverick/skills/maverick-hubspot-mcp) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/maverick) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runtime calls are limited to the reviewed read-only HubSpot MCP tool allowlist.] <br>

## Skill Version(s): <br>
1.0.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
