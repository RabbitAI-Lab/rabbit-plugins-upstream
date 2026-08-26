## Description:

Searches global corporate personnel by name, company, industry, and profile URL through the UpKuaJing Open Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead-generation specialists use this skill to find global corporate contacts, source candidates, and enrich lead data from company-person records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive recruiting, sales, and customer contact data.

Mitigation: Review the skill before use in sensitive environments and limit submitted search inputs to data appropriate for the intended business purpose.

Risk: The API key is persisted in ~/.upkuajing/.env.

Mitigation: Use a dedicated low-privilege API key and check local file permissions before running the skill.

Risk: Search outputs can persist in task_data result files.

Mitigation: Periodically delete result files that are no longer needed and handle exported JSONL data according to the user's data-retention requirements.

Risk: Error reports may include operational context from failed API calls.

Mitigation: Avoid sending personal data in error reports and report only after explicit user confirmation.

## Reference(s):

- [Global Company Person List API](references/global-company-person-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-search)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance, shell command examples, and JSON or JSONL API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are written to task_data result files; API responses include task identifiers, fee information, and result file paths.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
