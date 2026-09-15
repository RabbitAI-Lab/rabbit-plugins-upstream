## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Costco products, compare categories, check product details, availability, nearby warehouses, and reviews through Crawlora instead of scraping Costco.com directly.

### Deployment Geography for Use:

Global; Costco availability lookup is limited to US postal_code and two-letter state inputs.

## Known Risks and Mitigations:

Risk: Costco queries, product identifiers, ZIP/state destination data, precise coordinates when used, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, avoid entering unnecessary precise location details, and keep the API key in CRAWLORA_API_KEY rather than in prompts, files, or command arguments.

Risk: The helper accepts a POST mode even though the documented Costco endpoints are GET-only.

Mitigation: Invoke the helper with documented GET calls for Costco endpoints and avoid using -X POST for this skill.

## Reference(s):

- [Costco endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/costco-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized JSON from Crawlora Costco endpoints.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
