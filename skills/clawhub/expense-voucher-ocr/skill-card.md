## Description:

Recognizes common enterprise reimbursement vouchers and financial tickets through the Sugon-Scnet OCR API and returns structured extraction results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Employees, finance teams, and agent operators use this skill to extract structured fields from invoices, travel tickets, medical receipts, tax payment documents, and other reimbursement vouchers after the user explicitly provides a local file path for OCR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reimbursement documents are transmitted to Scnet for OCR and may contain personal, financial, travel, tax, or medical information.

Mitigation: Use the skill only for files approved for external processing, avoid secrets or regulated data, and review Scnet privacy and retention terms before use.

Risk: The skill requires a Scnet API key for authenticated OCR calls.

Mitigation: Store SCNET_API_KEY in an environment variable or local configuration file with restricted permissions, and do not paste the key into chat or commit it to source control.

Risk: OCR calls may hit Scnet rate limits when many files are processed at once.

Mitigation: Run OCR requests serially, honor retry guidance for 429 responses, and reduce call frequency if rate limiting continues.

## Reference(s):

- [Sugon-Scnet OCR API documentation summary](references/api-docs.md)
- [Financial voucher field summary](assets/templates/fields-summary.md)
- [Scnet official site](https://www.scnet.cn)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/expense-voucher-ocr)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [JSON array written to standard output, with friendly text errors on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Scnet OCR API response data field and removes per-item confidence values before printing.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
