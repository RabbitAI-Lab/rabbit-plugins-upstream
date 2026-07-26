## Description: <br>
Install and use the speechall CLI tool for speech-to-text transcription, including provider selection, model listing, speaker diarization, subtitle output, and terminal workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atacan](https://clawhub.ai/user/atacan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to install, authenticate, and run the Speechall command-line tool for audio and video transcription. It supports terminal workflows for choosing speech-to-text models, generating text or subtitle output, and using options such as diarization, language selection, and custom vocabulary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio or video selected for transcription may be sent to an external transcription service. <br>
Mitigation: Only transcribe recordings the user is authorized and comfortable sending to the service. <br>
Risk: API keys can be exposed if placed directly in shell history or shared command text. <br>
Mitigation: Prefer the SPEECHALL_API_KEY environment variable and avoid putting secrets directly in CLI flags. <br>
Risk: Installation depends on a Homebrew tap or GitHub release source. <br>
Mitigation: Confirm the user trusts the selected installation source before installing or running the binary. <br>


## Reference(s): <br>
- [Speechall CLI GitHub releases](https://github.com/Speechall/speechall-cli/releases) <br>
- [Speechall API key console](https://speechall.com/console/api-keys) <br>
- [ClawHub skill page](https://clawhub.ai/atacan/skills/speechall-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and option tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API-key environment variable guidance and CLI flags for model, language, output format, diarization, and vocabulary options.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
