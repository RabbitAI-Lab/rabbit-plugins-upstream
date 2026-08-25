## Description:

Researches public X (formerly Twitter) profiles and posts via the Crawlora API and returns clean JSON for profile stats, recent posts, and single-post content and engagement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social-listening analysts use this skill to fetch public X profile details, recent profile posts, and individual post metrics through Crawlora when they do not have official X API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper accepts arbitrary API paths and methods, so it can be used outside the documented X-only endpoints.

Mitigation: Constrain agent use to the documented /x/profile/{username}, /x/profile/{username}/posts, and /x/post/{id} endpoints or edit the helper to allow only those paths.

Risk: Using the helper with a Crawlora API key can consume account credits for successful API calls.

Mitigation: Use a scoped or low-risk Crawlora key where possible, monitor usage, and avoid broad unattended runs.

## Reference(s):

- [x-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public X data returned by Crawlora; profile posts are limited to the first public profile page payload with a documented maximum of 50 posts.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
