## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio for creator research, competitor tracking, and social-media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key.

Mitigation: Install only when the agent is allowed to use SCAVIO_API_KEY, and avoid exposing the key in prompts, logs, or generated examples.

Risk: Instagram API calls can consume paid or limited Scavio credits.

Mitigation: Estimate credit use before multi-call workflows, prefer lower-cost endpoints when sufficient, and stop when the user has not approved additional spend.

Risk: The skill can retrieve public Instagram comments, follower lists, and active stories.

Mitigation: Use it only for user-requested research and apply applicable platform, privacy, and legal constraints to collection and retention.

Risk: Raw upstream Instagram responses may vary in shape and field names.

Mitigation: Probe response keys defensively and avoid reporting normalized fields unless they are present in the returned data.

## Reference(s):

- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns guidance for retrieving raw public Instagram data through Scavio endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
