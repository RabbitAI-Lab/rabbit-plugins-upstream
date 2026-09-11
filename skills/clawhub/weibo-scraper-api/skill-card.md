## Description:

Pull Weibo user profiles and posts, post comments/likes/reposts, keyword search across posts, videos, users, topics and images, the hot-search board and ranking boards, and channel feeds. 31 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured Weibo social data through Scavio API endpoints for user, post, comment, keyword-search, hot-search, ranking, and channel-feed workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to Scavio's external API using SCAVIO_API_KEY.

Mitigation: Store the API key in the runtime environment or a secret store, keep it out of source control, and confirm the destination API before use.

Risk: Every Weibo endpoint call consumes credits, including empty results.

Mitigation: Run only intended queries, paginate with returned cursors, and monitor remaining credits in API responses.

Risk: Weibo posts, comments, follower lists, and user details can describe real people.

Mitigation: Summarize returned content and avoid using the skill to profile individuals or fabricate personal details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/weibo-scraper-api)
- [Scavio Weibo API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown guidance with inline bash, Python, curl, and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls spend credits and return structured JSON envelopes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
