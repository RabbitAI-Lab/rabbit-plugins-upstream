## Description:

Search companies from LinkedIn filtered by industry, size, founding year, geography, and contact-data availability, then return firmographic company results from the UpKuaJing Open Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, marketers, and B2B lead-generation specialists use this skill to find LinkedIn company profiles and enrich firmographic data for customer acquisition, market research, competitor analysis, and account-based sales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid third-party data provider and API calls can incur charges.

Mitigation: Confirm expected charges before paid searches, especially when query_count exceeds 20 or multiple calls are required.

Risk: The skill stores the UpKuaJing API key in a local plaintext file when the user chooses that setup path.

Mitigation: Prefer environment-variable storage where possible, restrict local file permissions, and rotate the API key if it may have been exposed.

Risk: Searches and optional diagnostics send query, request, and error-report data to UpKuaJing APIs.

Mitigation: Avoid submitting raw prompts, customer data, or sensitive context in search parameters or error reports, and confirm privacy and compliance obligations before using contact-data filters for outreach.

Risk: The skill performs an automatic remote version check during API requests.

Mitigation: Review outbound network behavior and allow the version-check endpoint only when it matches the deployment environment's network policy.

## Reference(s):

- [LinkedIn Company List API](references/linkedin-company-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with Python shell commands and JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are written to task data files and summarized with task ID, status, request ID, file path, fee, and account balance.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
