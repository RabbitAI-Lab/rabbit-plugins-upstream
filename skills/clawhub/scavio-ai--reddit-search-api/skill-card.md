## Description:

Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external teams use this skill to retrieve Reddit posts, comments, subreddit data, user activity, popular feeds, and trending queries for discussion research, brand monitoring, sentiment analysis, and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms, post IDs, subreddit names, usernames, and similar request parameters are sent to Scavio using the configured API key.

Mitigation: Use the skill only when external service processing is acceptable, and avoid secrets, confidential investigation terms, or personal data in request parameters.

Risk: API requests consume Scavio credits.

Mitigation: Confirm the request is needed before execution and monitor credit balance or billing controls for high-volume workflows.

## Reference(s):

- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/reddit-search-api)

## Skill Output:

**Output Type(s):** [JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and Python or bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Reddit API calls consume Scavio credits and may take 5-15 seconds.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
