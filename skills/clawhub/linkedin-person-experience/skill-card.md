## Description:

Check LinkedIn work history by personnel ID to review previous employers, job titles, employment dates, and candidate work-history timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, hiring managers, sales teams, and talent-acquisition workflows use this skill to retrieve LinkedIn work-history records for candidate vetting, pre-employment background checks, and professional background review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries sensitive employment-history data from a third-party LinkedIn dataset.

Mitigation: Use it only when authorized to query the person’s work-history data and when sending LinkedIn identifiers to UpKuaJing is acceptable.

Risk: API calls and account-management flows may incur paid charges.

Mitigation: Confirm current pricing and obtain explicit user approval before any fee-incurring query or top-up action.

Risk: The default setup stores the UpKuaJing API key in a plaintext local environment file.

Mitigation: Prefer a protected secret manager or secured environment variable, and restrict access to any local credential file.

Risk: Error reports can include operational context from failed calls.

Mitigation: Send reports only after user confirmation and avoid raw candidate data, full responses, tokens, or stack traces.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-person-experience)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Work Experience List API](artifact/references/linkedin-person-experience-list-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkedIn personnel ID, UpKuaJing API key, and user confirmation before fee-incurring calls.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
