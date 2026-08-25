## Description:

Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to query X content through Scavio for social search, profile lookup, conversation review, trend discovery, brand monitoring, and RAG or sentiment pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scavio acts as an intermediary for X lookups and the skill can retrieve public profile, follower, and post data.

Mitigation: Use the skill only when Scavio and X data processing fit the user's privacy and compliance requirements.

Risk: The skill requires a SCAVIO_API_KEY for API calls.

Mitigation: Keep the API key out of source control and load it from environment variables or secret storage.

Risk: Paginating large result sets consumes credits and may hit usage limits.

Mitigation: Inform the user before fetching many pages, monitor credit usage, and stop pagination when next_cursor is null.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/twitter-scraper-api)
- [Scavio X API documentation](https://scavio.dev/docs/x-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions, Python code examples, and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON from Scavio's X endpoints; paginated endpoints may consume one credit per page.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
