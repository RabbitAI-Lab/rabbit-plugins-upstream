## Description:

Pulls company trade-partner distributions, HS-code details, product portfolios, and monthly customs trade timelines by company ID across global markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Export teams, sourcing agents, and analysts use this skill to identify trade counterparts, analyze product and HS-code mix, and map supply-chain relationships from customs records. Agents can run paid UpKuaJing API queries for a specific company ID and company role after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and may write an UpKuaJing API key in ~/.upkuajing/.env.

Mitigation: Use a dedicated API key with the minimum required account permissions, keep the file private, and rotate the key if it may have been exposed.

Risk: Customs data queries are paid API calls.

Mitigation: Confirm the fee-bearing action in a separate user message before running the query, and use the pricing or account-info command when cost or balance is unclear.

Risk: Top-up flows can create payment URLs.

Mitigation: Only create top-up orders when the user explicitly requests it, and have the user complete payment directly on the provider page.

Risk: Optional diagnostic reports can send request details and context to UpKuaJing.

Mitigation: Ask for confirmation before reporting and remove secrets, raw business datasets, and sensitive customer information from diagnostic context.

Risk: The skill performs remote API calls, including an automatic version check.

Mitigation: Run it only in environments where outbound requests to UpKuaJing services are acceptable and review network behavior before deployment.

## Reference(s):

- [Company Trade Partner Trends API](references/customs-company-partner-stats-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-partner-stats)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with fee and request metadata, plus concise Markdown guidance for setup, confirmation, and interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY. Paid API calls require explicit user confirmation; diagnostic error reports are optional and should be sent only after confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
