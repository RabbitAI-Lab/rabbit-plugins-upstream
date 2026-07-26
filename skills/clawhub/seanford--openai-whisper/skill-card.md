## Description: <br>
Local speech-to-text with the Whisper CLI (no API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to transcribe or translate local audio files through the Whisper command-line tool without an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill may require installing the Homebrew openai-whisper package and allowing Whisper to download model files into the local cache. <br>
Mitigation: Install only in environments where the local Whisper package and model downloads are approved. <br>
Risk: Generated transcript files may contain sensitive speech content. <br>
Mitigation: Transcribe only audio intended for local processing and choose output directories deliberately. <br>


## Reference(s): <br>
- [OpenAI Whisper](https://openai.com/research/whisper) <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/openai-whisper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and local transcript output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local whisper binary; transcript files are written to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
