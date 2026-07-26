## Description: <br>
CloneV helps an agent generate cloned speech from a 6-30 second WAV voice sample and input text using Coqui XTTS v2. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[instant-picture](https://clawhub.ai/user/instant-picture) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use CloneV to create multilingual cloned-voice OGG audio from authorized WAV samples and text prompts, such as personal voice messages or notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice samples and cloned audio can contain sensitive biometric data and may be retained in the working directories used by the skill. <br>
Mitigation: Use only authorized voice samples and delete copied samples plus generated audio after the task is complete. <br>
Risk: Generated audio could be used for impersonation, deception, or fraud-sensitive messages. <br>
Mitigation: Avoid impersonation and fraud-sensitive content, disclose synthetic audio when sharing, and confirm any external send action before transmission. <br>
Risk: The skill can send generated voice messages through integrations such as Telegram examples. <br>
Mitigation: Review the generated audio and require explicit user confirmation before sending it to another person or channel. <br>


## Reference(s): <br>
- [Complete Reference Guide](references/complete-guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/instant-picture/skills/clonev) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated OGG audio file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires text, a WAV voice sample path, and an optional language code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
