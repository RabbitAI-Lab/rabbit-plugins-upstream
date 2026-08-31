## Description:

Read-only, normalized public-data reads of App Store applications through ReplyNodes: app lookup by track ID or bundle ID, bounded search, and related-app listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to look up, search, and retrieve related public Apple App Store application metadata through ReplyNodes read-only tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated gateway requests use a ReplyNodes workspace API key.

Mitigation: Install only if ReplyNodes is trusted for public App Store read requests, keep the key in a secret store, and send it only through the Authorization header.

Risk: Agents may attempt unsupported App Store operations such as purchases, reviews, account actions, or writes.

Mitigation: Expose only appstore_get_app, appstore_search_apps, and appstore_get_similar_apps; treat every other App Store capability as out of scope.

Risk: Public App Store data may omit fields, and upstream services may return rate limits or transient errors.

Mitigation: Surface null values, meta.availability, missing_fields, Retry-After, and normalized error codes without fabricating missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/replynodes-appstore)
- [Endpoint examples](artifact/references/endpoints.md)
- [OpenAPI schema](artifact/references/appstore-public-v1.openapi.json)
- [MCP tool schema](artifact/references/appstore-mcp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP examples, JSON schemas, and normalized JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET operations; search returns one bounded page with a default limit of 20 and a maximum of 50.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
