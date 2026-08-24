## Description:

Pull a Facebook page's profile, posts, reels and photos, one post with its comments, a single reel/video with downloadable URLs, a public group and its posts, an event, and hashtag posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve structured Facebook page, post, reel, group, event, and hashtag data through Scavio's API for brand monitoring, competitor analysis, and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facebook URLs, page or group IDs, post and reel links, event links, and hashtags are sent to Scavio's API.

Mitigation: Use the skill only when sharing those targets with Scavio is acceptable, and avoid confidential investigation targets unless that sharing has been approved.

Risk: The skill requires a Scavio API key.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source control.

Risk: Returned Facebook profiles, posts, and comments can involve real people and may be incomplete or unavailable.

Mitigation: Summarize returned data, avoid building profiles of individuals, and report only what the API returned.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio Facebook API Skill on ClawHub](https://clawhub.ai/scavio-ai/skills/scavio-facebook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends requested Facebook targets to the Scavio API.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
