## Description:

Query paginated product trade data for a company to retrieve product names with trade counts, amounts, quantities, weights, percentages, and associated HS codes for product-mix analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve paginated product-level customs trade statistics for a known company. It supports product-mix analysis by returning trade counts, amounts, quantities, weights, percentages, and HS codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an UpKuaJing API key stored in ~/.upkuajing/.env.

Mitigation: Keep the local API key file private and do not include the key in shared logs, prompts, or error reports.

Risk: Product-list API calls and account top-ups can incur fees.

Mitigation: Confirm fee-incurring queries or top-up actions before running them, and use the published pricing page or price-info command for current costs.

Risk: Optional error reports may include business data or request details.

Mitigation: Review and redact report content before submission so it does not include sensitive business data or secrets.

## Reference(s):

- [Company Product List API](references/customs-company-product-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-product-list)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; product-list calls are paginated and fee-incurring.]

## Skill Version(s):

1.0.1 (source: SKILL.md metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
