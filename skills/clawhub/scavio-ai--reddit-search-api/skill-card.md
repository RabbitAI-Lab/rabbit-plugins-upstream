## Description:

Search Reddit posts, comments, and subreddits and retrieve posts, discussions, user activity, popular feeds, and trending queries through Scavio's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to find Reddit discussions, examine posts and comment threads, monitor mentions, and collect structured community data for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms, post IDs, subreddit names, and usernames are sent to Scavio with an API key.

Mitigation: Use the skill only when sharing those inputs with Scavio is acceptable, and keep the API key in a secret store or environment variable.

Risk: Returned Reddit posts, comments, and user activity may contain privacy-sensitive information.

Mitigation: Handle returned user and discussion data as privacy-sensitive and avoid unnecessary disclosure.

Risk: Each endpoint call consumes paid API credits.

Mitigation: Monitor credit usage and limit unnecessary requests or pagination.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/reddit-search-api)
- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)
- [Scavio API rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands, Guidance]

**Output Format:** [Structured JSON from the API; Markdown explanations and code examples when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated responses can include a next_cursor; API responses report credits used and remaining.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
