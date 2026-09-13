## Description:

Researches homes and used cars via the Crawlora API, including Zillow and Redfin property search, estimates, and market trends plus CarMax, Autotrader, and Cars.com vehicle and dealer lookup, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research public real-estate listings, property estimates, market trends, used-car listings, vehicle details, and dealer information through Crawlora's normalized API responses. It is useful when an agent needs structured property or automotive research data rather than scraping listing pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises Zillow, Redfin, CarMax, Autotrader, and Cars.com, but the artifact also enables Rightmove property endpoints.

Mitigation: Review the endpoint scope before installation and authorize use only if the broader Rightmove real-estate coverage is acceptable.

Risk: Calls require a Crawlora API key and may consume account credits when requests succeed.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not commit it, and run only intentional, scoped requests through the provided helper.

Risk: Property estimates, market trends, and vehicle listing data can be incomplete, stale, or unsuitable for regulated advice.

Mitigation: Treat returned data as research input, cross-check important findings, and avoid presenting it as real-estate, financial, or legal advice.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to Crawlora's API; search endpoints may require pagination.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
