## Description:

Extracts Japanese invoice, receipt, and business-card data into structured JSON, checks dates, tax, totals, and registration numbers, and can verify issuers against Japanese public registries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

Developers and business teams use this skill to extract structured fields from Japanese invoices, receipts, and business cards, with optional issuer checks against Japanese public registries. It is suited to workflows that need OCR results together with validation status and explicit review signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text, images, and business-card details may be sent to JPVerify for processing.

Mitigation: Confirm the user is entitled to share the data and that external processing is acceptable before making a call.

Risk: OCR-only fields may be inaccurate; the security scan reports medium confidence and partial Skillspector coverage.

Mitigation: Treat OCR-only values as unconfirmed and send ambiguous results or results marked for manual review to a human.

Risk: Successful service calls incur per-call charges.

Mitigation: Select the endpoint that fits the task and follow the skill's approval rule for batches or total charges above $0.50.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/japanverify/skills/jp-business-document-ocr)
- [Endpoint guide](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON containing extracted document fields, validation statuses, and manual-review signals, with concise review guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [OCR-only values are unconfirmed; card-printed and registry-enriched values remain separate.]

## Skill Version(s):

1.0.1 (source: release evidence; confirmed by artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
