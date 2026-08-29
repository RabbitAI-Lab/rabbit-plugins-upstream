## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Kuaishou China creator, video, comment, search, hashtag, live, and leaderboard data through the Scavio API while planning per-endpoint credit costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou identifiers, URLs, keywords, and pagination requests are sent to Scavio.

Mitigation: Confirm the user is comfortable sharing those inputs with Scavio before making API requests.

Risk: Endpoint costs vary from 1 to 40 credits and multi-page search can increase spend quickly.

Mitigation: Quote the relevant per-endpoint and per-page costs before calling expensive or repeated endpoints, and monitor credits used.

Risk: Incorrect Kuaishou versus Kwai inputs can produce empty or misleading results.

Mitigation: Confirm inputs are for Kuaishou China domains before spending credits, and do not treat Kwai international identifiers as supported.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/kuaishou-scraper-api)
- [Scavio Kuaishou Profile Documentation](https://scavio.dev/docs/kuaishou-profile)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [Scavio Kuaishou User Posts Documentation](https://scavio.dev/docs/kuaishou-user-posts)
- [Scavio Kuaishou User Resolve Documentation](https://scavio.dev/docs/kuaishou-user-resolve)
- [Scavio Kuaishou Video Documentation](https://scavio.dev/docs/kuaishou-video)
- [Scavio Kuaishou Video Comments Documentation](https://scavio.dev/docs/kuaishou-video-comments)
- [Scavio Kuaishou Search Documentation](https://scavio.dev/docs/kuaishou-search)
- [Scavio Kuaishou Trending Documentation](https://scavio.dev/docs/kuaishou-trending)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Code, Configuration]

**Output Format:** [Markdown with JSON and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides authenticated POST requests that return structured JSON envelopes with credit usage and pagination cursors where applicable.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
