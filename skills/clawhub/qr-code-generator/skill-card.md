## Description: <br>
Creates customizable QR codes for URLs, text, WiFi credentials, vCards, email, phone, SMS, location coordinates, calendar events, and custom data, with batch generation and PNG, SVG, PDF, EPS, or terminal output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anisafifi](https://clawhub.ai/user/anisafifi) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Developers and external users use this skill to generate QR code assets and command-line workflows for links, contact details, WiFi sharing, event details, and bulk QR-code production. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated QR codes can disclose WiFi passwords, private contact details, or other sensitive data to anyone who can view or scan them. <br>
Mitigation: Treat generated QR codes as public artifacts; avoid long-lived secrets and distribute sensitive codes only through controlled channels. <br>
Risk: Single-code runs may print encoded content to terminal output or agent logs. <br>
Mitigation: Avoid encoding secrets in logged sessions, and clear or restrict logs when commands include private data. <br>
Risk: The tool depends on local Python image libraries, including Pillow. <br>
Mitigation: Install dependencies in a virtual environment and keep Pillow, qrcode, and segno current. <br>
Risk: Low contrast, small size, or large embedded logos can make generated QR codes unreliable to scan. <br>
Mitigation: Use sufficient contrast and quiet zone, choose higher error correction for print or logos, and test scan before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anisafifi/skills/qr-code-generator) <br>
- [QR Code Generator README](references/readme.md) <br>
- [qrcode Python package](https://pypi.org/project/qrcode/) <br>
- [segno Python package](https://pypi.org/project/segno/) <br>
- [Pillow documentation](https://python-pillow.org/) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated QR code files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files may be PNG, SVG, PDF, EPS, or terminal ASCII output; batch mode can create multiple files from TXT, CSV, or JSON input.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and references/readme.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
