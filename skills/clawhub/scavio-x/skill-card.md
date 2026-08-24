## Description:

Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external agents use this skill to retrieve structured X/Twitter search, tweet, profile, social graph, media, and trending-topic data through Scavio for monitoring, research, RAG, or sentiment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: X search terms, handles, tweet IDs, and related lookup requests are shared with Scavio.

Mitigation: Use only data appropriate for third-party processing and follow the user's privacy and data-handling requirements.

Risk: Paginating through many X results can consume Scavio API credits.

Mitigation: Tell the user before broad pagination and monitor returned credit usage fields.

Risk: Returned tweet, profile, follower, and trend data may change over time and should not be guessed.

Mitigation: Present API data as returned, surface engagement metrics as-is, and do not fabricate tweet IDs, handles, metrics, or replies.

## Reference(s):

- [Scavio X API documentation](https://scavio.dev/docs/x-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-x)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash and Python examples plus structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio X endpoints are read-only, paginated, and consume API credits.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
