## Description:

Recognizes supported financial and trade document images or PDFs with SCNet OCR and returns structured extracted fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to submit local financial or trade document files to SCNet OCR and receive structured JSON fields for downstream review or workflow automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive financial document images or PDFs may be sent to SCNet's remote OCR service.

Mitigation: Use only files approved for SCNet processing, confirm each local file path before execution, and avoid regulated or confidential records unless SCNet has been approved for that data.

Risk: The skill requires an SCNet API key for remote OCR requests.

Mitigation: Store SCNET_API_KEY in a protected local config file or environment variable and do not paste the key into chat.

Risk: Users may not notice the remote-upload behavior before submitting a financial document.

Mitigation: Present a clear consent check or operator review step before sending documents to the remote OCR service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/financial-bill-ocr)
- [Sugon-Scnet OCR API Docs](references/api-docs.md)
- [Financial OCR Field Summary](assets/templates/fields-summary.md)
- [SCNet website](https://www.scnet.cn)
- [SCNet OCR API endpoint](https://api.scnet.cn/api/llm/v1/ocr/recognize)

## Skill Output:

**Output Type(s):** [json, text]

**Output Format:** [Structured JSON emitted to standard output; errors are plain text messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ocrType and local filePath; response fields vary by document type.]

## Skill Version(s):

1.0.1 (source: frontmatter, skill.yaml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
