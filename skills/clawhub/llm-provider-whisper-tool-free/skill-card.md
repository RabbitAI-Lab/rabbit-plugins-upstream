## Description: <br>
Provides local Whisper CLI guidance for transcribing or translating common audio formats into text, subtitle, or JSON outputs without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run local Whisper-based transcription or translation workflows for meetings, podcasts, video subtitles, and single audio files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup commands install Python packages and system dependencies, including package-manager commands that may require elevated privileges. <br>
Mitigation: Review dependency commands before execution and install only from trusted package sources. <br>
Risk: The first transcription run may download a Whisper model into ~/.cache/whisper, which is incompatible with strictly offline environments. <br>
Mitigation: Preload approved model files into the cache before use when offline or network-restricted operation is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/llm-provider-whisper-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output file descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying CLI may produce txt, srt, vtt, json, or tsv transcription files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
