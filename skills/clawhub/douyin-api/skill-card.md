## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags. 27 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve structured Douyin data for user-directed video, creator, comment, trend, live-room, hashtag, music, and keyword-search workflows through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key and can spend API credits.

Mitigation: Store SCAVIO_API_KEY as a secret, confirm user intent before costly calls, check credits_used in responses, and avoid tight search loops.

Risk: Douyin profiles and comments are public content from real people.

Mitigation: Use the skill for user-directed lookups, summarize responsibly, and avoid building personal profiles of individuals.

Risk: Trending, hot-search, and ranking data are point-in-time snapshots.

Mitigation: Re-fetch current boards when freshness matters and label time-sensitive results as API-returned snapshots.

## Reference(s):

- [Scavio Douyin API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/douyin-api)
- [Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls, JSON]

**Output Format:** [Markdown with shell commands, code examples, and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns Scavio API responses in the envelope {data, response_time, credits_used, credits_remaining}.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
