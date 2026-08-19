## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags. 12 endpoints, 2-10 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, researchers, and agent users use this skill to retrieve public Instagram profile, post, comment, follower, following, story, reel, and search data through Scavio. It is suited for creator research, influencer vetting, competitor tracking, and social-media analysis workflows that can manage API-key and credit usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and can spend credits on Instagram lookups, especially large follower, following, or comment collection tasks.

Mitigation: Confirm API-key use before installation and set explicit page or credit limits before multi-call workflows.

Risk: Instagram responses are raw upstream data, so fields and pagination tokens may vary by endpoint and provider response.

Mitigation: Probe returned JSON defensively, avoid assuming normalized field names, and stop pagination when continuation fields are absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-instagram)
- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes raw upstream JSON fields, endpoint-specific identifiers, pagination, API-key setup, and credit budgeting.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
