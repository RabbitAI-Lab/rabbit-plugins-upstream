## Description:

Searches Upkuajing customs trade records to find importers, exporters, buyers, suppliers, company details, and contact information by product, HS code, country, or company.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade, sales, sourcing, and market research teams use this skill to query customs trade data, identify B2B buyers and suppliers, inspect transaction records, and enrich selected companies with details or contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs an Upkuajing API key to make authenticated requests.

Mitigation: Set UPKUAJING_API_KEY through the agent or shell secret mechanism where possible, and avoid storing secrets in plaintext files.

Risk: Search, detail, contact, account, and recharge operations can involve paid API calls.

Mitigation: Confirm expected call counts or pricing with the user before running paid operations, especially batch searches or enrichment calls.

Risk: Generated search results are stored locally and may contain business, contact, or customer-relevant data.

Mitigation: Handle result files according to the user organization's data policy and remove unneeded local task data after use.

Risk: Optional error reports may include request or response context.

Mitigation: Review error report contents with the user before sending and exclude secrets, customer data, and unnecessary request or response details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-customs-trade-company-search-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Trade list API reference](references/trade-list-api.md)
- [Company list API reference](references/company-list-api.md)
- [Company detail API reference](references/company-detail-api.md)
- [Contact fetch API reference](references/contact-fetch-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, files, guidance]

**Output Format:** [Human-facing guidance plus JSON command output and JSONL result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scripts may create task metadata and result.jsonl files; paid API calls require user confirmation before execution.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
