## Description:

Researches Reddit via the Crawlora API -- subreddit posts/comments/about, a single post plus its comment thread, keyword search, user post/comment history, domain-linked posts, and hot/new/rising/top trends -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, analysts, and external agent users use this skill to gather public Reddit posts, comments, user activity, subreddit trends, and domain mentions for community research, sentiment review, thread summaries, and brand or competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms, subreddit names, domains, post IDs, public usernames, and the Crawlora API key are sent to Crawlora.

Mitigation: Avoid sensitive or confidential research terms and keep CRAWLORA_API_KEY in the environment rather than committing it to files.

Risk: Public Reddit engagement metrics and anonymous-page data can be approximate or incomplete.

Mitigation: Treat metrics as directional, disclose uncertainty in summaries, and avoid relying on a single metric as a definitive measurement.

## Reference(s):

- [reddit-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/reddit-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns public Reddit data through Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
