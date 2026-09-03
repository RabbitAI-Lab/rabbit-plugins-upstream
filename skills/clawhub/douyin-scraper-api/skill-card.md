## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agents use this skill to query Scavio's Douyin API for videos, creators, comments, hashtags, music, live rooms, trends, and keyword search results for China-market social research and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Douyin URLs, account identifiers, video IDs, comment and search targets, and keywords to Scavio under the user's account.

Mitigation: Use the skill only for appropriate non-sensitive collection tasks, avoid sensitive profiling of individuals, and confirm third-party data transfer is acceptable for the use case.

Risk: Search endpoints cost 10 credits per call and repeated searches can consume account budget quickly.

Mitigation: Check credits_used and credits_remaining on responses, avoid tight search loops, and prefer targeted requests where possible.

Risk: The skill requires SCAVIO_API_KEY for authenticated API access.

Mitigation: Store SCAVIO_API_KEY in the runtime environment or a secrets manager and keep it out of source control and shared logs.

Risk: Trending, hot-search, rankings, comments, and profile data can change over time.

Mitigation: Treat returned data as point-in-time API output and re-fetch when freshness matters.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/douyin-scraper-api)
- [Scavio signup](https://dashboard.scavio.dev/sign-up?utm_source=clawhub&utm_medium=skill&utm_campaign=douyin-scraper-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, Configuration]

**Output Format:** [Markdown with JSON API response descriptions and inline Python or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
