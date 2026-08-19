## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio for creator research, influencer vetting, competitor tracking, and social-media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram lookup requests are sent through Scavio using the user's SCAVIO_API_KEY.

Mitigation: Install and use the skill only when that third-party API path is acceptable, and keep the API key out of shared outputs and logs.

Risk: Multi-page or follower-list workflows can consume paid credits quickly.

Mitigation: Check remaining credits, estimate cost before loops, use larger page sizes where supported, and stop on out-of-credit responses.

Risk: The skill retrieves public social data that can include profile, post, comment, follower, and following information.

Mitigation: Use returned public social data responsibly and align collection, retention, and sharing with applicable policies and laws.

## Reference(s):

- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with curl examples and JSON API response handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY; Instagram endpoint costs range from 2 to 10 credits per successful request.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
