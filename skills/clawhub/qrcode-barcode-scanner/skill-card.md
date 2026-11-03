## Description:

Scan QR codes, barcodes and supported 2D codes from local images, and inspect decoded content and measured QR quality diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qrcode-ai-com](https://clawhub.ai/user/qrcode-ai-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to inspect a selected local image, review decoded QR or barcode content and QR quality measurements, and compare identifiers with expected values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately downloaded native scanner engine was not inspected in this review.

Mitigation: Review and trust the exact engine package and version before installing it.

Risk: Decoded links or commands may contain untrusted content.

Mitigation: Review decoded content as data and do not open links or execute commands automatically.

Risk: A mixed image can contain a barcode that this engine release does not report.

Mitigation: Do not treat a missing barcode in a mixed-image report as proof of absence; verify expected symbols separately.

## Reference(s):

- [QR Code AI](https://qrcode-ai.com)
- [Engine 0.10.0 report contract](https://github.com/qrcode-ai-com/qrcode-barcode-scanner/blob/v0.10.0/spec/01-report.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON scan reports with decoded content and QR quality diagnostics, plus concise usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports preserve detection and scan-status details; QR raw payload bytes are represented in base64.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
