## Description:

Queries UpKuajing customs data for paginated company HS-code trade records, including trade count, amount, quantity, weight, and trade share.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams and analysts use this skill to inspect a company's HS-code product mix, compare supplier or buyer trade categories, and drill into paginated customs trade details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls may incur account charges.

Mitigation: Tell the user a query will incur cost and wait for explicit confirmation before running paid requests.

Risk: The API key and account metadata are sensitive.

Mitigation: Keep ~/.upkuajing/.env private and do not print the API key in chats or logs.

Risk: Optional error reports can include request context and API usage details.

Mitigation: Submit error reports only after user confirmation and include only the context needed for troubleshooting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-list-zh)
- [UpKuajing homepage](https://www.upkuajing.com)
- [UpKuajing developer platform](https://developer.upkuajing.com/)
- [UpKuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company HS-code list API reference](references/customs-company-hscode-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and formatted JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; successful queries include paginated HS-code trade data, fee information, and requestId.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
