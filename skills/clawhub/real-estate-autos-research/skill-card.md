## Description:

Researches public home and vehicle listings, property estimates, and market trends through Crawlora, including Zillow, Redfin, Rightmove, CarMax, Autotrader, and Cars.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Home shoppers, car shoppers, and researchers use this skill to compare public listings, check property estimates and market trends, and retrieve property, vehicle, or dealer details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and listing identifiers are sent to Crawlora with the user's API key, potentially disclosing sensitive location or business interests.

Mitigation: Use only with approved third-party access and avoid sensitive private locations or confidential business searches.

Risk: The main skill description omits included Rightmove routes.

Mitigation: Disclose Rightmove support in the skill description or remove those routes if unintended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown responses and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listing and market data returned through Crawlora; search results may be paginated.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
