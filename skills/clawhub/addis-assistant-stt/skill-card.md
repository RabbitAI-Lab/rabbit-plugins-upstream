## Description: <br>
Provides speech-to-text for Amharic audio and text translation between languages using the Addis Assistant API, with an x-api-key required for requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dagmawibabi](https://clawhub.ai/user/dagmawibabi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe Amharic audio files and translate text between languages through the Addis Assistant API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio and text submitted through this skill are sent to the Addis Assistant API. <br>
Mitigation: Use only audio or text that is appropriate to share with that external service, and avoid sensitive or regulated data unless approved. <br>
Risk: The provided scripts accept API keys as command-line arguments, which can expose secrets through shell history or process listings. <br>
Mitigation: Prefer a secret store or environment variable and avoid pasting real API keys directly into commands. <br>
Risk: The artifact scripts and examples use API endpoints without an explicit https:// scheme. <br>
Mitigation: Review or update requests to use explicit HTTPS endpoints before production use. <br>


## Reference(s): <br>
- [Addis Assistant API Specifications](references/api_spec.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dagmawibabi/skills/addis-assistant-stt) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Plain text and JSON API responses, with Python and curl command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an x-api-key and sends audio or text to the Addis Assistant API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
