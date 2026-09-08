## Description:

Pull a Facebook page's profile, posts, reels and photos, one post with its comments, a single reel/video with downloadable URLs, a public group and its posts, an event, and hashtag posts. 11 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agents use this skill to retrieve structured public Facebook page, post, reel, group, event, comment, and hashtag data through Scavio for brand monitoring, competitor analysis, and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Facebook URLs, hashtag queries, and the Scavio API key to Scavio for public-data retrieval.

Mitigation: Install and run it only when that data sharing is intended, and keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Returned posts, comments, profiles, and contact fields can include privacy-sensitive information about real people.

Mitigation: Use it for lawful, authorized research, avoid profiling individuals, and minimize retention or redistribution of personal data.

Risk: The endpoints return current top posts and top visible comments rather than complete historical feeds or full comment threads.

Mitigation: Describe results as partial public snapshots and avoid making claims that require exhaustive Facebook coverage.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/facebook-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with API request examples, setup commands, and structured JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns Scavio Facebook API response envelopes containing data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
