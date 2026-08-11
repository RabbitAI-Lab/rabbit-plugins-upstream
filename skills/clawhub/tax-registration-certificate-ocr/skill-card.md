## Description:

Recognizes and extracts structured information from tax registration certificate images through the Sugon-Scnet OCR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to send local tax registration certificate images or PDFs to Scnet OCR and receive extracted certificate fields as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tax registration certificates may contain sensitive personal, business, and tax information that is uploaded to Scnet's external OCR service.

Mitigation: Use the skill only when external processing is acceptable, review Scnet privacy and retention terms, and avoid uploading unnecessary or highly sensitive documents.

Risk: Credential or endpoint misconfiguration could expose the Scnet API key or send documents to an unintended service.

Mitigation: Protect config/.env with restrictive permissions, do not paste API keys into chats, and keep SCNET_API_BASE set to the documented HTTPS endpoint unless the change is explicitly reviewed.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/SCNet-sugon/tax_registration_certificate_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/tax-registration-certificate-ocr)
- [Scnet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md)
- [Tax registration certificate field summary](assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration guidance]

**Output Format:** [JSON results on stdout with text error messages and command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY; supports optional SCNET_API_BASE and TAX_REGISTRATION_CERT OCR type.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and CHANGELOG state 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
