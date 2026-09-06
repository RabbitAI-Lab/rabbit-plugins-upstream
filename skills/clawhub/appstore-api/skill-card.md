## Description:

Read-only access to public App Store application data through ReplyNodes for app lookup by track or bundle ID, bounded search, and related-app listings, with Bearer workspace-key or x402 v2 gateway access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to retrieve normalized public App Store records, run bounded app searches, and list related apps without write, purchase, review, account, or login capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace installation may require bypassing an untrusted-source warning while package verification is inconsistent.

Mitigation: Install only locally reviewed files or wait for verified ClawHub publication; avoid --force unless the publisher and exact package bytes are independently trusted.

Risk: ReplyNodes workspace keys could be exposed if pasted into prompts, repositories, logs, screenshots, or client-side code.

Mitigation: Keep workspace keys in a secret store and pass them only through configured Bearer authentication.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/replynodes-ai/skills/appstore-api)
- [OpenAPI 3.1 App Store Public Reads Spec](artifact/references/appstore-public-v1.openapi.json)
- [MCP Tool Schema](artifact/references/appstore-mcp.schema.json)
- [Endpoint Examples](artifact/references/endpoints.md)
- [Install Guide](artifact/INSTALL.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET operations; search returns one bounded page with a documented maximum limit of 50.]

## Skill Version(s):

1.1.12 (source: server release evidence; artifact metadata also reports 1.1.10 and 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
