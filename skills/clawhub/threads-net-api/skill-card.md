## Description:

Read public Threads profiles, a user's posts and replies, a single post, its comment tree, and Threads people-search results as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Threads profile, post, reply, comment, and people-search data for creator research, brand or competitor analysis, and account monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the configured Scavio API key to Scavio's API and consumes Scavio credits for each request.

Mitigation: Use a scoped Scavio API key, keep it in the environment rather than source code, monitor credits_used and credits_remaining, and run only intended public Threads data lookups.

Risk: Threads content search is not supported, and treating people search as content search can produce misleading results.

Mitigation: Tell users when topic, keyword, or hashtag search is unavailable and, when appropriate, retrieve posts from known accounts and filter client-side.

Risk: Using usernames instead of user_id values doubles the credit cost for profile, user posts, and user replies endpoints.

Mitigation: Resolve a handle once, reuse the returned user_id for subsequent calls, and read credits_used from each response.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/threads-net-api)
- [Scavio Threads profile documentation](https://scavio.dev/docs/threads-profile)
- [Scavio Threads user posts documentation](https://scavio.dev/docs/threads-user-posts)
- [Scavio Threads user replies documentation](https://scavio.dev/docs/threads-user-replies)
- [Scavio Threads post documentation](https://scavio.dev/docs/threads-post)
- [Scavio Threads post comments documentation](https://scavio.dev/docs/threads-post-comments)
- [Scavio Threads user search documentation](https://scavio.dev/docs/threads-user-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with JSON response descriptions and Python or bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses use a structured JSON envelope with data, response_time, credits_used, and credits_remaining; cursor-paginated endpoints include next_cursor.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
