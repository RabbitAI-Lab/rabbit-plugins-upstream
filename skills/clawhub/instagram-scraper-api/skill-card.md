## Description:

Guides agents in retrieving public Instagram profiles, posts, reels, stories, comments, follower lists, and search results through Scavio's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to retrieve public Instagram account and content data for creator discovery, competitor research, and authorized social-media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram lookup targets are sent to Scavio, and collecting follower, comment, or story data can expose sensitive personal information.

Mitigation: Use only for authorized, legitimate research; minimize collection and avoid bulk profiling or harassment.

Risk: Repeated or paginated requests can consume Scavio credits.

Mitigation: Estimate costs before multi-call workflows, monitor remaining credits, and stop when the API reports insufficient credits.

## Reference(s):

- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=instagram-scraper-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown guidance and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Scavio API key; requests consume 2–10 credits per endpoint.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
