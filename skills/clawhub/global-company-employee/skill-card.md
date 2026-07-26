## Description: <br>
Retrieve overseas employee profiles by company ID, including person identifiers and job titles, for recruitment and B2B lead-generation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead-generation specialists use this skill to retrieve employee lists for a known company ID and identify role-level contacts for talent mapping, organizational research, and decision-maker targeting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party employee-data API and each lookup can incur fees. <br>
Mitigation: Confirm pricing and obtain explicit user approval before running billable lookup or pagination requests. <br>
Risk: The API key may be stored in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Protect the local environment file, avoid sharing logs or terminal output containing credentials, and rotate the key if exposure is suspected. <br>
Risk: Employee profile data may be sensitive or regulated depending on jurisdiction and intended use. <br>
Mitigation: Use retrieved employee data only for lawful, appropriate workflows and avoid ambiguous or unauthorized lead-generation requests. <br>
Risk: The skill contacts UpKuaJing for lookup requests and version checks. <br>
Mitigation: Install only when outbound requests to UpKuaJing are acceptable for the operating environment. <br>


## Reference(s): <br>
- [Employee List API Reference](references/company-employee-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON responses with concise Markdown guidance and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a company ID, supports cursor-based pagination, and reports API fee information returned by the provider.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
