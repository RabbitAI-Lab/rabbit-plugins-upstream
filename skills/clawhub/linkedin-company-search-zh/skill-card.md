## Description:

Searches LinkedIn company data by company name, industry, company size, founding year, geography, and contact availability to support prospecting, market research, company profiling, and account-based sales workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, marketers, and B2B lead builders use this skill to discover LinkedIn company profiles, research target accounts, and enrich company data for prospecting, market research, competitor analysis, and account-based sales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a disclosed paid API integration, so searches can incur charges.

Mitigation: Confirm pricing and expected call counts before paid searches, and require explicit user approval for cost-incurring operations.

Risk: The API key may be stored in plaintext in ~/.upkuajing/.env.

Mitigation: Restrict access to the credential file, avoid sharing its contents, and rotate the key if exposure is suspected.

Risk: Optional error reports could include sensitive request context or customer data if submitted without review.

Mitigation: Ask for user confirmation before reporting errors and redact secrets, customer data, and unnecessary request details.

Risk: Search results can be written to local result files containing company or contact-related data.

Mitigation: Handle result files according to the user's data handling requirements and delete or restrict access when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-company-search-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn company list API reference](references/linkedin-company-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands plus JSON summaries and JSONL result files from API-backed searches]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches require an Upkuajing API key and may produce local task result files; API use may incur fees.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
