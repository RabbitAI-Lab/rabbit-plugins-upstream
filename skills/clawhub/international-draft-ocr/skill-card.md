## Description:

Extracts payer and payee details, currency and amount, maturity date, paying bank, and bill number from international draft images using SCNet OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and document-processing teams use this skill to run OCR on local international draft images, PDFs, or archives and receive structured fields for downstream review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads drafts, PDFs, images, or archives that may contain sensitive financial data to SCNet for OCR.

Mitigation: Use it only with authorization, verify SCNet privacy and retention terms, and avoid confidential banking or customer documents without explicit approval.

Risk: SCNET_API_KEY exposure could allow unauthorized use of the OCR service.

Mitigation: Store the API key in a protected local environment or config file, restrict file permissions, and do not paste credentials into chat.

Risk: OCR output for financial documents can be incomplete or inaccurate.

Mitigation: Review extracted fields before using them in operational, banking, or customer-facing workflows.

## Reference(s):

- [Server-resolved source repository](https://github.com/SCNet-sugon/international_draft_ocr)
- [ClawHub skill listing](https://clawhub.ai/scnet-sugon/skills/international-draft-ocr)
- [SCNet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API docs](artifact/references/api-docs.md)
- [International bill field summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, text]

**Output Format:** [Structured JSON emitted to stdout, with human-readable error text on failure.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OCR type and local file path; uses SCNET_API_KEY and optional SCNET_API_BASE configuration.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
