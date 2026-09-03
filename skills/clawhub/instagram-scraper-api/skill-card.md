## Description:

Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags. 12 endpoints, 2-10 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio for creator research, competitor tracking, and social media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key to retrieve Instagram data.

Mitigation: Install and run it only when providing a Scavio API key is acceptable for the intended environment.

Risk: Large follower, following, comment, or multi-page collection tasks can spend Scavio credits quickly.

Mitigation: Set page, count, and credit limits before multi-call workflows and stop when the API reports insufficient credits.

Risk: Instagram responses are raw upstream JSON whose keys and pagination tokens can vary by endpoint and response path.

Mitigation: Probe response keys defensively and avoid presenting ordering, pagination progress, or normalized field names as guaranteed unless present in the returned JSON.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/instagram-scraper-api)
- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; responses are raw upstream Instagram JSON and requests consume Scavio credits.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
