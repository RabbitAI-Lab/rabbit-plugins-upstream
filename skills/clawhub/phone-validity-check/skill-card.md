## Description:

Verify phone-number validity, number type, and WhatsApp registration status through the Upkuajing Open Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales teams, recruiters, traders, exporters, and CRM operators use this skill to validate contact phone numbers before outreach, screening, or supplier and buyer verification. It helps reduce invalid contacts and identify mobile, landline, and WhatsApp registration status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone numbers are sent to the Upkuajing/Open Platform API for validation.

Mitigation: Use the skill only when sharing those phone numbers with the remote API is acceptable for the relevant privacy, consent, and business requirements.

Risk: Validation calls are paid API operations and may require account top-up.

Mitigation: Confirm fee-incurring operations before execution, check current pricing through the documented pricing flow, and review top-up payment URLs before opening or paying.

Risk: The skill uses UPKUAJING_API_KEY from the environment or ~/.upkuajing/.env.

Mitigation: Keep the API key private, restrict permissions on ~/.upkuajing/.env where possible, and rotate the key if it may have been exposed.

Risk: Optional error reporting can send troubleshooting context related to failed API calls.

Mitigation: Review error-report context before submission and report only abnormal skill-call failures, not normal business conditions such as invalid keys, insufficient balance, or parameter errors.

Risk: Optional API logging can write request and response data under ~/.upkuajing/logs if enabled.

Mitigation: Leave API logging disabled unless needed for troubleshooting, and protect or remove local logs that may contain phone numbers or response details.

## Reference(s):

- [Phone Validity API](references/phone-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON results and concise Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns total count, per-number validation results, fee and balance information, and requestId when available.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
