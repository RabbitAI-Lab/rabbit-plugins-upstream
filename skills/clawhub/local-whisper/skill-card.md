## Description: <br>
Local speech-to-text using OpenAI Whisper. Runs fully offline after model download. High quality transcription with multiple model sizes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[araa47](https://clawhub.ai/user/araa47) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to transcribe local audio files with OpenAI Whisper, choosing model size, language, timestamps, and JSON output as needed. It is useful for offline speech-to-text workflows after the initial model download. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill requires ffmpeg, Python Whisper/Torch dependencies, and a Whisper model download on first use. <br>
Mitigation: Install it only in an environment where those dependencies and model downloads are acceptable, and review dependency sources before use. <br>
Risk: Audio files and generated transcripts may contain sensitive content. <br>
Mitigation: Choose input files intentionally, keep processing and transcript storage local where required, and avoid sharing outputs without review. <br>


## Reference(s): <br>
- [ClawHub Local Whisper skill page](https://clawhub.ai/araa47/skills/local-whisper) <br>
- [PyTorch CPU wheel index](https://download.pytorch.org/whl/cpu) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration guidance] <br>
**Output Format:** [Plain text transcript or JSON with transcript text, language, and optional timestamp segments; setup guidance is Markdown with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports selectable Whisper model size, optional language selection, optional word timestamps, JSON output, and quiet mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
