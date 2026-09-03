## Description:

Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON for discussion research, brand monitoring, sentiment analysis, and RAG.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external agents use this skill to search Reddit, inspect posts and threaded comments, retrieve subreddit or user data, and collect structured public discussion data for research, monitoring, sentiment analysis, or RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit requests are processed by Scavio and require a Scavio API key.

Mitigation: Use the skill for public Reddit research, store SCAVIO_API_KEY as a secret, and avoid sensitive internal queries unless Scavio processing is acceptable.

Risk: API calls consume Scavio credits and can fail when the account balance is exhausted.

Mitigation: Monitor credit use, handle 402 billing responses, and confirm expected usage before high-volume workflows.

## Reference(s):

- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/reddit-search-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash and Python examples, plus structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Reddit requests are processed through Scavio, consume credits, and may take 5-15 seconds.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
