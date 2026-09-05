## Description:

Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured X data for search, profile lookup, conversation review, trend discovery, brand monitoring, sentiment workflows, and social-context pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send X search terms, handles, tweet IDs, country selections, and the Scavio API key to Scavio's service.

Mitigation: Use the skill only for workflows where sharing those request values with Scavio is appropriate, and keep SCAVIO_API_KEY in environment or secret storage.

Risk: Paginated social-graph pulls can consume credits and may raise privacy or policy considerations.

Mitigation: Limit pagination to the data needed for the task, inform users before large pulls, and review retrieved social-graph data before downstream use.

## Reference(s):

- [Scavio X API documentation](https://scavio.dev/docs/x-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitter-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitter-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/twitter-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response shapes, API request examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio X endpoints return structured JSON and may use pagination cursors.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
