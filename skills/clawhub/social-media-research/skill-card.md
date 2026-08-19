## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, and Reddit via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to research public social-media profiles, posts, engagement, searches, trending topics, and brand or competitor mentions across supported platforms through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Social-media handles, post IDs, search terms, and related research targets are sent to Crawlora.

Mitigation: Use only for public, appropriate research targets and avoid private, regulated, confidential, or sensitive investigative queries unless Crawlora's data handling and terms have been reviewed.

Risk: The skill requires a Crawlora API key.

Mitigation: Store CRAWLORA_API_KEY in the environment or a secrets manager and do not hardcode it, put it in query parameters, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/social-media-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests transmit public handles, post IDs, search terms, and related research targets to Crawlora.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
