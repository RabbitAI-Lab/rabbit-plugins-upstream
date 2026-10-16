## Description:

Helps agents find and check Brazilian companies using Radar CNPJ's company records, public-data searches, and due-diligence tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers use this skill to look up Brazilian companies, review public risk indicators, find potential suppliers, and assess company counts by activity and location.

### Deployment Geography for Use:

Global (Brazilian company data)

## Known Risks and Mitigations:

Risk: Company identifiers, lookup terms, and search filters may be sent to Radar CNPJ.

Mitigation: Share only information needed for the requested lookup and inform users before sending sensitive queries.

Risk: Paid features may use prepaid credits and expose credential tokens if mishandled.

Mitigation: Confirm the current price and get user approval before paid calls; keep credit tokens out of responses and logs.

Risk: Public-record dates and cached data may not reflect current company status; partner details can be personal data.

Mitigation: Report source dates, avoid treating results as official certificates, and use personal details only for the user's stated legitimate purpose.

## Reference(s):

- [Radar CNPJ on ClawHub](https://clawhub.ai/wrpbr/skills/radar-cnpj)
- [Radar CNPJ API reference](https://radar-cnpj.com/llms-full.txt)
- [Radar CNPJ API routes](https://radar-cnpj.com/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries of company records, searches, and risk indicators]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include source dates and distinguish registered-company counts from demand estimates.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
