## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags. 27 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agents use this skill to retrieve structured Douyin data for videos, creators, comments, hashtags, music, live rooms, trending boards, and keyword search through Scavio API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls consume Scavio credits, and search endpoints cost more than other Douyin endpoints.

Mitigation: Check credits_used on responses, avoid search loops, and prefer specific 1-credit endpoints when the needed identifier is already known.

Risk: The skill requires a Scavio API key.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and keep it out of source control and logs.

Risk: Responses may include public social-media data about real people.

Mitigation: Use the data only for appropriate Douyin research tasks, summarize comments and profiles, and avoid building individual profiles from returned data.

Risk: Trending, hot-search, feed, and ranking responses are point-in-time snapshots.

Mitigation: Re-fetch current boards when freshness matters and do not present stale counts or rankings as current.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/douyin-scraper-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, Python, curl, and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for authenticated POST requests to Scavio's Douyin API and for interpreting structured JSON responses.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
