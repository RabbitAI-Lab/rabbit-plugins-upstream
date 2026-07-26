## Description: <br>
Handles voice-to-voice conversations on WhatsApp by transcribing incoming audio and responding with local TTS audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to handle WhatsApp voice conversations when a user wants to speak instead of type. It turns incoming voice notes into prompts and returns both text and local TTS audio replies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incoming voice notes may contain sensitive information and are handled as prompts. <br>
Mitigation: Install only for WhatsApp voice workflows that need local transcription and TTS, and review generated replies before sending when the client allows it. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands] <br>
**Output Format:** [Text response plus OGG audio file, with shell commands for local transcription and TTS execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local ffmpeg, whisper-cpp, and sherpa-onnx-tts tooling; no server-resolved provenance links were available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
