## Description:

Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill to search Reddit discussions, retrieve posts and comment threads, inspect subreddit or redditor activity, and collect structured discussion data for research, monitoring, sentiment analysis, and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit searches, post identifiers, URLs, subreddit names, usernames, and cursors are sent to Scavio's external service.

Mitigation: Avoid submitting sensitive research terms or identifiers unless the user is comfortable with Scavio processing them.

Risk: Requests consume Scavio API credits and may be rate limited.

Mitigation: Use pagination intentionally, account for the 1-credit-per-endpoint cost, and handle rate-limit responses before retrying.

Risk: Returned Reddit data may include NSFW content.

Mitigation: Preserve and surface the API's is_nsfw flag so downstream users or workflows can decide how to handle the content.

Risk: The integration requires a Scavio API key.

Mitigation: Load SCAVIO_API_KEY from an environment variable or secret store and avoid embedding it in source code or logs.

## Reference(s):

- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/reddit-search-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Code]

**Output Format:** [Markdown guidance with JSON response data and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY; API requests are external to Scavio and each Reddit endpoint costs 1 credit.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
