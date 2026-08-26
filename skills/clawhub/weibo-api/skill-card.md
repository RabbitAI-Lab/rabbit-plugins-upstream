## Description:

Pull Weibo user profiles and posts, post comments/likes/reposts, keyword search across posts, videos, users, topics and images, the hot-search board and ranking boards, and channel feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured Weibo user, post, comment, search, hot-search, ranking, and channel-feed data through the Scavio API for social listening, trend spotting, creator research, and topic research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weibo lookup targets and search terms are sent to Scavio when the API is used.

Mitigation: Use the skill only when the user understands that queried IDs, handles, post IDs, and keywords are sent to the provider; avoid sensitive investigations unless that disclosure is acceptable.

Risk: Returned Weibo posts and comments may describe real people and may be incomplete or time-sensitive.

Mitigation: Summarize returned content, avoid building individual profiles, re-fetch hot-search or ranking boards when freshness matters, and do not fabricate counts, post text, comment text, or user details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/weibo-api)
- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and Python or curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each Weibo endpoint call uses 1 credit and returns a response envelope with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
