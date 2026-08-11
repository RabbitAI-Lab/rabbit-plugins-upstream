## Description:

Recognizes structured fields from medical inpatient invoices and medical expense settlement documents through Scnet's OCR API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to send a local image or PDF of a medical inpatient invoice or medical expense settlement document to Scnet's OCR API and return structured fields for reimbursement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive medical and identity documents may be uploaded to Scnet's external OCR service without strong consent or privacy guidance.

Mitigation: Use only when authorized to process the documents; review Scnet privacy, retention, deletion, residency, and compliance terms; require explicit approval before each upload.

## Reference(s):

- [Server-resolved source repository](https://github.com/SCNet-sugon/medical_invoice_scene_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/medical-invoice-scene-ocr)
- [Scnet OCR API documentation](artifact/references/api-docs.md)
- [OCR field summary](artifact/assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [JSON, API Calls]

**Output Format:** [JSON printed to standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured OCR data from Scnet; confidence values may be removed by the wrapper before output.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
