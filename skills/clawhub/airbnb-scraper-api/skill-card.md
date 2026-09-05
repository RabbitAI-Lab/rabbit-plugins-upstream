## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External agents, developers, and travel or hospitality analysts use this skill to search Airbnb stays, compare stay-total pricing, inspect listing details, and summarize guest reviews through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Airbnb search criteria, listing IDs, and review requests to Scavio's API.

Mitigation: Use the skill only when sharing those inputs with Scavio is acceptable, and avoid sending unnecessary sensitive context.

Risk: Returned host profiles and guest review text may contain personal data.

Mitigation: Summarize review and host information for the requested task, and avoid profiling individuals.

Risk: Airbnb prices can be misleading when dates are defaulted or currency is omitted.

Mitigation: Provide explicit check-in and check-out dates plus currency, and do not quote prices from responses marked as defaulted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/airbnb-scraper-api)
- [Scavio Airbnb API documentation](https://scavio.dev/docs/airbnb-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=airbnb-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=airbnb-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and code examples for JSON API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs and recommendations depend on live Scavio API responses and caller-provided Airbnb search criteria.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
