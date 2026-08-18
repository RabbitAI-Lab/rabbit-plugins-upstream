## Description:

Extracts structured international draft OCR fields from user-selected images, PDFs, or archives after explicit consent to upload the file to Scnet's OCR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to extract payee, drawee, amount, date, bank, letter-of-credit, and draft-number fields from international bill documents. It is intended for workflows where the user is authorized to send the selected document to Scnet's cloud OCR service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected bill images, PDFs, or archives may contain sensitive financial or personal information and are uploaded to Scnet's cloud OCR service.

Mitigation: Use the skill only for documents the user is authorized to disclose, and require explicit upload consent before execution.

Risk: Uploaded documents may be subject to Scnet retention, compliance, or cross-border processing terms.

Mitigation: Review Scnet's service terms and organizational compliance requirements before using the skill on regulated financial data.

Risk: The skill requires an API key for Scnet's OCR service.

Mitigation: Store the API key in environment or local configuration with restricted file permissions, and do not paste credentials into chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scnet-sugon/skills/international-draft-ocr)
- [Sugon-Scnet OCR API Documentation Summary](references/api-docs.md)
- [International Bill Field Summary](assets/templates/fields-summary.md)
- [Scnet Service Website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON OCR result data on success, with plain-text error guidance on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One OCR request per invocation; returned fields depend on the INTERNATIONAL_BILL recognition type.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
