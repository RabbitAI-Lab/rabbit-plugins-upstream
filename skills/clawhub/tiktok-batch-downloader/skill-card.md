## Description:

This skill lets agents search TikTok by keyword, fetch public creator posts, retrieve video comments, and return structured JSON for content research, competitor monitoring, influencer analysis, and trend discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public TikTok search, creator-post, and comment data through command-line tools, then analyze the returned JSON for content planning, market research, social listening, and influencer screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API token and TikTok search terms, target URLs, or IDs to www.guaikei.com.

Mitigation: Use it only when that data sharing is acceptable, keep GUAIKEI_API_TOKEN in the environment, and avoid submitting sensitive targets or keywords.

Risk: Temporary JSON logs can contain returned TikTok content, comments, and user identifiers on shared machines.

Mitigation: Review and delete temporary logs when needed, and avoid retaining public personal data longer than the use case requires.

Risk: Returned TikTok comments and profile identifiers are public personal data that may carry consent, retention, or terms-of-service obligations.

Mitigation: Minimize, anonymize, or aggregate data before external sharing or commercial reuse, and confirm applicable platform and privacy requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-batch-downloader)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Guaikei API and token service](https://www.guaikei.com)
- [Complete parameter reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Creator posts request schema](assets/post_cli_req.schema.json)
- [Creator posts response schema](assets/post_cli_resp.schema.json)
- [Comments request schema](assets/comment_cli_req.schema.json)
- [Comments response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Text, Markdown, Guidance, Configuration]

**Output Format:** [Structured JSON from command stdout with text or Markdown analysis guidance for the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; command logs may be written under the system temporary directory.]

## Skill Version(s):

1.0.0 (source: server release, SKILL.md frontmatter, package.json, changelog released 2026-09-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
