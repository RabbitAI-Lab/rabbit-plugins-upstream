## Description:

Commercial Invoice OCR extracts buyer and seller details, invoice totals, invoice numbers, unit prices, and international trade terms from commercial invoice files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit local commercial invoice image, PDF, or archive files to Scnet's OCR API and receive structured invoice fields as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Potentially sensitive invoice files are uploaded to Scnet's external OCR service without a strong user-confirmation or privacy boundary.

Mitigation: Confirm the exact file path before invocation and avoid submitting confidential or regulated documents unless Scnet is approved for that data.

Risk: The skill requires an API key for Scnet's OCR service.

Mitigation: Use a dedicated API key, keep config/.env access restricted, and rotate the key if it may have been exposed.

## Reference(s):

- [Server-resolved source repository](https://github.com/SCNet-sugon/commercial_invoice_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/commercial-invoice-ocr)
- [Sugon-Scnet OCR API docs summary](references/api-docs.md)
- [Commercial invoice fields summary](assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [JSON on standard output, with text error messages for failures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the selected file to Scnet's OCR API; retries rate limits up to 3 times.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
