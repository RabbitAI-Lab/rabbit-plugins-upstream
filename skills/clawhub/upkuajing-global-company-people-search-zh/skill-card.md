## Description:

Searches global company and people data to help trade, export, purchasing, and B2B sales teams find companies, decision makers, contact details, and supplier or prospect leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as exporters, B2B sales teams, purchasing agents, and market researchers use this skill to search for overseas companies and contacts, retrieve company or person details, and obtain contact channels for authorized lead generation and supplier discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve personal contact information for people and companies.

Mitigation: Use it only for lawful, authorized outreach or research, and review any returned contact data before storing, sharing, or acting on it.

Risk: Search, detail, contact, account, and recharge actions may create paid API activity.

Mitigation: Confirm the intended query size, ID count, and pricing before running paid operations, and check account balance or pricing when cost is unclear.

Risk: The API key may be stored in a plaintext local .env file.

Mitigation: Prefer a protected environment variable when possible, restrict access to ~/.upkuajing/.env, and avoid displaying or sharing that file.

Risk: Search results may be written to local JSONL files that can contain sensitive business or personal data.

Mitigation: Review local task result files for sensitive data, limit access to generated files, and remove result files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-global-company-people-search-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company list API reference](references/company-list-api.md)
- [Human list API reference](references/human-list-api.md)
- [Company detail API reference](references/company-detail-api.md)
- [Human detail API reference](references/human-detail-api.md)
- [Contact API reference](references/contact-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSONL result files for search tasks and may return task IDs, request IDs, fee summaries, and file paths.]

## Skill Version(s):

1.0.10 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
