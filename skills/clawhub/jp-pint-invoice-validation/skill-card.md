## Description:

Validate Japanese Peppol e-invoices (JP PINT 1.1.3 UBL Invoice XML) with JPVerify against the official OASIS UBL 2.1 XSD and OpenPeppol JP PINT Schematron, optionally checking the seller's qualified-invoice T-number in the National Tax Agency registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance teams use this skill to validate JP PINT UBL invoice XML before sending it, accepting it into accounting, or paying it. They can optionally check the seller's qualified-invoice T-number in the National Tax Agency registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending a complete invoice to the validation service may disclose information in that invoice; scan evidence notes that the full-invoice upload lacks a privacy warning.

Mitigation: Before sending invoice XML, confirm you are permitted to share it with JPVerify and are comfortable with the provider's data handling.

Risk: The security scan had incomplete reference checks, so its benign, medium-confidence verdict does not establish complete coverage.

Mitigation: Review the service and references relevant to your use before relying on the validation workflow.

## Reference(s):

- [JP PINT Invoice Validation on ClawHub](https://clawhub.ai/japanverify/skills/jp-pint-invoice-validation)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)

## Skill Output:

**Output Type(s):** [API Calls, Code, Shell commands, Guidance]

**Output Format:** [Markdown instructions with HTTP, shell, and Python examples; JSON validation responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results distinguish schema and rule validity from workflow signals and are validation evidence, not legal, tax, or Peppol certification.]

## Skill Version(s):

1.2.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
