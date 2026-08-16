## Description:

Recognizes only birth medical certificates and extracts newborn, birth, parent, medical institution, issue date, and certificate number fields using Scnet's remote OCR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agents use this skill when a user explicitly asks to extract structured fields from a birth medical certificate image. It should not be used for general OCR or for other document types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Birth medical certificate images contain highly sensitive personal and medical information and are sent to Scnet's remote OCR service.

Mitigation: Use the skill only when authorized to process the document, review Scnet's privacy and retention terms, and delete local document copies when no longer needed.

Risk: The Scnet API key could be exposed if pasted into chat or stored with broad local permissions.

Mitigation: Keep the API key in the skill-local config with restrictive permissions and do not paste credentials into conversations.

Risk: Using the skill for general OCR or other document types can create unsupported data handling and accuracy expectations.

Mitigation: Limit use to explicit birth medical certificate requests and the BIRTH_CERTIFICATE OCR type.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/birth-medical-cert-ocr)
- [Sugon-Scnet OCR API docs summary](references/api-docs.md)
- [Birth certificate field summary](assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)
- [Scnet OCR API endpoint](https://api.scnet.cn/api/llm/v1/ocr/recognize)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON array on stdout with friendly text errors on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the API data array after removing confidence fields; supports only the BIRTH_CERTIFICATE OCR type.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter, skill.yaml, ClawHub release metadata, CHANGELOG released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
