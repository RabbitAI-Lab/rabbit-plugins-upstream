## Description:

Researches homes and used cars via the Crawlora API - Zillow and Redfin property search/estimates/market trends, plus CarMax, Autotrader, and Cars.com vehicle search and dealer/listing detail - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to research real estate and vehicle listings, property estimates, market trends, comparable properties, and dealer or listing detail through documented Crawlora API routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends search terms such as locations, ZIP codes, listing IDs, and price filters to Crawlora.

Mitigation: Confirm the user is comfortable sharing those query details with Crawlora and avoid sending sensitive or unnecessary personal information.

Risk: The skill requires a Crawlora API key for API access.

Mitigation: Store the key only in CRAWLORA_API_KEY, keep it out of prompts and command-line arguments, and do not commit it.

Risk: Rightmove property endpoints are supported even though the main description emphasizes Zillow, Redfin, CarMax, Autotrader, and Cars.com.

Mitigation: Disclose Rightmove coverage when relevant and consult the endpoint reference before calling those routes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill release page](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized public listing, estimate, trend, vehicle, dealer, and endpoint response data.]

## Skill Version(s):

1.0.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
