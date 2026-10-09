## Description:

Helps agents check Brazilian company records, search companies, assess suppliers, and monitor CNPJ changes through Radar CNPJ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users can research Brazilian companies, screen suppliers, search by activity or location, and track changes to CNPJ records using public data.

### Deployment Geography for Use:

Global (Brazilian company data)

## Known Risks and Mitigations:

Risk: Company queries are sent to the external Radar CNPJ service.

Mitigation: Inform users where queries go and send only information needed for the requested check.

Risk: Paid lookups and credit tokens can spend a user's balance or expose credentials.

Mitigation: Check current prices, obtain approval for the specific lookup and amount, and keep tokens out of files, logs, and responses.

Risk: Revealed partner names, phone numbers, and emails are personal data.

Mitigation: Get user approval before revealing them and use them only for the stated legitimate purpose.

## Reference(s):

- [Radar CNPJ API discovery](https://radar-cnpj.com/api/)
- [Radar CNPJ full API reference](https://radar-cnpj.com/llms-full.txt)
- [Radar CNPJ skill release](https://clawhub.ai/wrpbr/skills/radar-cnpj)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company findings should include source dates; counts reflect registered companies, not demand or revenue.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
