## Description:

Extract structured fields from Japanese invoices, receipts, and business cards, with local date, tax, total, and T-number checks and optional National Tax Agency issuer verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to extract structured data from Japanese invoices, receipts, and business cards, check document fields, and optionally verify an issuer against National Tax Agency registries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document images and text, including personal details on business cards, are sent to an external API.

Mitigation: Send only information the user is entitled to process, avoid unnecessary personal details, and review JPVerify's privacy terms before use.

Risk: The security scan has partial coverage, so its benign verdict does not cover every local reference.

Mitigation: Review the unresolved references and API integration before deployment.

## Reference(s):

- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON fields with a concise text summary and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports validation status and fields needing manual review; OCR-only values remain unconfirmed.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
