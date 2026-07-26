## Description: <br>
Provides local Whisper v1 audio transcription and subtitle generation for single audio or video files, with optional audio-to-English translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to install local transcription dependencies, run Whisper CLI commands, and produce transcript or subtitle outputs for user-selected media files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to run local shell commands and install transcription dependencies. <br>
Mitigation: Review proposed commands before execution and install only in environments where local package installation is permitted. <br>
Risk: The first transcription run may download Whisper model files and cache them locally. <br>
Mitigation: Plan for network access and local storage, or pre-stage approved model files before using the skill in controlled environments. <br>
Risk: The documentation contains inconsistent API-key guidance and a broader localization trigger than the supported transcription scope. <br>
Mitigation: Use the skill only for user-selected audio or video transcription and audio-to-English translation, and clarify API-key requirements with the publisher before controlled or offline use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/llm-provider-whisper-v1-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and transcript or subtitle file outputs such as txt, srt, vtt, json, or tsv.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install command-line dependencies and cache Whisper model files locally on first use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
