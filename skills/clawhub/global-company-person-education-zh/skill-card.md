## Description:

Retrieves a person's education history from UpKuajing's global company database by person ID, including schools, degrees, majors, minors, GPA, summaries, and pagination metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, human resources teams, hiring managers, and other business users can use this skill to retrieve education records for a known person ID and support candidate screening, background verification, talent assessment, or customer-profile enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The education lookup and pagination calls use a paid UpKuajing API account.

Mitigation: Confirm pricing and obtain explicit user approval before each paid lookup or additional page request.

Risk: The skill may store or read an UpKuajing API key from ~/.upkuajing/.env.

Mitigation: Prefer manual API key management, restrict access to the key file, and avoid sharing the key in chat or logs.

Risk: Recharge helpers can create payment links when the account balance is insufficient.

Mitigation: Review any recharge link and account context before approving payment or asking a user to pay.

Risk: Confirmed error reports send troubleshooting context to the provider.

Mitigation: Ask for confirmation before reporting and avoid including unnecessary personal, credential, or candidate-sensitive details.

Risk: The artifact includes automatic version-check behavior during API requests.

Mitigation: Review network behavior before installation in restricted environments and disable or isolate the skill if update checks are not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-education-zh)
- [UpKuajing Homepage](https://www.upkuajing.com)
- [UpKuajing Developer Platform](https://developer.upkuajing.com/)
- [UpKuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Person Education List API Reference](artifact/references/person-education-list-api.md)
- [Skill Error Report API Reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with direct shell commands and formatted JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup responses may include paginated education records, fee information, and request identifiers.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
