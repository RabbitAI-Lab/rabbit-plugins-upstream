## Description:

Pull a Facebook page's profile, posts, reels and photos, one post with its comments, a single reel/video with downloadable URLs, a public group and its posts, an event, and hashtag posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured public Facebook page, post, reel, group, event, and hashtag data for brand monitoring, competitor analysis, and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests go to Scavio's external API and may consume Scavio credits.

Mitigation: Use the skill only for legitimate requests, keep SCAVIO_API_KEY in a secret store or environment variable, and watch for credit usage and 402 billing responses.

Risk: Returned Facebook content may involve real people.

Mitigation: Summarize and use only the needed fields; do not profile individuals or fabricate follower counts, comments, contact details, or post text.

Risk: The API has bounded coverage and time-sensitive outputs, including top posts/comments only and short-expiring reel or video URLs.

Mitigation: State these limits in agent responses and use expiring media URLs promptly when the user asks to retrieve them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/facebook-scraper-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API calls may consume credits.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
