## Description:

This skill queries Upkuajing customs import-export data by company ID and company role to summarize trade count, weight, quantity, amount, partner count, and trade date range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, analysts, and researchers use this skill to retrieve company-level customs trade summaries and assess trade scale and partner-network breadth. It supports supplier screening, buyer validation, and trade intelligence workflows that require paid Upkuajing API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a paid Upkuajing API key in ~/.upkuajing/.env.

Mitigation: Protect the .env file, limit local access to the key, and rotate the key if exposure is suspected.

Risk: Customs data queries can incur charges through the Upkuajing API.

Mitigation: Confirm each billable call with the user in a separate message before executing the query.

Risk: The skill contacts openapi.upkuajing.com and performs an automatic version check.

Mitigation: Install only where this network behavior is acceptable and monitor outbound access to the expected Upkuajing API host.

Risk: Optional error reports can include business context from failed API calls.

Mitigation: Send error reports only after user confirmation and avoid including sensitive business details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-stats-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company trade statistics API reference](artifact/references/customs-company-stats-api.md)
- [Skill error report API reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; billable API calls should be confirmed separately before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
