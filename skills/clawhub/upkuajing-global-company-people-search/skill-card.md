## Description:

Search global companies and professional contacts for cross-border B2B lead generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External B2B exporters, sourcing agents, and sales teams use this skill to find companies, professional contacts, business credentials, and contact channels for export lead generation, supplier discovery, and company background verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve personal contact channels and business lead data.

Mitigation: Use only where there is a lawful basis for contact-data processing, limit searches to necessary records, and protect or delete generated result files when no longer needed.

Risk: The skill can make paid API calls.

Mitigation: Confirm expected fee counts before paid searches or enrichment calls, and use the vendor pricing or account information flow when cost is unclear.

Risk: The skill can store an API key in a plaintext home-directory file.

Mitigation: Prefer protected environment-variable storage where possible, restrict access to the credential file, and remove unused keys.

Risk: The skill can send diagnostic reports to the vendor after confirmation.

Mitigation: Do not include raw request data, response data, or sensitive personal information in diagnostic context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-global-company-people-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company List API Reference](references/company-list-api.md)
- [Company Detail API Reference](references/company-detail-api.md)
- [People List API Reference](references/human-list-api.md)
- [People Detail API Reference](references/human-detail-api.md)
- [Contact API Reference](references/contact-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries; list searches may also produce JSONL result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls can retrieve and persist company and personal contact data.]

## Skill Version(s):

1.0.10 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
