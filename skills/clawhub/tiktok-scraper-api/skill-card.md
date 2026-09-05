## Description:

Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph through Scavio's external API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve structured TikTok profile, video, hashtag, comment, follower, and following data for social media research, trend analysis, influencer review, and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok handles, video IDs, search keywords, and Scavio API authentication to Scavio's external API.

Mitigation: Use it only when those inputs may be shared with Scavio, and keep SCAVIO_API_KEY in an environment variable or secret store outside source control.

Risk: Bulk pagination can consume credits quickly and collect more TikTok data than intended.

Mitigation: Confirm the requested scope before paginating, monitor credit usage, and keep collection aligned with applicable platform rules and privacy expectations.

## Reference(s):

- [Scavio TikTok API documentation](https://scavio.dev/docs/tiktok-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-scraper-api)
- [Scavio TikTok skill on ClawHub](https://clawhub.ai/scavio-ai/skills/tiktok-scraper-api)
- [Scavio publisher profile on ClawHub](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, JSON]

**Output Format:** [Markdown guidance with shell setup, Python examples, API endpoint details, and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints described by the skill cost 1 credit per request.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
