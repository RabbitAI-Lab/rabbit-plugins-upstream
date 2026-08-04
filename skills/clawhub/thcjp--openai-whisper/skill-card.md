## Description: <br>
Openai Whisper helps an agent guide local speech-to-text transcription with the Whisper CLI, supporting common audio formats without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent builders, and automation workflow users can use this skill to run or configure local Whisper CLI transcription and produce usable transcript output from audio files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documentation is contradictory and asks for broad API key and command authority that is not clearly tied to local transcription. <br>
Mitigation: Use the skill only for local Whisper transcription, do not provide API keys based on the current documentation, and review the skill carefully before installation. <br>
Risk: Command execution can affect unintended files or paths if audio inputs or output paths are untrusted. <br>
Mitigation: Limit execution to trusted audio inputs and intended output paths, and review generated commands before running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/openai-whisper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and text transcription outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local transcription workflow; transcript quality depends on audio quality, language selection, and the selected Whisper model.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
