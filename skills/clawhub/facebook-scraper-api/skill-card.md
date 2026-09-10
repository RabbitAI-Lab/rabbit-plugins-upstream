## Description:

Pull a Facebook page's profile, posts, reels and photos, one post with its comments, a single reel/video with downloadable URLs, a public group and its posts, an event, and hashtag posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve structured public Facebook page, post, reel, group, event, hashtag, and comment data through Scavio API endpoints for brand monitoring, competitor analysis, and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access to SCAVIO_API_KEY can spend Scavio credits while retrieving public Facebook data.

Mitigation: Store the key in an environment or secret store, scope access to trusted agents, and monitor credit usage.

Risk: Returned Facebook profile, post, comment, and contact fields can include personal or contact information.

Mitigation: Summarize and handle returned data with care, respect Scavio and Facebook terms, and avoid profiling individuals.

Risk: Reel and video download URLs are signed and short-lived.

Mitigation: Use download URLs promptly and avoid storing them as durable assets.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/facebook-scraper-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API usage consumes credits and may return short-lived downloadable media URLs.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
