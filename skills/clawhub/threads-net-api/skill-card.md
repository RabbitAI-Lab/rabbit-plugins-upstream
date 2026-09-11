## Description:

Read Threads profiles, a user's posts and replies, a single post, its comment tree, and search Threads people as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to retrieve public Threads profile, post, reply, comment, and people-search data through Scavio with cost-aware API usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends Threads queries to Scavio's API.

Mitigation: Provide the API key through the environment, avoid placing it in source files or prompts, and install only when the data flow is acceptable.

Risk: Paging through posts or replies can consume paid Scavio credits, especially when using usernames instead of user IDs.

Mitigation: Resolve a handle once, reuse the returned user_id, monitor credits_used and credits_remaining, and stop pagination when next_cursor is null.

Risk: Returned Threads data is public social-media content and may be incomplete, stale, or unverified.

Mitigation: Preserve attribution, avoid fabricating engagement or profile details, and present summaries as API-returned public data rather than verified facts.

Risk: Threads content search is not supported by this API.

Mitigation: Use /search/users only for people search; for topic or keyword work, pull posts from known accounts and filter client-side.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/threads-net-api)
- [Scavio Threads profile documentation](https://scavio.dev/docs/threads-profile?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user posts documentation](https://scavio.dev/docs/threads-user-posts?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user replies documentation](https://scavio.dev/docs/threads-user-replies?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads post documentation](https://scavio.dev/docs/threads-post?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads post comments documentation](https://scavio.dev/docs/threads-post-comments?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user search documentation](https://scavio.dev/docs/threads-user-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON API examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are structured JSON envelopes with data, response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
