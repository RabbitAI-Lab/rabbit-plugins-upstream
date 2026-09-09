## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details via the Crawlora API, returning normalized JSON instead of requiring direct Facebook scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to retrieve public Facebook Marketplace listing data for a location or category and public Facebook Page profile details for market research or lead enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to a non-Crawlora destination if CRAWLORA_API_BASE is changed.

Mitigation: Use the default Crawlora API base for normal use, and set CRAWLORA_API_BASE only in controlled tests with a non-production key.

Risk: The bundled helper is broader than the documented Facebook-only purpose.

Mitigation: Limit agent use to the documented GET /facebook/marketplace/search and GET /facebook/{page} endpoints unless the command is explicitly reviewed.

## Reference(s):

- [Facebook endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/facebook-research)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Marketplace results are limited to the first public page returned by the upstream service.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
