## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio. It is suited for creator research, influencer vetting, competitor tracking, and user-directed social media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Follower lists, comments, stories, and profile details can include personal data.

Mitigation: Use only public Instagram data for lawful, user-directed purposes, and avoid bulk collection, profiling, or retention unless there is a clear need and authority.

Risk: Multi-page Instagram workflows can consume Scavio credits quickly.

Mitigation: Estimate endpoint and pagination costs before starting, set an explicit page budget, monitor credits remaining, and stop if the API reports exhausted credits.

Risk: Instagram responses are raw upstream passthroughs whose fields and top-level keys can vary by endpoint and provider response.

Mitigation: Inspect returned keys defensively, handle alternate data shapes such as items or data, and avoid inventing normalized field names when reporting results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)
- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=instagram-scraper-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume 2-10 Scavio credits per endpoint.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
