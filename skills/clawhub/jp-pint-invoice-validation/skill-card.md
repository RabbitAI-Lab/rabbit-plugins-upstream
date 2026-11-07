## Description:

Validate Japanese Peppol e-invoices (JP PINT 1.1.3 UBL Invoice XML) with JPVerify against the official OASIS UBL 2.1 XSD and OpenPeppol JP PINT Schematron, optionally checking the seller's qualified-invoice T-number in the National Tax Agency registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, accounting teams, and invoice recipients can validate a Japanese JP PINT 1.1.3 UBL invoice before sending it, accepting it into accounting, or paying it. The optional registry check provides a separate status for the seller's qualified-invoice T-number.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoices may contain personal, payment, or confidential business information that is sent to an external validation service.

Mitigation: Before sending an invoice, consider its contents and confirm that your organization permits sending it to the external service.

Risk: Security analysis is incomplete because some referenced materials could not be resolved.

Mitigation: Review the referenced JPVerify documentation and confirm that its service and data handling are acceptable for the invoice before use.

## Reference(s):

- [JPVerify API endpoint](https://api.jpverify.com/v1/invoices/validate-jp-pint)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoint details](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured validation response summarized in concise text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes document validity, rule-level errors, warnings, and optional registry evidence.]

## Skill Version(s):

1.0.1 (source: skill body and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
