## Description: <br>
Handles voice-to-voice conversations on WhatsApp by transcribing incoming audio and responding with local text-to-speech audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent handle WhatsApp voice conversations: incoming voice notes are transcribed locally, processed as prompts, and answered with both text and a generated voice note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WhatsApp voice notes are transcribed and processed by the agent, and the skill can send both text and voice-note replies. <br>
Mitigation: Use only where that voice processing and reply behavior is intended, and review the agent's text and audio responses before relying on them in sensitive conversations. <br>
Risk: The transcription and text-to-speech tools referenced by the skill are local dependencies that were not included in the reviewed artifact. <br>
Mitigation: Verify ffmpeg, whisper-cpp, sherpa-onnx-tts, and any helper scripts are installed from trusted sources before enabling the skill. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated OGG voice-note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates local .ogg audio replies and also sends text for clarity.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
