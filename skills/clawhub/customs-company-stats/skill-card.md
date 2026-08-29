## Description:

Fetches aggregated customs-trade statistics by company ID across more than 220 countries and territories for supplier screening, buyer validation, and trade-intelligence analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External export teams, analysts, researchers, and agents use this skill to retrieve summarized company trade activity, including shipment frequency, weight, quantity, transaction value, trade date range, and partner counts. It supports evaluating trading scale and partner networks for supplier screening, buyer validation, and trade-intelligence research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid UpKuaJing API, so normal query and top-up actions can incur fees.

Mitigation: Inform the user when an action may incur a fee and wait for explicit confirmation before running the query or creating a top-up order.

Risk: The skill depends on UPKUAJING_API_KEY and local credential storage.

Mitigation: Keep the API key private, avoid printing or sharing ~/.upkuajing/.env, and only use the key for intended UpKuaJing API calls.

Risk: Error reports may include business context or request details.

Mitigation: Ask for user confirmation before reporting an error and avoid including secrets, personal data, or sensitive business information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-stats)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company Basic Trade Statistics API](references/customs-company-stats-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; fee-incurring API calls require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
