## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, and Reddit via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and social-media analysts use this skill to inspect public profiles, posts, engagement, search results, and trending topics through Crawlora API calls. It supports competitor audits, brand-mention sweeps, influencer vetting, and cross-platform trend scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Social handles, search terms, listing queries, and related research targets are sent to Crawlora.

Mitigation: Send only the public research inputs needed for the task and avoid including secrets or unrelated private data in request bodies.

Risk: Changing CRAWLORA_API_BASE can redirect API-key-authenticated requests to another destination.

Mitigation: Keep the default Crawlora API base unless the replacement endpoint is fully trusted.

Risk: The available endpoint surface is broader than the nine social platforms emphasized in the headline description.

Mitigation: Review the endpoint reference before use so calls stay within the intended platforms and data surfaces.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests return normalized JSON from Crawlora.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
