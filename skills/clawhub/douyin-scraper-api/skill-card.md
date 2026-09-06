## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags. 27 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve structured Douyin data through Scavio endpoints for social research, creator analysis, trend spotting, and application workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin URLs, user identifiers, search terms, and the Scavio API key are sent to Scavio when the skill is used.

Mitigation: Confirm the user is comfortable sharing that data with Scavio, keep the API key in environment or secret storage, and avoid sensitive person-level investigations.

Risk: Search endpoints cost more credits than other endpoints and can consume balance quickly in repeated runs.

Mitigation: Check credits_used and credits_remaining on responses, avoid tight search loops, and prefer targeted endpoint calls when identifiers are already known.

Risk: Trending, hot-search, feed, profile, and comment data can change over time.

Mitigation: Treat results as point-in-time API responses, re-fetch fresh data when recency matters, and do not fabricate counts, comments, follower numbers, or user details.

## Reference(s):

- [Scavio Douyin API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/douyin-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and curl examples; Scavio API calls return JSON envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search endpoints consume 10 credits and other Douyin endpoints consume 1 credit.]

## Skill Version(s):

1.0.2 (source: release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
