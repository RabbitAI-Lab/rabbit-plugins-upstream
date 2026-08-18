## Description:

Researches homes and used cars via the Crawlora API - Zillow and Redfin property search, estimates, and market trends, plus CarMax, Autotrader, and Cars.com vehicle search and dealer or listing detail - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public home listings, property estimates, regional housing trends, used vehicle listings, and dealer or listing details through Crawlora API calls.

### Deployment Geography for Use:

Global, with United States-focused property and vehicle data sources.

## Known Risks and Mitigations:

Risk: The included Crawlora helper can call arbitrary Crawlora API endpoints with the user's API key, not only the documented real estate and vehicle endpoints.

Mitigation: Review and constrain helper use to the documented Zillow, Redfin, CarMax, Autotrader, and Cars.com endpoints before deployment.

Risk: Sensitive personal data or unrelated content could be sent to Crawlora through the helper.

Mitigation: Use only the minimum public listing, location, vehicle, or dealer data needed for the task, and avoid sending sensitive personal information.

Risk: Property estimates, market trends, and vehicle listing data may be incomplete, stale, or unsuitable for financial decisions.

Mitigation: Treat outputs as research inputs, cross-check important results with source platforms, and do not use the skill as real estate, financial, or legal advice.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search endpoints may be paginated.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
