## Description:

Retrieves overseas employee profiles by company ID, including job-level details for recruitment, talent mapping, and B2B lead qualification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External recruiters, sales teams, and B2B lead generation specialists use this skill to retrieve paginated employee profile records for a known company ID and identify potential decision-makers. The skill supports contact enrichment, competitor organization analysis, and role validation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid third-party employee-data service.

Mitigation: Confirm pricing and obtain explicit user approval before each fee-incurring query.

Risk: The API key is stored in a local plaintext environment file.

Mitigation: Restrict file access, avoid printing the environment file, and rotate the key if it may have been exposed.

Risk: Error reports may include sensitive personal or business context.

Mitigation: Review and redact raw personal, business-sensitive, or secret data before submitting an error report.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-employee)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Employee List API Reference](references/company-employee-list-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paginated employee records, fee metadata, and request IDs returned by the API.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
