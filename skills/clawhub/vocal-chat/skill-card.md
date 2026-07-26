## Description: <br>
Handles voice-to-voice conversations on WhatsApp by transcribing incoming audio and responding with local TTS audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent handle WhatsApp voice conversations, including local transcription of incoming voice notes and local text-to-speech responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Referenced local speech tools may process sensitive WhatsApp audio, transcripts, or generated voice replies. <br>
Mitigation: Confirm ffmpeg, whisper-cpp, and sherpa-onnx-tts are trusted local installations and review retention of temporary audio, transcripts, and sent voice files before use. <br>
Risk: Automatic transcription and voice responses can produce unintended replies if audio is misrecognized or context is incomplete. <br>
Mitigation: Keep the paired text response visible for review and test the voice workflow with representative WhatsApp audio before relying on it. <br>


## Reference(s): <br>
- [Vocal Chat on ClawHub](https://clawhub.ai/rubenfb23/skills/vocal-chat) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, audio files, guidance] <br>
**Output Format:** [Markdown with inline bash commands and references to generated .ogg voice files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local speech tools for transcription and TTS; no additional output constraints are stated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
