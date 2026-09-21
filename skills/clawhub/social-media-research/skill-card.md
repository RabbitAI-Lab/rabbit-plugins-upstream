## Description:

Researches public social-media profiles, posts, engagement, search results, and trending topics across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, Reddit, Bilibili, and Patreon through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and developers use this skill to retrieve normalized JSON for public social-media research, competitor monitoring, influencer vetting, brand-mention sweeps, marketplace discovery, and same-day trend scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use only approved public research queries, keep the key in CRAWLORA_API_KEY, and do not submit secrets, private personal data, or sensitive investigation terms unless approved.

Risk: Commercial discovery endpoints such as Reddit leads, Marketplace, ads, and product-directory searches can produce business-intelligence outputs beyond ordinary social profile lookup.

Mitigation: Invoke those endpoint families deliberately and only when commercial intelligence collection is intended and authorized.

Risk: Platform coverage and result depth vary, including narrowed public surfaces and pagination limits.

Mitigation: Check the endpoint reference before relying on a platform surface and follow returned cursors or documented endpoint limits when interpreting results.

## Reference(s):

- [social-media-research endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/social-media-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown guidance with shell command examples and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET endpoints for public social-media and commercial discovery data.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
