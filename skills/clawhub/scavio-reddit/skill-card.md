## Description:

Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and operations teams use this skill to retrieve public Reddit discussions, post details, comment threads, subreddit data, redditor activity, popular posts, and trending searches for discussion research, brand monitoring, sentiment analysis, and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends Reddit lookup inputs and API requests to Scavio and consumes Scavio credits.

Mitigation: Avoid sending secrets, private identifiers, or regulated data unless third-party processing is acceptable for the use case.

Risk: Reddit results are user-generated public data and may include NSFW content, attribution requirements, or misleading claims.

Mitigation: Surface source fields such as author, subreddit, score, timestamps, and NSFW flags, and verify important claims before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-reddit)
- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, API calls]

**Output Format:** [Markdown with JSON and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Scavio Reddit API requests and structured JSON responses.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
