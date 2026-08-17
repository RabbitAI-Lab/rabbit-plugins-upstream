## Description:

Extracts core bill-of-lading information, including voyage and port details, shipper and consignee names, cargo quantity, bill of lading number, and carrier data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and operations teams use this skill to extract structured fields from bill-of-lading images, PDFs, or supported archives through Scnet's OCR API after confirming the document is approved for external upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected bill-of-lading files may contain commercial or personal information and are uploaded to Scnet's remote OCR service.

Mitigation: Confirm the user has permission to upload the exact file before running the skill, and disclose that the file will be sent to Scnet for OCR processing.

Risk: The Scnet API key can be exposed if pasted into chat or stored with loose permissions.

Mitigation: Keep SCNET_API_KEY in config/.env with restrictive file permissions, and do not paste the key into chat.

## Reference(s):

- [Sugon-Scnet OCR API documentation summary](references/api-docs.md)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/bill-of-lading-ocr)
- [Scnet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [text, json]

**Output Format:** [JSON recognition results printed to stdout, with friendly text errors on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include recognized bill-of-lading fields and confidence values returned by the OCR API.]

## Skill Version(s):

1.0.2 (source: server evidence, SKILL.md frontmatter, skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
