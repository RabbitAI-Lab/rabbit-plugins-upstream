## Description:

Apple App Store API for AI agents searches iOS apps by name, keyword, App Store ID, or bundle ID and retrieves public App Store metadata, ratings, reviews, developer details, privacy labels, similar apps, and competitors as structured JSON through the ReplyNodes API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, analysts, and agents use this skill to answer App Store search, ASO research, competitor research, ratings, reviews, publisher lookup, and public metadata questions without write access to Apple services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent needs a ReplyNodes API key and successful calls spend metered ReplyNodes credits.

Mitigation: Keep the key in a secret store, send it only to https://api.replynodes.com, and limit calls to task-related App Store lookups.

Risk: Localized App Store data may vary by storefront and language.

Mitigation: Use the user's requested country and language when available, and state the storefront used in analysis.

Risk: Some deployed routes were degraded or partial in the packaged live audit.

Mitigation: Report upstream failures, partial availability, empty chart results, or missing fields honestly instead of fabricating privacy labels, counters, rankings, or market-share estimates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/replynodes-ai/skills/appstore-api)
- [Operation Reference](references/endpoints.md)
- [Live Audit](references/live-audit.md)
- [OpenAPI 3.0.3 Specification](references/appstore-public-v1.openapi.json)
- [MCP Tool Schema](references/appstore-mcp.schema.json)
- [ReplyNodes API](https://api.replynodes.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with HTTPS GET examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public App Store lookups using a ReplyNodes Bearer API key; successful calls consume metered ReplyNodes credits.]

## Skill Version(s):

2.1.3 (source: artifact/SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
