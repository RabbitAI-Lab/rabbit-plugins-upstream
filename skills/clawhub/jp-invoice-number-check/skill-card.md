## Description:

Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号, インボイス登録番号) against the National Tax Agency registry with JPVerify, and compare an invoice issuer's name and address with the registered record. Use when a task involves verifying a T-number, checking whether a Japanese supplier can issue qualified invoices, or confirming who issued a Japanese invoice. Paid per call (API key credits or x402).

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

External users can check whether a Japanese qualified-invoice T-number is registered and active, or compare the number and issuer name or address on an invoice with the registry. It can also check up to 10 numbers in one request.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Invoice identifiers and issuer details are sent to an external JPVerify API, and successful calls can incur per-call charges.

Mitigation: Use only invoice data the user is entitled to process, confirm the user is comfortable with the external API, and check the price and approved payment method before calling.

Risk: Registry results are a dated public-registry pre-check and may not settle an ambiguous issuer match or establish broader business risk.

Mitigation: Report the registry data-as-of date and comparison evidence; surface manual-review or ambiguous results for the user to decide, and do not present the check as KYB or legal, tax, or accounting advice.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/japanverify/skills/jp-invoice-number-check)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Concise text summary with structured registry and issuer-comparison results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports registration status, registered name, relevant dates, registry data-as-of date, and any name or address comparison results; supports up to 10 T-numbers per batch request.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
