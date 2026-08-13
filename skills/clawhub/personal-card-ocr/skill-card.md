## Description:

Extracts structured OCR data from user-provided images of personal documents by sending the selected file to Scnet after explicit user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to extract fields from user-selected identity, financial, travel, education, vehicle, and property document images. It is intended for cases where the user is authorized to upload the document and agrees to third-party OCR processing by Scnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected document images and extracted OCR data may contain highly sensitive personal, identity, or financial information and are sent to Scnet for processing.

Mitigation: Use only documents the user is authorized to upload, obtain explicit consent before processing, and send only the minimum document image needed for the task.

Risk: The Scnet API credential could be exposed if pasted into chat or stored with broad file permissions.

Mitigation: Keep SCNET_API_KEY out of chat, store it in a protected environment variable or config/.env file, and restrict config file permissions.

Risk: Changing SCNET_API_BASE can redirect sensitive documents and credentials to an untrusted endpoint.

Mitigation: Leave SCNET_API_BASE at the default unless the replacement endpoint is deliberately trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/personal-card-ocr)
- [Scnet service site](https://www.scnet.cn)
- [Sugon-Scnet OCR API docs](artifact/references/api-docs.md)
- [OCR output fields summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON on stdout with text warnings and error messages on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Scnet OCR response data for a single requested file path and OCR type; field names vary by document type.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
