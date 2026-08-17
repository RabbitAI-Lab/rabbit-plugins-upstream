## Description:

Query EVE Online ESI for public and authenticated character data, manage local OAuth2/PKCE tokens, and run read-only PI, market, route, wallet, assets, skills, industry, mail, and related API lookups with explicit opt-in for state-changing calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[burnshall-ui](https://clawhub.ai/user/burnshall-ui)

### License/Terms of Use:

MIT-0

## Use Case:

External EVE Online players, developers, and agents use this skill to authenticate characters, query ESI data, inspect account and universe state, and validate dashboard configuration for alerts, reports, market tracking, planetary interaction, industry, route, and status workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth access and refresh tokens can expose private EVE account data if copied into shell history, logs, config files, CI output, or chat transcripts.

Mitigation: Use the local token store and --char flow, avoid manual token handling, use --token-stdin only when a token must be passed, and never paste tokens into configs or shared text.

Risk: Over-broad EVE SSO scopes can grant access to sensitive wallet, mail, asset, location, clone, implant, contract, and activity data.

Mitigation: Ask the user which scope profile or exact scopes to grant, prefer the narrowest profile that answers the task, and use public endpoints without authentication when possible.

Risk: Some ESI methods can change account state, including mail, fittings, contacts, market orders, or planetary interaction operations.

Mitigation: Rely on the skill's read-only default and require explicit user intent plus --allow-write before any state-changing request.

Risk: Telegram or Discord notifications can move configured alert text into third-party systems.

Mitigation: Send only the alert content the user has configured and avoid including raw wallet figures, asset inventories, mail, tokens, or other sensitive account data in outbound notifications.

## Reference(s):

- [Skill README](README.md)
- [EVE SSO OAuth2 Authentication](references/authentication.md)
- [EVE ESI Character Endpoints Reference](references/endpoints.md)
- [Dashboard Config Schema](config/schema.json)
- [Endpoint Presets](config/esi_endpoints.json)
- [EVE ESI API Explorer](https://developers.eveonline.com/api-explorer)
- [EVE Developer Portal](https://developers.eveonline.com/applications)
- [EVE ESI OpenAPI 3.1 Specification](https://esi.evetech.net/meta/openapi.json)
- [EVE ESI Compatibility Dates](https://esi.evetech.net/meta/compatibility-dates)
- [EVE ESI Changelog](https://esi.evetech.net/meta/changelog)
- [EVE SSO Authorization Server Metadata](https://login.eveonline.com/.well-known/oauth-authorization-server)
- [Revoke EVE Third-Party Access](https://community.eveonline.com/support/third-party/)
- [ClawHub Skill Page](https://clawhub.ai/burnshall-ui/skills/eve-esi)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API or configuration output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [ESI results may be paginated; state-changing non-GET calls require explicit --allow-write.]

## Skill Version(s):

1.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
