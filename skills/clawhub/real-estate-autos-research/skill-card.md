## Description:

Researches public property and vehicle listings, property estimates, and market trends through Crawlora and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, car shoppers, and research agents use the skill to compare public listings, check property estimates and local market trends, and inspect vehicle or dealer details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property or vehicle search terms, locations, listing IDs, and the API key are sent to Crawlora.

Mitigation: Use only necessary search details and a dedicated API key; do not include sensitive information in queries.

Risk: Additional Rightmove endpoints are supported but omitted from the main skill description.

Mitigation: Review the endpoint reference to understand the full supported scope before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)
- [Supported endpoint reference](reference/endpoints.md)
- [Crawlora API and key setup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown research summaries and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches can be filtered by location, property or vehicle identifiers, and listing attributes.]

## Skill Version(s):

1.0.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
