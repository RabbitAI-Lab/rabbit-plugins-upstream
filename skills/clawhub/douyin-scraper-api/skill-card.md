## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags. 27 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and analysts use this skill to retrieve structured Douyin video, creator, comment, hashtag, music, live-room, trending, and search data through Scavio. It is suited for lawful, user-directed China-market social research, creator analysis, and trend spotting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin queries, URLs, identifiers, and requested data to Scavio using a Scavio API key.

Mitigation: Use it only for user-directed tasks, keep SCAVIO_API_KEY in a secret store or environment variable, and avoid submitting unnecessary personal identifiers.

Risk: API calls consume credits, and search endpoints cost more than other endpoints.

Mitigation: Check credits_used and credits_remaining in responses, avoid tight search loops, and prefer targeted resolve or detail endpoints when possible.

Risk: Public comments and profiles can expose information about real people.

Mitigation: Summarize results and avoid building invasive individual profiles from comments, follower lists, or profile data.

Risk: Trending, ranking, feed, and engagement metrics are point-in-time data and may become stale.

Mitigation: Re-fetch current boards or metrics before making time-sensitive claims and report only values returned by the API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/douyin-scraper-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline Python or bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search endpoints consume more credits than other Douyin endpoints.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
