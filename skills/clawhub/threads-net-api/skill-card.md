## Description:

Read Threads profiles, a user's posts and replies, a single post, its comment tree, and search Threads people as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Threads profile, post, reply, comment, and people-search data through Scavio. It is suited for creator research, brand or competitor monitoring, and workflows that need structured JSON from known Threads accounts or posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Threads handles, user IDs, post IDs, and lookup queries are sent to Scavio.

Mitigation: Use the skill only for data the user is comfortable sending to Scavio, and limit lookups to public Threads data needed for the task.

Risk: SCAVIO_API_KEY is required for all API calls.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, and do not commit it to source control.

Risk: API calls spend Scavio credits, with username-based user lookups costing more than user_id lookups.

Mitigation: Resolve a handle once, reuse the returned user_id for later calls, and check response credit fields rather than assuming cost.

Risk: The API supports Threads people search, not content, keyword, topic, or hashtag search.

Mitigation: For content analysis, retrieve posts from known accounts and filter client-side instead of presenting the skill as a Threads content search tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/threads-net-api)
- [Scavio Threads profile documentation](https://scavio.dev/docs/threads-profile?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user posts documentation](https://scavio.dev/docs/threads-user-posts?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user replies documentation](https://scavio.dev/docs/threads-user-replies?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads post documentation](https://scavio.dev/docs/threads-post?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads post comments documentation](https://scavio.dev/docs/threads-post-comments?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio Threads user search documentation](https://scavio.dev/docs/threads-user-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=threads-net-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with HTTP request examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; requests consume Scavio credits and return public Threads data only.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
