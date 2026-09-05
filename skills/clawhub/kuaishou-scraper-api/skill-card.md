## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to retrieve public Kuaishou China creator, video, comment, search, hashtag, live, and leaderboard data through Scavio's paid API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and identifiers are sent to Scavio as a third-party API provider.

Mitigation: Avoid sending sensitive private notes or confidential research terms as API inputs.

Risk: Some API calls consume 10 or 40 credits, and paginated search pages can multiply costs.

Mitigation: Quote endpoint costs before calls, monitor credits_used in responses, and stop pagination when next_cursor is null.

Risk: The skill requires a Scavio API key.

Mitigation: Keep SCAVIO_API_KEY in the environment or a secret store and do not embed it in source files.

Risk: Kwai international links are outside this API's scope and may return empty results.

Mitigation: Confirm inputs are for Kuaishou China on kuaishou.com or v.kuaishou.com before spending credits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/kuaishou-scraper-api)
- [Kuaishou profile API documentation](https://scavio.dev/docs/kuaishou-profile?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python examples, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use the envelope {data, response_time, credits_used, credits_remaining}.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
