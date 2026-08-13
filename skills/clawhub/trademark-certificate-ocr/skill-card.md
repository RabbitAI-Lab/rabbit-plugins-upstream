## Description:

Recognizes trademark registration certificates with the Sugon-Scnet OCR API and returns structured JSON fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to send local trademark registration certificate images, PDFs, or supported archives to Scnet OCR and receive extracted certificate fields as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trademark certificate images or PDFs are uploaded to Scnet's OCR API.

Mitigation: Use the skill only for documents that may be shared with Scnet for OCR, and avoid unrelated sensitive documents.

Risk: Misconfigured credentials or API base URL could expose requests or keys.

Mitigation: Store SCNET_API_KEY in config/.env with restrictive permissions and verify SCNET_API_BASE before processing confidential files.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/SCNet-sugon/trademark_certificate_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/trademark-certificate-ocr)
- [Sugon-Scnet OCR API docs](artifact/references/api-docs.md)
- [Trademark registration certificate fields](artifact/assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [JSON emitted to standard output with friendly error messages on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY; accepts ocrType and a local file path; removes confidence from returned result items before printing.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
