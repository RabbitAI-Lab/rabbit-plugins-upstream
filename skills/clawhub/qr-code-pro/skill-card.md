## Description: <br>
Generate and read QR codes from text, URLs, image files, and screenshots, with support for PNG/JPG workflows and configurable QR generation options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[omar-khaleel](https://clawhub.ai/user/omar-khaleel) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and other ClawHub users use this skill to generate QR codes from text or URLs and decode QR code payloads from local image files or screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Decoded QR contents may contain untrusted links or text. <br>
Mitigation: Inspect decoded payloads before opening links, executing commands, or acting on the content. <br>
Risk: The skill requires local QR and image-processing dependencies. <br>
Mitigation: Install only the listed dependencies from trusted package sources and verify platform-specific requirements such as zbar or Visual C++ Redistributable before use. <br>


## Reference(s): <br>
- [Advanced QR Intelligence on ClawHub](https://clawhub.ai/omar-khaleel/skills/qr-code-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python code examples; scripts emit text or JSON results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated QR codes are saved as PNG files; decoded QR results may be emitted as plain text or JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
