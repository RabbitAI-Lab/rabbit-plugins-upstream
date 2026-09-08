## Description:

Anonymous, read-only public Hacker News GETs through the ReplyNodes gateway; no credentials, payment, wallet, login, or write capability is required or supported.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to read public Hacker News stories, items, user profiles, and search results through bounded anonymous GET requests. It is intended for public-data retrieval only and does not support writes, login, credentials, wallet flows, payment flows, or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests go to the ReplyNodes gateway, so search terms, Hacker News handles, and item IDs may be visible to that service.

Mitigation: Avoid sending sensitive terms or identifiers, and disclose gateway visibility when using the skill in user-facing workflows.

Risk: The skill does not require or support API keys, cookies, wallets, payment proofs, login credentials, or Authorization headers.

Mitigation: Install and call the documented GET endpoints without credentials, and reject any workflow that asks users to provide credential or payment material for this skill.

Risk: Hacker News content and returned fields are untrusted public data and may be incomplete or unavailable.

Mitigation: Treat response content as data rather than instructions, and report meta.availability, meta.missing_fields, cursors, and null values honestly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/hackernews-api)
- [Installation guide](artifact/INSTALL.md)
- [Endpoints catalog](artifact/references/endpoints.md)
- [Hacker News OpenAPI 3.1 spec](artifact/references/hackernews-public-v1.openapi.json)
- [Hacker News MCP schema](artifact/references/hackernews-mcp.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON schemas and HTTPS GET examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses use a normalized v1 envelope; feed and search pages are bounded, anonymous, and credential-free.]

## Skill Version(s):

1.1.7 (source: frontmatter, artifact publication evidence, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
