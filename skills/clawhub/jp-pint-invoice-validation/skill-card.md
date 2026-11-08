## Description:

Validate Japanese JP PINT 1.1.3 UBL invoice XML against UBL and Peppol rules, with an optional check of the seller’s qualified-invoice number in Japan’s NTA registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and accounting teams use the skill to validate JP PINT e-invoice XML before sending, accepting it into accounting, or paying it. It can also return rule-level errors and optionally check the seller’s qualified-invoice number against Japan’s NTA registry.

### Deployment Geography for Use:

Global; for Japanese JP PINT invoices.

## Known Risks and Mitigations:

Risk: Complete invoice XML is sent to an external validation service.

Mitigation: Submit only invoices the user is authorized to share, and consider the service’s data-handling terms before sending them.

Risk: The security analysis is incomplete because some references were unresolved.

Mitigation: Resolve or review those references before relying on the scanner assessment.

## Reference(s):

- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [JP PINT validation endpoint](https://api.jpverify.com/v1/invoices/validate-jp-pint)
- [Endpoint details](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured validation result with a concise text explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes document validity and separate workflow decision and trust signals; optional NTA registry evidence.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
