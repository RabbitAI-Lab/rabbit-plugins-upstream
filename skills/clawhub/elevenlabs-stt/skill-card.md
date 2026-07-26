## Description: <br>
Transcribe audio files using ElevenLabs Speech-to-Text (Scribe v2). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdbotborges](https://clawhub.ai/user/clawdbotborges) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to transcribe selected audio or video files with ElevenLabs Speech-to-Text, optionally requesting speaker diarization, language hints, audio event tags, or JSON output with timestamps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio files are sent to ElevenLabs for transcription. <br>
Mitigation: Use this skill only for audio that is approved for ElevenLabs processing, and avoid confidential, regulated, or consent-sensitive recordings unless that use is authorized. <br>
Risk: The ElevenLabs API key is required for authentication. <br>
Mitigation: Keep ELEVENLABS_API_KEY out of source control and provide it through an approved secret or environment configuration. <br>
Risk: The script relies on jq when parsing API responses. <br>
Mitigation: Install jq before relying on the transcription script in normal workflows. <br>


## Reference(s): <br>
- [ElevenLabs Speech-to-Text](https://elevenlabs.io/speech-to-text) <br>
- [ElevenLabs Speech-to-Text API Documentation](https://elevenlabs.io/docs/api-reference/speech-to-text) <br>
- [ClawHub Skill Page](https://clawhub.ai/clawdbotborges/skills/elevenlabs-stt) <br>
- [Publisher Profile](https://clawhub.ai/user/clawdbotborges) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Plain text transcript or JSON response emitted by a shell command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq for response parsing, and ELEVENLABS_API_KEY for ElevenLabs authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
