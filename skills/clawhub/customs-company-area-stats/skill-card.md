## Description:

Query company customs trade statistics by region dimension, including trade volume, amount, monthly trends, and country distribution across global markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query UpKuaJing customs data for a company's regional import-export distribution, country coverage, and monthly trade patterns. It supports market intelligence, supplier coverage assessment, and cross-border trade trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls can incur charges.

Mitigation: Confirm pricing and obtain explicit user approval before running fee-bearing queries.

Risk: The skill stores and uses an UpKuaJing API key.

Mitigation: Keep ~/.upkuajing/.env private and do not share API-key contents in chat or logs.

Risk: Error reports may include request context.

Mitigation: Review the report context and send it only after user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-area-stats)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Company Area Trade Statistics API](references/customs-company-area-stats-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls require explicit user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
