## Description: <br>
ClawVox is an ElevenLabs voice studio for OpenClaw that helps agents generate speech, transcribe audio, clone voices, create sound effects, isolate voices, dub audio, and manage voice libraries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhishek-official1](https://clawhub.ai/user/abhishek-official1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to add ElevenLabs voice workflows to an agent, including text-to-speech, transcription, voice cloning, sound effects, voice isolation, dubbing, and voice library management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send selected text, audio, video, and voice samples to ElevenLabs. <br>
Mitigation: Use it only with data that is authorized for third-party processing, and avoid confidential or regulated recordings unless policy permits that use. <br>
Risk: Voice cloning can misuse a speaker's voice if samples are used without consent. <br>
Mitigation: Clone voices only with explicit permission from the speaker and document the permitted use. <br>
Risk: API keys may be exposed through debug or test usage. <br>
Mitigation: Store the ElevenLabs API key in protected environment or config storage, avoid passing it on the command line, and do not run transcribe.sh with DEBUG enabled in shared logs. <br>


## Reference(s): <br>
- [ClawVox ClawHub skill page](https://clawhub.ai/abhishek-official1/skills/clawvox) <br>
- [ElevenLabs developer documentation](https://elevenlabs.io/developers) <br>
- [ElevenLabs API documentation](https://elevenlabs.io/docs) <br>
- [ElevenLabs voice library](https://elevenlabs.io/voice-library) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated audio or transcript files from the invoked scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and ELEVENLABS_API_KEY; generated media and transcripts are handled by ElevenLabs APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
