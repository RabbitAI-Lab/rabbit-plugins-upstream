## Description: <br>
Generate expressive talking-head videos from static images using Kameo AI, with optional prompt enhancement for facial expression, lip-sync, and motion guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[veya2ztn](https://clawhub.ai/user/veya2ztn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content creators use this skill to turn portraits or avatar images into short talking-head videos for demos, social media content, educational material, and multilingual avatar presentations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports risky credential handling and a live-looking API key in the documentation. <br>
Mitigation: Use a user-owned Kameo API key, do not reuse any key shown in the docs, and rotate or revoke any exposed credential before use. <br>
Risk: The registration helper may write credentials to ~/.config/kameo/credentials.json. <br>
Mitigation: Review the helper before running it, protect the credentials file, and delete it when persistent local storage is not needed. <br>
Risk: Prompts and images may be sent to Kameo and optionally Google Gemini. <br>
Mitigation: Avoid submitting sensitive, private, or regulated images and prompts unless the relevant service terms and data handling are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/veya2ztn/skills/kameo-free) <br>
- [Publisher profile](https://clawhub.ai/user/veya2ztn) <br>
- [Kameo service](https://kameo.chat) <br>
- [Kameo public API](https://api.kameo.chat/api/public) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides Kameo API calls that can return video URLs and local credential configuration instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
