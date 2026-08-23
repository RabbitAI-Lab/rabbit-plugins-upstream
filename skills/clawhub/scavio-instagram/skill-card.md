## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio for creator research, competitor tracking, and influencer vetting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and can spend Scavio credits when retrieving Instagram data.

Mitigation: Set page and credit limits before large follower, following, comment, or story collection tasks, and check remaining credits during multi-call workflows.

Risk: Large collection tasks can become costly because most Instagram endpoints cost 8 to 10 credits per call.

Mitigation: Prefer lower-cost endpoints when they answer the user's question, raise page size instead of making repeated calls, and confirm the expected spend before looping.

Risk: Instagram responses are raw upstream passthroughs with fields and pagination keys that can vary by endpoint and provider response.

Mitigation: Inspect returned keys defensively, avoid inventing normalized field names, and stop pagination when continuation signals are absent or repeated.

## Reference(s):

- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api)
- [Scavio API base URL](https://api.scavio.dev)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-instagram)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API calls that return raw JSON from Scavio's Instagram endpoints.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
