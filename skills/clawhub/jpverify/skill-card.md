## Description:

JPVerify: Japan business data for AI agents — verify Japanese companies (法人番号), qualified-invoice T-numbers (インボイス), invoice issuers and suppliers; OCR Japanese invoices, receipts and business cards; normalize and validate Japanese addresses; plus JP PINT e-invoice validation, EU VAT/Peppol, UK and SEC cross-border checks. Use when a task involves Japanese business documents or data and you need to pick the right check. Paid per call (API key credits or x402); a free guide tool is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations teams use this skill to choose JPVerify calls for Japanese company, invoice, receipt, business-card, address, and supplier checks, with selected cross-border checks. It helps interpret returned evidence and review signals before a human makes a decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice, receipt, business-card, and other task data may be sent to JPVerify during external API calls; full invoices can contain sensitive information.

Mitigation: Send only the information the task requires and only documents or personal data the user is entitled to process. Review JPVerify's privacy information before sharing sensitive documents.

Risk: ClawScan reports partial analysis, and OCR or registry results may be incomplete or ambiguous.

Mitigation: Treat results as public-registry pre-checks, inspect source dates and review signals, and route ambiguous or consequential cases to human review.

Risk: Users could mistake a registry pre-check or risk flags for a complete KYB, legal, tax, or accounting determination.

Mitigation: Present the result within its stated coverage and limitations, and do not use it as a substitute for the relevant professional or compliance review.

## Reference(s):

- [JPVerify ClawHub release](https://clawhub.ai/japanverify/skills/jpverify)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured API results with concise routing and interpretation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include registry evidence, extracted document fields, validation status, confidence, and review signals; paid API calls are charged per successful call.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
