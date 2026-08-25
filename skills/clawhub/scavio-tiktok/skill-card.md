## Description:

Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph (followers/followings). Eleven endpoints, all at 1 credit per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to retrieve structured TikTok profile, video, hashtag, comment, and follower/following data through Scavio endpoints for research, trend analysis, influencer analysis, and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries go through Scavio and consume credits, especially when paginating through many result pages.

Mitigation: Confirm large paginated lookups before running them and monitor credit usage.

Risk: The skill requires a Scavio API key.

Mitigation: Keep SCAVIO_API_KEY out of source control and store it through the user's normal secret-management flow.

Risk: The skill can retrieve TikTok comments and social graph data.

Mitigation: Use retrieved public data in line with applicable platform rules and privacy expectations.

## Reference(s):

- [Scavio TikTok API documentation](https://scavio.dev/docs/tiktok-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-tiktok)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON, API calls]

**Output Format:** [Markdown guidance with shell commands, Python examples, endpoint descriptions, and structured JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. TikTok calls go through Scavio and each endpoint request costs 1 credit; pagination can consume additional credits.]

## Skill Version(s):

1.0.7 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
