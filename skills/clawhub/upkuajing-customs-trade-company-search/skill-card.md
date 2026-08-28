## Description:

Access global customs trade data from more than 220 countries to search import-export records by company, HS code, product, and trade activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade, sales, and export teams use this skill to find potential buyers or suppliers, review historical shipment records, and enrich selected companies with details or contact information through the UpKuaJing API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid third-party trade-data API and list searches or enrichment requests may incur fees.

Mitigation: Confirm expected call counts and current pricing before paid lookups, especially for batch or paginated searches.

Risk: The UpKuaJing API key may be stored in a local ~/.upkuajing/.env file.

Mitigation: Store the key only on trusted machines, restrict file access, and rotate the key if it may have been exposed.

Risk: Company contact details and shipment intelligence can be retrieved and saved locally.

Mitigation: Handle exported results as sensitive business data and delete or redact local files when they are no longer needed.

Risk: Error reports can include request context and troubleshooting details.

Mitigation: Review and redact sensitive details before approving any error report submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-customs-trade-company-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company Detail API Reference](references/company-detail-api.md)
- [Company List API Reference](references/company-list-api.md)
- [Contact Fetch API Reference](references/contact-fetch-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [Trade List API Reference](references/trade-list-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save query task metadata and result JSONL files locally for paginated searches.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
