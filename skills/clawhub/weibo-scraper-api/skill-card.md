## Description:

Pull Weibo user profiles and posts, post comments/likes/reposts, keyword search across posts, videos, users, topics and images, the hot-search board and ranking boards, and channel feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and analysts use this skill to retrieve structured Weibo data through Scavio for China-market social listening, trend spotting, creator research, and topic analysis. It supports user, post, search, hot-search, ranking, and channel-feed workflows when a valid SCAVIO_API_KEY is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access privacy-relevant social data from Weibo.

Mitigation: Use it only for lawful, policy-compliant research; minimize personal data collection; summarize posts and comments; and avoid profiling or monitoring individuals.

Risk: SCAVIO_API_KEY authorizes paid API calls and consumes credits.

Mitigation: Store the key in a secret manager or environment variable, avoid committing it to source control, and monitor credit usage before high-volume workflows.

Risk: Hot-search and ranking results are point-in-time snapshots.

Mitigation: Re-fetch those endpoints when current trend state matters, and label time-sensitive findings as based on the returned API response.

## Reference(s):

- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/weibo-scraper-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and curl examples for JSON API requests and responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use a JSON envelope with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
