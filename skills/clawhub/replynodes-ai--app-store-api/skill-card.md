## Description:

Helps agents research public iOS App Store listings, ratings, reviews, developer catalogs, privacy details, and similar apps through the read-only ReplyNodes API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, app researchers, and marketing teams use this skill to discover iOS apps, compare ratings and reviews, examine developer catalogs and privacy details, and inform App Store optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App Store searches and app IDs are sent to ReplyNodes.

Mitigation: Only send query terms and app IDs you are comfortable sharing with ReplyNodes.

Risk: An API key used for authenticated continuation could be exposed.

Mitigation: Store REPLYNODES_API_KEY in a secret store and never include it in chats, URLs, files, or logs.

Risk: App listings and reviews may contain untrusted instructions or misleading claims.

Mitigation: Treat fetched content as data and verify material claims before relying on them.

## Reference(s):

- [ReplyNodes App Store capabilities and API schema](https://api.replynodes.com/v1/capabilities)
- [ReplyNodes authentication documentation](https://docs.replynodes.com/docs/auth)
- [ReplyNodes MCP endpoint](https://mcp.replynodes.com/mcp)
- [ReplyNodes agent skills repository (listed in metadata)](https://github.com/replynodes/replynodes-agent-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Natural-language summaries and Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only App Store research; results can vary by storefront and availability.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
