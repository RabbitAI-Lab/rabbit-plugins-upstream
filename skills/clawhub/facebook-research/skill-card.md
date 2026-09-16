## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details (name, follower/like counts, category, contact info) via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to research public Facebook Marketplace listings and public Facebook Page details through the Crawlora API for local price checks, lead enrichment, and public business profile review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace search terms, Facebook Page references, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode, commit, or pass it in query parameters.

Risk: The skill is intended for public Facebook Marketplace listings and public Page data, not private or logged-in content.

Mitigation: Use it only for public Facebook content and avoid private, session-based, or access-controlled data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/facebook-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; returns public Facebook Marketplace and Page data only.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
