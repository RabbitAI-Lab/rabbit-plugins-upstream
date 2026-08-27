## Description:

Gets monthly customs-trade breakdowns for a company, including shipment frequency, quantity, gross weight, and transaction value, using the UpKuaJing Open Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Export teams, analysts, and supply-chain managers use this skill to study monthly company trade patterns, seasonal changes, supplier performance, and long-term trade-flow trends across customs data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls can incur paid UpKuaJing charges.

Mitigation: Confirm the user wants to spend credits before each charged query and use the pricing endpoint or pricing page for current costs.

Risk: The skill stores and reads the UpKuaJing API key from the user's environment or ~/.upkuajing/.env.

Mitigation: Keep the API key private, restrict local file access, and rotate the key if it may have been exposed.

Risk: Top-up flows can return payment URLs.

Mitigation: Review the payment URL before opening it and confirm the amount before completing payment.

Risk: Raw API request and response logging can create local copies of query and response data if enabled.

Mitigation: Leave raw API logging disabled unless local retention is acceptable, and protect or delete logs when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-trends)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company Trade Trends API](references/customs-company-trends-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return monthly trend records with fee information and request IDs; the skill requires an UpKuaJing API key.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
