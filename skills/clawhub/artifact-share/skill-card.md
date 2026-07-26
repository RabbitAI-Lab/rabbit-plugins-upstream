## Description: <br>
Use when you need to share static web content (HTML/CSS/JS/images) via a publicly accessible URL — uploading generated files, creating shareable pages, or deploying single-page web artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gavin-yyc](https://clawhub.ai/user/gavin-yyc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to upload generated static web artifacts, manage hosted files, and return public preview links or QR codes for browser review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded files become available through an external public sharing service. <br>
Mitigation: Upload only static content intended for sharing, avoid private documents or internal code, and use password protection when access should be limited. <br>
Risk: The service uses a persistent API key stored in a local config file. <br>
Mitigation: Protect or delete ~/.config/artifact-share/config.yml when no longer needed and never commit or share the API key. <br>
Risk: A device ID based on username and hostname can reveal local identity details. <br>
Mitigation: Prefer a random device_id when identity exposure is not necessary. <br>


## Reference(s): <br>
- [Artifact Share service](https://artifact-share.youthol.top) <br>
- [ClawHub skill page](https://clawhub.ai/gavin-yyc/skills/artifact-share) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, API examples, share URLs, and optional QR code image data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or reuse a local config file containing the API key for the external sharing service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
