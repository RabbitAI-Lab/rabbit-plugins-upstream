## Description: <br>
Generates QR codes from text or URLs and decodes QR codes from image files, including screenshots, with PNG/JPG support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[omar-khaleel](https://clawhub.ai/user/omar-khaleel) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and users use this skill to create QR code images from text or URLs and to decode QR payloads from local image files or screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependencies installed from untrusted package sources could compromise the runtime environment. <br>
Mitigation: Install qrcode, Pillow, pyzbar, and zbar from trusted repositories, preferably inside a virtual environment. <br>
Risk: Generated QR files may overwrite existing files if the output path is chosen carelessly. <br>
Mitigation: Review output paths before generation and write to an intended directory. <br>
Risk: Decoded QR payloads may contain unsafe links or misleading text. <br>
Mitigation: Treat decoded content as untrusted and verify links or text before acting on them. <br>


## Reference(s): <br>
- [Advanced QR Intelligence on ClawHub](https://clawhub.ai/omar-khaleel/skills/qr-code) <br>
- [Publisher profile](https://clawhub.ai/user/omar-khaleel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated QR images are files, and decoded QR output is text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated QR codes are saved to caller-selected output paths; decoded QR contents should be treated as untrusted.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
