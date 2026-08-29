## Description:

Verify phone numbers, WhatsApp status, email addresses, and website domains through the UpKuaJing Open Platform API for contact-list cleansing and B2B prospect validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales teams, recruiters, exporters, and agents use this skill to validate phone numbers, WhatsApp registration status, email addresses, and business domains before outreach or lead import. It supports contact-data cleansing, bounce-rate reduction, candidate screening, and supplier or buyer verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone numbers, email addresses, domains, and optional error context are sent to the UpKuaJing service.

Mitigation: Use the skill only for records that may be shared with UpKuaJing, and avoid including sensitive customer details in optional error reports.

Risk: The API key may be stored in ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, restrict local file access, and remove or rotate the key when it is no longer needed.

Risk: Validity-check API calls incur fees.

Mitigation: Confirm current pricing and obtain explicit user approval before running paid checks.

Risk: Bulk validation can expose more contact data than intended.

Mitigation: Review input lists before execution and submit only the minimum records needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-contact-info-validity-check)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Phone validity API reference](artifact/references/phone-api.md)
- [Email validity API reference](artifact/references/email-api.md)
- [Domain validity API reference](artifact/references/domain-api.md)
- [Skill error report API reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; validation API calls return result lists, fee details, and request IDs.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
