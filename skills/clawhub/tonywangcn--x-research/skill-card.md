## Description:

Researches public X (formerly Twitter) profiles, recent posts, and individual post metrics through Crawlora API endpoints and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve public X profile details, recent profile posts, or a specific public post when they need structured social-listening data without browser automation or official X API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the user's API key to an environment-selected API base or endpoints beyond the documented X routes.

Mitigation: Keep CRAWLORA_API_BASE unset or pinned to https://api.crawlora.net/api/v1, restrict use to the documented GET /x/profile/{username}, GET /x/profile/{username}/posts, and GET /x/post/{id} endpoints, and avoid environments where untrusted input can control command arguments.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/x-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; documented X endpoints cover public profiles, first-page profile posts, and numeric post lookup.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
