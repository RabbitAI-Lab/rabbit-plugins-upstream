## Description:

Read Threads profiles, user posts and replies, individual posts, comment trees, and people search results as structured JSON through Scavio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social media researchers use this skill to retrieve public Threads profile, post, reply, comment, and people-search data for creator, brand, competitor, or account monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using this skill may call Scavio with the user's SCAVIO_API_KEY and spend Scavio credits, especially during large paginated crawls.

Mitigation: Keep the API key in an environment variable or secret store, prefer user_id over username to reduce per-request credits, and verify expected usage costs before large crawls.

## Reference(s):

- [Scavio Threads Profile Documentation](https://scavio.dev/docs/threads-profile)
- [Scavio Threads User Posts Documentation](https://scavio.dev/docs/threads-user-posts)
- [Scavio Threads User Replies Documentation](https://scavio.dev/docs/threads-user-replies)
- [Scavio Threads Post Documentation](https://scavio.dev/docs/threads-post)
- [Scavio Threads Post Comments Documentation](https://scavio.dev/docs/threads-post-comments)
- [Scavio Threads User Search Documentation](https://scavio.dev/docs/threads-user-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-threads)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with API examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio Threads endpoints with a user-provided SCAVIO_API_KEY and to handle cursor pagination, credit costs, and common API errors.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
