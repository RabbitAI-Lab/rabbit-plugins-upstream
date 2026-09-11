## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, and Reddit via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public social-media profiles, posts, engagement, search results, and trending topics through Crawlora instead of scraping individual platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research queries and requested targets are sent to Crawlora.

Mitigation: Install only when this data sharing is acceptable and keep CRAWLORA_API_KEY scoped, private, and out of source control.

Risk: The security scan reports that the helper reaches beyond the nine platforms and request methods advertised.

Mitigation: Review the endpoint reference before use and restrict agent calls to endpoints and methods approved for the intended workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/social-media-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Endpoint Reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends public-data research queries to Crawlora.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
