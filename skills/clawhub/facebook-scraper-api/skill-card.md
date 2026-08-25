## Description:

Pull a Facebook page's profile, posts, reels and photos, one post with its comments, a single reel/video with downloadable URLs, a public group and its posts, an event, and hashtag posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured public Facebook page, post, reel, group, event, and hashtag data for brand monitoring, competitor analysis, influencer research, and content insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Scavio's third-party API.

Mitigation: Use only when the user is comfortable sharing the Facebook pages, posts, reels, groups, events, or hashtags being queried with Scavio.

Risk: The skill requires an API key.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source code.

Risk: Facebook profiles, posts, and comments can involve real people.

Mitigation: Summarize results, avoid building profiles of individuals, and return only data provided by the API.

Risk: Returned data may be incomplete because private groups, locked profiles, unavailable surfaces, full feeds, and full comment threads are out of scope.

Mitigation: Represent unavailable or limited results accurately and do not fabricate follower counts, post text, comment text, or contact details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/facebook-scraper-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=facebook-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Python and curl examples; API calls return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. API responses use a data envelope with response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
