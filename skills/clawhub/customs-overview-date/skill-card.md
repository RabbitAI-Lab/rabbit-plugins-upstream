## Description:

Retrieves UpKuaJing date reference values for customs trade data queries, including last year, last month, and same-month-last-year.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, export teams, and import-export professionals use this skill to retrieve precise date parameters for customs data analysis, market trend analysis, and import-export trade research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid UpKuaJing API calls and top-up flows can incur charges.

Mitigation: Require explicit user confirmation before fee-incurring calls or top-up order creation, and verify current pricing through the documented price source before execution.

Risk: The UpKuaJing API key may be stored in a plaintext home-directory .env file.

Mitigation: Use an account appropriate for the task, restrict local file access, and avoid sharing or logging the API key.

Risk: The skill contacts UpKuaJing servers and can send diagnostic reports after confirmation.

Mitigation: Use it only in environments where outbound UpKuaJing requests are approved, and review diagnostic context before confirming a report.

Risk: Account and balance checks expose account-related information to the agent workflow.

Mitigation: Run account-management commands only when needed and share resulting account details only with authorized users.

## Reference(s):

- [Date Reference API](references/customs-overview-date-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON API results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an UpKuaJing API key and explicit confirmation before fee-incurring API calls.]

## Skill Version(s):

1.0.1 (source: metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
