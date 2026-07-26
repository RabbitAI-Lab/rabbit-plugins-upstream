## Description: <br>
Generate QR codes from text or URLs and decode QR codes from local image files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[omar-khaleel](https://clawhub.ai/user/omar-khaleel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to create QR code image files for supplied text or URLs, or to decode QR contents from screenshots and image files before deciding how to use the result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: QR codes can contain sensitive URLs, tokens, or other private text. <br>
Mitigation: Only provide content and images you are comfortable processing, and review decoded results before opening links or sharing generated QR codes. <br>
Risk: Decoded QR content may point to unsafe or unexpected destinations. <br>
Mitigation: Treat decoded links as untrusted text until inspected and verified outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/omar-khaleel/skills/qr-code-intelligence) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and Python examples; generated QR artifacts are image files and decoded QR results are text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports configurable QR size, border, and error correction level for generation; decoding can return the first QR result or all detected QR results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
