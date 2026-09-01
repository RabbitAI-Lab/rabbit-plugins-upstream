## Description:

Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph (followers/followings). Eleven endpoints, all at 1 credit per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to retrieve structured TikTok profile, video, comment, hashtag, and social graph data through Scavio API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send TikTok identifiers, search terms, and related lookup details to Scavio.

Mitigation: Use the skill only where the planned data collection is permitted by applicable platform terms, law, and privacy expectations.

Risk: API calls consume Scavio credits and paginated workflows can increase usage.

Mitigation: Set query bounds before broad collection and warn users before paging through many result sets.

Risk: The skill requires SCAVIO_API_KEY for authenticated requests.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source control.

## Reference(s):

- [Scavio TikTok API documentation](https://scavio.dev/docs/tiktok-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tiktok-scraper-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown with API endpoint tables and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio TikTok API endpoints that return structured JSON.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
