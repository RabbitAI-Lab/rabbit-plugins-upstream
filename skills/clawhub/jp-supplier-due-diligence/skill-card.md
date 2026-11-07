## Description:

Run a pre-payment supplier and counterparty check with JPVerify: combine Japanese corporate-number, qualified-invoice (T-number) and address evidence for a supplier, add FSA licence and EDINET checks when relevant, and for foreign counterparties check UK Companies House, EU VAT (VIES), Peppol participant IDs and SEC EDGAR filings. Use when a task involves onboarding a vendor, approving an invoice for payment, checking a vendor master in bulk, or deciding whether a counterparty needs manual review. Paid per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Accounts payable, procurement, and compliance teams can use this skill to gather public registry evidence when onboarding a supplier or reviewing an invoice or counterparty. It summarizes identity matches, conflicts, coverage, and next steps for a human decision.

### Deployment Geography for Use:

Global, with checks covering Japan and selected UK, EU, and US public registries.

## Known Risks and Mitigations:

Risk: Supplier identifiers or documents may be sent to JPVerify for external checks.

Mitigation: Use only information the user is entitled to process, minimize personal data, and confirm the user is comfortable with the external service.

Risk: Paid API calls can incur per-call charges, including for batch checks.

Mitigation: Check the stated price and total call count before proceeding; obtain user approval for batch calls or plans over $0.50.

Risk: Registry coverage can be incomplete, so an inconclusive or not-found result may be mistaken for a definitive finding.

Mitigation: Show coverage, freshness, conflicts, and source dates, and send ambiguous or insufficient-coverage cases for human review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/japanverify/skills/jp-supplier-due-diligence)
- [JPVerify endpoint guide](artifact/references/endpoints.md)
- [JPVerify request examples](artifact/references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text, Markdown, API calls]

**Output Format:** [Markdown evidence summary, with optional API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One evidence block per counterparty, covering decision signal, supporting evidence, and next actions.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
