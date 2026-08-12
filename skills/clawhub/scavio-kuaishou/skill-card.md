## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON. 14 endpoints priced per endpoint at 1, 2, 10 or 40 credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agent builders use this skill to retrieve public Kuaishou (China) creator, video, comment, search, hashtag, live, and leaderboard data through Scavio as structured JSON while planning per-endpoint credit spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for Kuaishou lookups.

Mitigation: Store SCAVIO_API_KEY as a private secret or environment variable and do not paste it into shared prompts, logs, or generated files.

Risk: Scavio acts as an intermediary for Kuaishou data requests.

Mitigation: Install and use the skill only when that intermediary role is acceptable for the intended workflow and data handling requirements.

Risk: Endpoint costs vary from 1 to 40 credits, and paginated search can multiply spend.

Mitigation: Quote the specific endpoint cost before requests, limit pagination intentionally, and inspect returned credits_used instead of assuming a flat platform cost.

Risk: Kwai international links are outside the documented API coverage.

Mitigation: Confirm the user is asking for Kuaishou China and use only kuaishou.com or v.kuaishou.com links before spending credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-kuaishou)
- [Scavio Kuaishou profile documentation](https://scavio.dev/docs/kuaishou-profile)
- [Scavio Kuaishou user posts documentation](https://scavio.dev/docs/kuaishou-user-posts)
- [Scavio Kuaishou video documentation](https://scavio.dev/docs/kuaishou-video)
- [Scavio Kuaishou search documentation](https://scavio.dev/docs/kuaishou-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell and Python examples for Scavio API calls that return structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; documented endpoint costs range from 1 to 40 credits per request.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
