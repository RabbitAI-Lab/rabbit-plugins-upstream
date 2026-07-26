## Description: <br>
Generate expressive talking-head videos from static images using Kameo AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[veya2ztn](https://clawhub.ai/user/veya2ztn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to turn portrait or avatar images into short talking-head videos with dialogue, facial motion, and selectable aspect ratios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documentation includes a live-looking Kameo API key. <br>
Mitigation: Use your own Kameo key, rotate or avoid any copied key, and remove embedded credentials before sharing or deploying the skill. <br>
Risk: The registration helper accepts passwords on the command line. <br>
Mitigation: Avoid passing real passwords to register.sh; prefer an interactive or secret-manager-based credential flow. <br>
Risk: Image and dialogue inputs are sent to external Kameo and, for enhanced generation, Google Gemini services. <br>
Mitigation: Only process images and dialogue that are approved for those services and meet the user's privacy and data-handling requirements. <br>
Risk: Credentials may be stored in ~/.config/kameo/credentials.json. <br>
Mitigation: Prefer a secure secret manager or tightly permissioned local credential storage, and rotate keys if local storage is exposed. <br>


## Reference(s): <br>
- [Kameo Skill on ClawHub](https://clawhub.ai/veya2ztn/skills/kameo) <br>
- [Kameo](https://kameo.chat) <br>
- [Kameo Public API](https://api.kameo.chat/api/public) <br>
- [Google Gemini GenerateContent API](https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and API response details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce video URLs from Kameo API calls when executed with user-provided credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact package.json lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
