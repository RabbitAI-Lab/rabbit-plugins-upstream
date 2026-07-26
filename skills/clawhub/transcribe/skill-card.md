## Description: <br>
Transcribe audio files to text using local Whisper (Docker). Use when receiving voice messages, audio files (.mp3, .m4a, .ogg, .wav, .webm), or when asked to transcribe audio content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[javicasper](https://clawhub.ai/user/javicasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Transcribe to convert local audio attachments or voice messages into plain text before summarizing, replying, or extracting content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The current installer is incomplete because it references a missing scripts/transcribe wrapper and attempts a privileged system-wide install. <br>
Mitigation: Review before installing, avoid system-wide installation until the wrapper is supplied and reviewed, or adapt installation to a user-local path. <br>
Risk: The Docker build downloads external Python and model dependencies before local transcription can run. <br>
Mitigation: Build in a controlled environment and verify downloaded dependencies and the selected language setting before relying on transcripts. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text transcript with Markdown usage guidance and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local Docker image with faster-whisper, defaults to Spanish unless a language is supplied, and supports auto-detection.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
