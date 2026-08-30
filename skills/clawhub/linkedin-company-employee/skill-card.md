## Description:

Pulls LinkedIn employee lists and job titles from UpKuaJing by company ID for corporate hierarchy research, talent mapping, and B2B lead qualification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead-generation specialists use this skill to retrieve employee names, person identifiers, and job titles from LinkedIn company data. It supports talent mapping, organizational analysis, team-structure checks, and lead qualification when the user has a company ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid UpKuaJing API and employee list lookups can incur fees.

Mitigation: Tell the user a lookup may incur a fee and wait for explicit confirmation before running fee-incurring calls; use the pricing endpoint or UpKuaJing pricing page for current rates.

Risk: The API key is sensitive and may be stored in ~/.upkuajing/.env.

Mitigation: Keep UPKUAJING_API_KEY protected, avoid sharing command output that may reveal credentials, and limit access to the local credentials file.

Risk: Error reports may include operational context from failed API calls.

Mitigation: Review error report text and request details before sending, and only submit reports after user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-company-employee)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn Company Employee List API](artifact/references/linkedin-company-employee-list-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Python runtime and UPKUAJING_API_KEY; employee list calls return paginated records with fee and request identifiers.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
