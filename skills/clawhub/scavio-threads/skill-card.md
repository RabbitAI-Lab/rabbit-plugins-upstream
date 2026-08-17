## Description:

Read Threads profiles, a user's posts and replies, a single post, its comment tree, and search Threads people as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve public Threads profile, post, reply, comment, and people-search data through Scavio for creator, brand, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Threads queries are sent through Scavio and may consume account credits.

Mitigation: Use the skill for public Threads lookups, avoid unnecessary or sensitive query data, and prefer user_id-based calls after resolving a handle once.

Risk: The skill cannot search Threads content by keyword, topic, or hashtag.

Mitigation: Use /search/users only for people search; for known accounts, fetch posts and filter client-side without implying platform-wide content search.

Risk: Returned public social-media data can be incomplete, unavailable, or rate limited by the upstream service.

Mitigation: Handle 401, 404, 422, 429, and 502 responses explicitly, retry transient upstream errors once, and do not fabricate missing profile, post, or engagement data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-threads)
- [Scavio Threads profile documentation](https://scavio.dev/docs/threads-profile)
- [Scavio Threads user posts documentation](https://scavio.dev/docs/threads-user-posts)
- [Scavio Threads user replies documentation](https://scavio.dev/docs/threads-user-replies)
- [Scavio Threads post documentation](https://scavio.dev/docs/threads-post)
- [Scavio Threads post comments documentation](https://scavio.dev/docs/threads-post-comments)
- [Scavio Threads user search documentation](https://scavio.dev/docs/threads-user-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with request examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; user-keyed profile, posts, and replies calls cost fewer credits when addressed by user_id instead of username.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
