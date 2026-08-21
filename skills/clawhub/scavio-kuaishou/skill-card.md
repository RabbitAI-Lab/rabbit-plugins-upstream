## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agent builders use this skill to plan Scavio API calls for public Kuaishou China creator, video, comment, search, hashtag, live-status, and leaderboard data while accounting for endpoint costs and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent through Scavio using SCAVIO_API_KEY and can consume paid credits, especially on search, profile, and batch endpoints.

Mitigation: Confirm the user is comfortable using Scavio for Kuaishou lookups, quote the endpoint cost before calls, and avoid unnecessary pagination or broad fan-out searches.

Risk: The skill covers Kuaishou China only; Kwai international links or identifiers are unsupported and may produce empty or failed results.

Mitigation: Check whether the user supplied kuaishou.com or v.kuaishou.com input before spending credits, and clarify the platform distinction when needed.

Risk: Public social-media data can be stale, incomplete, or rejected by the upstream platform, including live-status snapshots and paginated search results.

Mitigation: Report only returned data, preserve original Chinese text alongside translations when helpful, stop when next_cursor is null, and retry upstream failures conservatively.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-kuaishou)
- [Scavio Kuaishou profile documentation](https://scavio.dev/docs/kuaishou-profile)
- [Scavio Kuaishou user posts documentation](https://scavio.dev/docs/kuaishou-user-posts)
- [Scavio Kuaishou user live documentation](https://scavio.dev/docs/kuaishou-user-live)
- [Scavio Kuaishou user resolve documentation](https://scavio.dev/docs/kuaishou-user-resolve)
- [Scavio Kuaishou video documentation](https://scavio.dev/docs/kuaishou-video)
- [Scavio Kuaishou video comments documentation](https://scavio.dev/docs/kuaishou-video-comments)
- [Scavio Kuaishou comment replies documentation](https://scavio.dev/docs/kuaishou-comment-replies)
- [Scavio Kuaishou videos batch documentation](https://scavio.dev/docs/kuaishou-videos-batch)
- [Scavio Kuaishou search documentation](https://scavio.dev/docs/kuaishou-search)
- [Scavio Kuaishou video search documentation](https://scavio.dev/docs/kuaishou-video-search)
- [Scavio Kuaishou user search documentation](https://scavio.dev/docs/kuaishou-user-search)
- [Scavio Kuaishou live search documentation](https://scavio.dev/docs/kuaishou-live-search)
- [Scavio Kuaishou tag feed documentation](https://scavio.dev/docs/kuaishou-tag-feed)
- [Scavio Kuaishou trending documentation](https://scavio.dev/docs/kuaishou-trending)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with endpoint tables and code examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and includes endpoint-specific credit costs from 1 to 40 credits.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
