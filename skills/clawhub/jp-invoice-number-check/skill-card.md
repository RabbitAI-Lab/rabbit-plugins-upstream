## Description:

Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号, インボイス登録番号) against the National Tax Agency registry with JPVerify, and compare an invoice issuer's name and address with the registered record. Use when a task involves verifying a T-number, checking whether a Japanese supplier can issue qualified invoices, confirming who issued a Japanese invoice, or matching an invoice to a supplier's expected T-number or corporate number from master data (AP / vendor checks). Paid per call (API key credits or x402).

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Accounts payable and vendor teams use this skill to check Japanese T-number registration and compare invoice issuer details with registry records or supplier master data. It provides registry evidence for review and does not make a payment-approval or tax-deduction decision.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Invoice fields or documents may be sent to the external JPVerify API.

Mitigation: Confirm the user is comfortable sending the information and send only data they are entitled to process.

Risk: Successful checks incur per-call charges, and x402 calls can spend wallet funds.

Mitigation: Use available API-key credits or make wallet payments only within a user-approved budget.

## Reference(s):

- [references/endpoints.md](references/endpoints.md)
- [references/examples.md](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Concise text summary of registry and issuer-match results; source API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include registration status, registered name and dates, comparison evidence, and next steps. Avoid repeating personal details unless requested.]

## Skill Version(s):

1.0.9 (source: SKILL.md and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
