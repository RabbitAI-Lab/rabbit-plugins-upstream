## Description:

Pull Weibo user profiles and posts, post comments/likes/reposts, keyword search across posts, videos, users, topics and images, the hot-search board and ranking boards, and channel feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to retrieve structured Weibo data for China-market social listening, trend spotting, creator research, and topic research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Weibo identifiers, search terms, and the Scavio API key to Scavio's service.

Mitigation: Use the skill only for lawful, privacy-respecting research and keep SCAVIO_API_KEY in the environment or a secret store rather than source files.

Risk: Each API call may consume credits, including calls that return empty results.

Mitigation: Confirm the intended query and pagination before broad collection, and monitor credits and rate limits during use.

Risk: Weibo posts and comments can identify real people, and hot-search or ranking data is point-in-time.

Mitigation: Summarize social content carefully, avoid profiling individuals, and re-fetch time-sensitive boards before relying on them.

## Reference(s):

- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/weibo-scraper-api)
- [Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Weibo endpoints are described as costing 1 credit each.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
