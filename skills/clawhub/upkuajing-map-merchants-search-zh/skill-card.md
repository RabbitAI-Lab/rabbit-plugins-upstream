## Description:

Uses the Upkuajing map merchant database to search overseas local businesses, stores, and service providers by geography, industry, rating, keyword, and contact filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, channel, brand, and regional expansion teams use this skill to find merchant leads, inspect local market density, support distributor sourcing, and plan store or channel coverage by location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant search calls can incur charges through a paid Upkuajing API key.

Mitigation: Check current pricing and obtain explicit user confirmation before paid searches, large result counts, or recharge actions.

Risk: The API key may be stored locally in ~/.upkuajing/.env.

Mitigation: Keep the local credential file private and avoid sharing command output or logs that could expose the key.

Risk: Optional diagnostic reports may include request context or business details.

Mitigation: Review diagnostic content before sending and remove secrets, customer data, or unnecessary business information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-map-merchants-search-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Merchant search API reference](references/merchants-search-api.md)
- [Country list API reference](references/country-list-api.md)
- [Province list API reference](references/province-list-api.md)
- [City list API reference](references/city-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with Python command examples, JSON API summaries, and JSONL merchant result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Merchant search results are paginated and saved under per-task result files; geography list commands can also write local JSON list files.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
