## Description:

Read-only App Store API for iOS app metadata and ASO research through ReplyNodes prepaid credits using one long-lived Bearer fetcher key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, ASO researchers, and agent builders use this skill to query public iOS App Store metadata, searches, related apps, reviews, ratings, privacy details, and developer listings through ReplyNodes read-only endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a ReplyNodes bearer key to the ReplyNodes gateway and consumes prepaid credits for successful public App Store queries.

Mitigation: Store the key only in an agent secret store, send it in the Authorization header, never paste it into chats or repositories, and monitor prepaid credit usage.

Risk: Security evidence notes inconsistent base-URL wording that may matter for environments with strict egress review.

Mitigation: Confirm the approved ReplyNodes gateway URL with the publisher before installation in restricted networks.

Risk: Public App Store source data may omit counters, prices, ratings, or other fields.

Mitigation: Preserve null values and report meta.availability and meta.missing_fields instead of fabricating missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/appstore-api)
- [ReplyNodes publisher profile](https://clawhub.ai/user/replynodes-ai)
- [Installation guide](artifact/INSTALL.md)
- [Endpoint examples](artifact/references/endpoints.md)
- [OpenAPI specification](artifact/references/appstore-public-v1.openapi.json)
- [MCP schema](artifact/references/appstore-mcp.schema.json)
- [ReplyNodes API gateway](https://api.replynodes.com)
- [ReplyNodes developer console](https://app.replynodes.com/developers)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses and Markdown setup guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [GET-only public App Store reads; requires a ReplyNodes Bearer key; responses use a normalized v1 envelope with explicit nulls for omitted values.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
