## Description:

Pull Weibo user profiles and posts, post comments/likes/reposts, keyword search across posts, videos, users, topics and images, the hot-search board and ranking boards, and channel feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to retrieve structured Weibo profiles, posts, comments, rankings, hot-search data, and keyword search results through Scavio's external API for social listening, trend monitoring, and creator or topic research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weibo IDs, post IDs, handles, and keyword searches are sent to Scavio's external API under the user's account.

Mitigation: Use the skill only when that disclosure is acceptable, and avoid sensitive investigative or personal search terms.

Risk: Each Weibo endpoint call costs one Scavio credit, including calls that return empty results.

Mitigation: Validate required identifiers before requests, paginate only with returned cursors, and retry rate-limited calls only after waiting.

Risk: The skill can retrieve posts and comments written by real people, which can support overbroad profiling if misused.

Mitigation: Summarize returned content and avoid building profiles of individuals beyond what the API response directly supports.

## Reference(s):

- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-weibo)

## Skill Output:

**Output Type(s):** [API Calls, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON-oriented API guidance and inline Python or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY; API responses are structured JSON envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
