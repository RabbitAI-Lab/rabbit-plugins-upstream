## Description: <br>
Guides agents through ScrappyLabs text-to-speech and speech-to-text APIs for voice generation, transcription, voice design, and bot credential setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loserbcc](https://clawhub.ai/user/loserbcc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent builders use this skill to connect agents to ScrappyLabs speech APIs for generating speech, transcribing uploaded audio, designing voices, and checking credential status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes generated text, bot identifiers, and uploaded audio to ScrappyLabs, creating privacy and data-handling exposure. <br>
Mitigation: Require explicit user approval before sending text, identifiers, or recordings, and review ScrappyLabs retention and privacy terms before use. <br>
Risk: The skill describes permanent auto-renewing credentials and owner-provided keys without full revocation, quota, renewal, or billing detail. <br>
Mitigation: Confirm token scope, revocation, renewal, quotas, and billing implications before initiating or evolving credentials or using owner-provided keys. <br>
Risk: Voice cloning and audio upload behavior may involve sensitive biometric or consent-dependent data. <br>
Mitigation: Use voice cloning only with documented consent and approval, and avoid uploading recordings that contain sensitive or unapproved personal data. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/loserbcc/skills/cult-of-carcinization) <br>
- [ScrappyLabs TTS website](https://tts.scrappylabs.ai) <br>
- [ScrappyLabs API base](https://api.scrappylabs.ai) <br>
- [ScrappyLabs molt discovery endpoint](https://api.scrappylabs.ai/v1/molt/discover) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with inline bash code blocks and endpoint tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes ScrappyLabs endpoint examples for TTS, STT, voice design, voice cloning, status checks, and credential evolution.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
