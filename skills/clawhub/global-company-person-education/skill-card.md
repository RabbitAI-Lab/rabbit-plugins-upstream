## Description:

Verify overseas candidates' education history, including schools attended, degrees, majors, minors, and GPA, for HR background checks and hiring screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, HR teams, and hiring managers use this skill to query UpKuaJing person IDs for education records during pre-employment screening, background verification, and credential validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles candidate education data and account metadata through a third-party paid API.

Mitigation: Use only where UpKuaJing is approved for the organization's candidate-data workflow and confirm each fee-incurring query before execution.

Risk: The skill stores or reads the UpKuaJing API key from the user's environment or ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, restrict access to the local credential file, and avoid sharing account secrets in prompts or logs.

Risk: Optional error reporting can send request context to the provider for troubleshooting.

Mitigation: Submit error reports only after user confirmation and do not include candidate records or account secrets unless policy permits it.

## Reference(s):

- [Education History List API Reference](references/person-education-list-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require an UpKuaJing API key and may return paginated education records with fee and request identifiers.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
