## Description:

Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号, インボイス登録番号) against the National Tax Agency registry with JPVerify, check that a T-number belongs to the issuer name (and address) on an invoice and that the issuer was registered — not cancelled or expired — on the invoice date, and match an invoice to a supplier's expected T-number or corporate number from master data (AP / vendor checks). Use when a task involves verifying a T-number, confirming who issued a Japanese invoice and whether their registration covered the invoice date, or matching an invoice to supplier master data. Paid per call (API key credits or x402).

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and accounts-payable teams use this skill to check Japanese qualified-invoice registration numbers, compare invoice issuer names and addresses with registry records, confirm registration on an invoice date, and match the issuer against supplier master data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice-related information is sent to the external JPVerify service.

Mitigation: Send only fields needed for the check and only information the user is entitled to process; avoid unnecessary personal details.

Risk: Calls can consume prepaid API credits or make an x402 wallet payment.

Mitigation: Use an API key only when configured by the user, check costs before batches, and make x402 payments only within a user-approved budget.

## Reference(s):

- [JPVerify endpoints and pricing](artifact/references/endpoints.md)
- [JPVerify request examples](artifact/references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured registry check results with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results are returned per item in input order.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
