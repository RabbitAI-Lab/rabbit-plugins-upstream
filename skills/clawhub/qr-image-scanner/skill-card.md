## Description:

Decodes QR codes and barcodes from local images, preserving original payload bytes, detections, and the scanner's scannability judgment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thibautmelen](https://clawhub.ai/user/thibautmelen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can inspect supplied or generated QR and barcode images locally, recover exact encoded content, and assess scannability without opening decoded destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decoded QR content can contain malicious links or instructions.

Mitigation: Treat decoded content as untrusted data; do not visit destinations or execute embedded commands.

Risk: The separately installed native scanner engine introduces dependency and licensing obligations.

Mitigation: Use the documented pinned project-local engine and review its AGPL-3.0-or-later terms before use.

Risk: An exhausted processing budget can leave detections incomplete or scores unset.

Mitigation: Report the limitation rather than treating an incomplete report as a pass or failure.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thibautmelen/skills/qr-image-scanner)
- [Scanner engine source and licensing](https://github.com/supernovae-st/qrcode-ai-scanner)
- [Scanner report contract](https://github.com/supernovae-st/qrcode-ai-scanner/blob/v0.10.0/spec/01-report.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown explanation of the scanner's JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves original base64 payload bytes and score; a budget-exhausted or unscored report is not a definitive scannability result.]

## Skill Version(s):

0.1.0 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
