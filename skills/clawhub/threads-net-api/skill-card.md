## Description:

Read Threads profiles, a user's posts and replies, a single post, its comment tree, and search Threads people as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve public Threads profile, post, reply, comment, and people-search data through the Scavio API for creator research, brand monitoring, competitor research, or account-level analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested public Threads handles, post IDs, or URLs to Scavio as a third-party API provider.

Mitigation: Confirm the user is comfortable using Scavio for the request and avoid submitting sensitive or non-public data.

Risk: Requests consume Scavio API credits, and username-based profile, posts, and replies calls cost more than user_id calls.

Mitigation: Resolve a handle once, reuse user_id for paginated calls, and check credits_used in responses.

Risk: The skill requires SCAVIO_API_KEY.

Mitigation: Store the key in an environment variable or secret manager and keep it out of source control.

Risk: Threads content search is unavailable through this API.

Mitigation: For topic or keyword research, retrieve posts from known accounts and filter client-side instead of claiming platform-wide content search.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/threads-net-api)
- [Scavio Threads profile documentation](https://scavio.dev/docs/threads-profile)
- [Scavio Threads user posts documentation](https://scavio.dev/docs/threads-user-posts)
- [Scavio Threads user replies documentation](https://scavio.dev/docs/threads-user-replies)
- [Scavio Threads post documentation](https://scavio.dev/docs/threads-post)
- [Scavio Threads post comments documentation](https://scavio.dev/docs/threads-post-comments)
- [Scavio Threads user search documentation](https://scavio.dev/docs/threads-user-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns structured JSON from Scavio API endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
