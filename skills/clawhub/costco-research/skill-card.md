## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Costco products, compare categories, check US delivery availability, find nearby warehouses, and review product feedback through Crawlora rather than scraping Costco.com directly.

### Deployment Geography for Use:

Global; Costco delivery availability lookup is limited to US postal code and state inputs.

## Known Risks and Mitigations:

Risk: Costco search terms, product identifiers, warehouse coordinates, and availability lookup locations are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid including unrelated personal or confidential data in queries or request bodies.

Risk: The Crawlora API key could be exposed if copied into prompts, command history, or committed files.

Mitigation: Store the key only in the CRAWLORA_API_KEY environment variable and do not hardcode or pass it as a query parameter.

Risk: Availability checks are limited to US postal code and state inputs, so results may not apply to non-US delivery scenarios.

Mitigation: Use the availability endpoint only for US destinations and state the limitation when answering non-US availability requests.

## Reference(s):

- [Costco endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Costco Research on ClawHub](https://clawhub.ai/tonywangcn/skills/costco-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs API calls that return normalized JSON from Crawlora.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
