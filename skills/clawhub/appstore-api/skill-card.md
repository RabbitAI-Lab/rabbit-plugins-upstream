## Description:

Provides read-only App Store public metadata lookup, search, and related-app discovery through the ReplyNodes gateway with bounded JSON responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and external agents use this skill to retrieve normalized public App Store app records by track ID or bundle ID, search public apps, and list related apps while preserving null and missing-field semantics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are routed through the ReplyNodes remote gateway for public App Store reads.

Mitigation: Install only when that gateway is acceptable for the workspace and verify the configured HTTPS base URL before use.

Risk: Bearer workspace keys or x402 payer configuration may be mishandled by an integrating agent or user.

Mitigation: Store workspace keys and payer settings in a secret store, never commit or print them, and use x402 only with a payer intentionally configured for this skill.

Risk: Agents may request unsupported or mutable App Store actions such as reviews, purchases, accounts, or write operations.

Mitigation: Expose only the three documented read-only GET operations and refuse unsupported capabilities instead of approximating them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/appstore-api)
- [Endpoint examples](references/endpoints.md)
- [OpenAPI specification](references/appstore-public-v1.openapi.json)
- [MCP tool manifest](references/appstore-mcp.schema.json)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Configuration instructions, Guidance]

**Output Format:** [JSON API responses with Markdown installation and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET operations return normalized v1 response envelopes; search results are bounded to one page with no continuation tokens.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
