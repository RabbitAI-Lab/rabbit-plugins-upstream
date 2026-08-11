## Description:

Researches public X (formerly Twitter) profiles and posts via the Crawlora API, returning normalized JSON for profile stats, recent posts, and individual post content and engagement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public X profile data, recent posts, or a specific post's text and engagement through Crawlora instead of scraping x.com or using the official X API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make authenticated Crawlora API requests beyond the three documented X endpoints.

Mitigation: Restrict use to GET /x/profile/{username}, GET /x/profile/{username}/posts, and GET /x/post/{id}; review any call path before execution.

Risk: The skill requires a Crawlora API key for authenticated requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid hardcoding or sharing it in prompts or files, and rotate it if exposed.

Risk: Returned X data is public, endpoint-limited, and may be incomplete for timelines or deleted or restricted content.

Mitigation: Treat responses as point-in-time public data and verify important conclusions against additional sources before relying on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/x-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public X data from Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
