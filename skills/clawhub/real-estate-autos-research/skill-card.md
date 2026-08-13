## Description:

Researches homes and used cars via the Crawlora API, covering Zillow and Redfin property search, estimates, and market trends, plus CarMax, Autotrader, and Cars.com vehicle search and listing details, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search residential real estate and used vehicle listings, retrieve property or vehicle details, compare listings, and check market or valuation signals through documented Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call arbitrary Crawlora API paths, which is broader than the home and car research scope described by the skill.

Mitigation: Use only the documented Zillow, Redfin, CarMax, Autotrader, and Cars.com endpoints unless broader Crawlora access is intentional.

Risk: The skill depends on a Crawlora API key and credit-backed API usage.

Mitigation: Keep CRAWLORA_API_KEY private, avoid committing it, and monitor Crawlora credit usage.

Risk: Real estate estimates, vehicle prices, and market trend data can be incomplete or unsuitable as professional advice.

Mitigation: Treat outputs as research inputs and verify important real estate, financial, or purchasing decisions with authoritative sources or qualified professionals.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public listing, detail, estimate, trend, and dealer data from Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
