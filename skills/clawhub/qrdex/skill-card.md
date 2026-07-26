## Description: <br>
Create, manage, and track QR codes using the QRdex.io REST API for URL, email, telephone, SMS, WhatsApp, and WiFi QR workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sebastienb](https://clawhub.ai/user/sebastienb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to generate QRdex.io API requests, manage account QR codes, download SVG QR images, and inspect scan-tracking fields for QR campaigns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a QRdex.io API key to perform account-level QR code actions. <br>
Mitigation: Use a revocable API key, keep QRDEX_API_KEY out of prompts and logs, and remove the key when the agent no longer needs access. <br>
Risk: Update and delete operations can affect existing QR codes in the connected QRdex.io team. <br>
Mitigation: Confirm QR code IDs and intended changes before update or delete commands. <br>
Risk: Tracked QR codes and QR payloads can store or expose sensitive WiFi, contact, message, or business data through QRdex.io. <br>
Mitigation: Avoid sensitive payloads unless remote storage and scan tracking are acceptable for the data involved. <br>


## Reference(s): <br>
- [QRdex API Reference](references/API_REFERENCE.md) <br>
- [QRdex Skill Page](https://clawhub.ai/sebastienb/skills/qrdex) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with API examples, CLI commands, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce QRdex.io API requests and commands that use QRDEX_API_KEY; downloaded QR images are SVG files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
