## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags across 12 endpoints that cost 2 to 10 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user search, and hashtag search data through Scavio's API for creator research, competitor tracking, and influencer vetting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram handles, post identifiers, and search terms to Scavio's API.

Mitigation: Install and use it only when sharing those inputs with Scavio is acceptable for the user's workflow.

Risk: Instagram API calls consume paid credits, with documented endpoint costs from 2 to 10 credits and multi-call workflows adding up quickly.

Mitigation: Check or discuss the credit budget before loops or pagination, prefer lower-cost endpoints when sufficient, and stop on billing or rate-limit errors.

Risk: Raw upstream Instagram responses may vary in structure and field names across calls.

Mitigation: Inspect returned keys defensively and avoid reporting missing data until the raw response shape has been checked.

## Reference(s):

- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=instagram-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Instagram endpoint calls are documented as 2 to 10 credits each.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
