## Description:

Query and manage EVE Online characters via the ESI (EVE Swagger Interface) REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[burnshall-ui](https://clawhub.ai/user/burnshall-ui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to authenticate with EVE SSO, query EVE ESI endpoints, and generate character, wallet, asset, market, planetary interaction, route, and threat reports for EVE Online account management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granted EVE SSO scopes can expose private account data such as wallet, assets, skills, mail, location, contracts, and killmails.

Mitigation: Grant the smallest practical scope set for the task and install only when that account-data access is acceptable.

Risk: Bearer tokens can leak if pasted into configs, chats, shell history, logs, or command-line arguments.

Mitigation: Use the default local token store and the esi_query.py --char flow where possible; use --token-stdin if an external token must be supplied.

Risk: The --allow-write option can permit state-changing ESI requests when the token has matching write scopes.

Mitigation: Keep the default read-only behavior for normal use and require explicit user review before any --allow-write request.

Risk: Configured Telegram or Discord alerts send the selected alert text to third-party services.

Mitigation: Avoid including raw wallet figures, asset inventories, tokens, or other sensitive account data in alert templates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/burnshall-ui/skills/eve-esi)
- [EVE SSO OAuth2 Authentication](references/authentication.md)
- [EVE ESI Character Endpoints Reference](references/endpoints.md)
- [Dashboard configuration schema](config/schema.json)
- [EVE ESI API Explorer](https://developers.eveonline.com/api-explorer)
- [EVE ESI Swagger specification](https://esi.evetech.net/latest/swagger.json)
- [EVE Developer Portal](https://developers.eveonline.com/applications)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; state-changing ESI requests require an explicit --allow-write option.]

## Skill Version(s):

1.3.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
