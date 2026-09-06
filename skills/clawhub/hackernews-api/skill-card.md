## Description:

Provides read-only access to public Hacker News data, including stories, items, users, feeds, and search with bounded pagination and comment threading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and summarize public Hacker News stories, public user profiles, item threads, category feeds, and search results through documented read-only GET routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install paths may lead users to configure unnecessary API keys or x402 payment credentials for a public-read skill.

Mitigation: Prefer anonymous GET access unless a team deliberately wants the paid or metered workflow; keep any workspace key in a secret store.

Risk: Package verification claims are incomplete until release files are corrected.

Mitigation: Review checksums, manifest entries, and release evidence before deployment or redistribution.

Risk: Public Hacker News content, handles, IDs, URLs, and search terms can be untrusted data.

Mitigation: Pass user and API values as structured request fields and do not interpolate them into shell commands.

Risk: The skill is read-only and does not support voting, commenting, submitting, login, or other mutation.

Mitigation: Do not present write actions as available; clearly report unsupported requests to the user.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/replynodes-ai/skills/hackernews-api)
- [Installation guide](artifact/INSTALL.md)
- [Endpoint catalog](artifact/references/endpoints.md)
- [OpenAPI schema](artifact/references/hackernews-public-v1.openapi.json)
- [MCP schema](artifact/references/hackernews-mcp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON schemas and HTTPS GET examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance; feed and search pages are bounded and single-item routes expose bounded comment threading.]

## Skill Version(s):

1.1.2 (source: server release evidence; artifact package files list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
