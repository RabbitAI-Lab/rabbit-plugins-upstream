## Description:

Recognizes medical inpatient invoices and medical expense settlement forms after the user provides a local file path and confirms upload to the Scnet OCR API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit explicitly selected medical invoice or settlement document files to Scnet OCR and receive structured field extraction for reimbursement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads medical documents that may contain PHI/PII to Scnet OCR.

Mitigation: Use only with intentionally selected files, informed user consent, and a valid legal or policy basis for third-party OCR processing.

Risk: The Scnet API key is a sensitive credential.

Mitigation: Store SCNET_API_KEY in config/.env or an environment variable with restricted access, and do not paste the key into chat.

Risk: OCR output can contain sensitive identifiers, diagnoses, insurance details, and payment information.

Mitigation: Limit access to results and redact sensitive fields before sharing, forwarding, or publishing extracted data.

## Reference(s):

- [Sugon-Scnet OCR API Docs](references/api-docs.md)
- [OCR Field Summary](assets/templates/fields-summary.md)
- [Scnet Service Website](https://www.scnet.cn)
- [ClawHub Skill Page](https://clawhub.ai/scnet-sugon/skills/medical-invoice-scene-ocr)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON OCR result arrays on stdout, with human-readable warnings and error messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OCR type and local file path; the selected file is uploaded to Scnet OCR for processing.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter and skill.yaml state 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
