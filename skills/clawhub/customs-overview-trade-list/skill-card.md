## Description:

Query paginated national trade list data to retrieve country-level annual, quarterly, and monthly trade volumes for market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External export teams, market researchers, and trade analysts use this skill to compare country-level import-export volumes, analyze market penetration, and identify growth opportunities from structured trade data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls may incur charges for each paginated trade-list request.

Mitigation: Require explicit user confirmation before paid queries and use the platform pricing reference or price-info script for current pricing.

Risk: The API key is stored in plaintext under ~/.upkuajing/.env when configured locally.

Mitigation: Protect the file like any other credential, avoid sharing it, and rotate the API key if exposure is suspected.

Risk: Error reports can include troubleshooting context and request details.

Mitigation: Submit error reports only after user confirmation and avoid including extra sensitive details in the report context.

## Reference(s):

- [Trade List API Reference](references/customs-overview-trade-list-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [UpKuaJing](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API queries return paginated country trade records with fee and request identifiers.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
