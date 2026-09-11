## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and social-listening teams use this skill to retrieve public Kuaishou China creator, video, comment, search, hashtag, live, and leaderboard data through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests go to Scavio using SCAVIO_API_KEY and may spend credits, especially search and batch endpoints.

Mitigation: Keep the key in an environment variable or secret store, confirm endpoint costs before use, limit pagination, and check credits_used in responses.

Risk: The API covers Kuaishou China only; using Kwai international links can return empty or unsuitable results.

Mitigation: Confirm that inputs are kuaishou.com or v.kuaishou.com URLs before making paid calls.

Risk: Returned public platform data can be time-sensitive, including live status and paginated search results.

Mitigation: Present live status and search results as snapshots and avoid fabricating counts, identifiers, comments, or rankings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/kuaishou-scraper-api)
- [Kuaishou Profile API Documentation](https://scavio.dev/docs/kuaishou-profile?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou User Posts API Documentation](https://scavio.dev/docs/kuaishou-user-posts?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou User Live API Documentation](https://scavio.dev/docs/kuaishou-user-live?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou User Resolve API Documentation](https://scavio.dev/docs/kuaishou-user-resolve?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Video API Documentation](https://scavio.dev/docs/kuaishou-video?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Video Comments API Documentation](https://scavio.dev/docs/kuaishou-video-comments?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Comment Replies API Documentation](https://scavio.dev/docs/kuaishou-comment-replies?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Videos Batch API Documentation](https://scavio.dev/docs/kuaishou-videos-batch?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Search API Documentation](https://scavio.dev/docs/kuaishou-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Video Search API Documentation](https://scavio.dev/docs/kuaishou-video-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou User Search API Documentation](https://scavio.dev/docs/kuaishou-user-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Live Search API Documentation](https://scavio.dev/docs/kuaishou-live-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Tag Feed API Documentation](https://scavio.dev/docs/kuaishou-tag-feed?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Kuaishou Trending API Documentation](https://scavio.dev/docs/kuaishou-trending?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=kuaishou-scraper-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell and Python examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Requests use Scavio credits, with endpoint costs from 1 to 40 credits.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
