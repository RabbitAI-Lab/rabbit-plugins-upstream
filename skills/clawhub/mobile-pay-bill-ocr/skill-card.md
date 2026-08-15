## Description:

Recognizes Alipay and WeChat mobile payment bill screenshots when explicitly requested and extracts transaction time, merchant, amount, and payment direction into structured JSON data; it is not intended for general OCR or non-payment receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT License

## Use Case:

External users and developers use this skill to process local screenshots of mobile payment bills through Scnet's OCR service and receive structured transaction fields for payment record review or data entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment screenshots and extracted transaction details are sent to Scnet's remote OCR service.

Mitigation: Use the skill only when remote processing is acceptable, review Scnet's privacy and retention terms, and delete unneeded local or cloud copies of bill images after use.

Risk: Mobile payment bills can contain personal, financial, and social relationship information.

Mitigation: Avoid uploading bills that contain another person's personal information unless the user has permission, and limit use to the supported mobile payment bill scenario.

Risk: The skill requires a Scnet API key.

Mitigation: Store the API key in a dedicated environment variable or restricted config file, avoid pasting it into chat, rotate expired keys, and keep file permissions restrictive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/mobile-pay-bill-ocr)
- [Scnet website](https://www.scnet.cn)
- [Sugon-Scnet mobile payment bill OCR API summary](artifact/references/api-docs.md)
- [Mobile payment bill output fields](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON data on success; plain text error messages on failure.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Extracted fields include transaction amount, status, date, merchant, payment method, transaction number, merchant number, remarks, and refund number when returned by the OCR service.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter and skill.yaml report 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
