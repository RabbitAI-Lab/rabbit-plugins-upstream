## Description:

App Store API gives agents read-only access to public App Store app data through app lookup, bounded search, and related-app listings via the ReplyNodes public-read service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent builders use this skill to let agents retrieve normalized public App Store records, search results, and related-app listings while preserving the documented read-only boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App Store lookup and search queries are sent to the ReplyNodes gateway.

Mitigation: Install only if this data flow is acceptable for the workspace, and avoid sending sensitive or unnecessary query terms.

Risk: A workspace API key may be exposed if pasted into prompts, logs, repositories, screenshots, or client-side code.

Mitigation: Store the key only in the agent's secret configuration and send it as a Bearer token at request time.

Risk: Agents may overstate the supported surface by attempting purchase, review, account, login, ranking, developer-catalog, review, rating, or suggestion workflows.

Mitigation: Expose only the three documented read-only operations and refuse unsupported capabilities instead of approximating them.

Risk: The installed artifact could differ from the reviewed package.

Mitigation: Verify the included checksum inventory with sha256sum before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/appstore-api)
- [OpenAPI specification](references/appstore-public-v1.openapi.json)
- [MCP schema](references/appstore-mcp.schema.json)
- [Endpoint examples](references/endpoints.md)
- [Installation guide](INSTALL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON schemas, HTTP examples, and read-only API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve null values for omitted public data, surface meta.availability, and avoid unsupported purchase, review, account, login, or mutation capabilities.]

## Skill Version(s):

1.1.14 (source: SKILL.md frontmatter, manifest.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
