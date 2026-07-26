## Description: <br>
Command-line guide for fast speech-to-text transcription from local files, URLs, STDIN, or live microphone input using the Deepgram CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nerkn](https://clawhub.ai/user/nerkn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to install and authenticate the Deepgram CLI, transcribe audio from files, URLs, STDIN, or microphone input, and capture transcripts for search, summarization, subtitles, or post-processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio or live microphone input may include confidential, personal, or regulated content that is sent to Deepgram for transcription. <br>
Mitigation: Only transcribe audio that the user is authorized to send to Deepgram, and review data handling requirements before use. <br>
Risk: The workflow stores and uses a Deepgram API key locally for CLI authentication. <br>
Mitigation: Protect the API key, avoid exposing it in shell history or shared files, and rotate it if it may have been disclosed. <br>
Risk: The skill asks the agent to install and use the @deepgram/cli package. <br>
Mitigation: Verify that @deepgram/cli is the intended Deepgram package before installation. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/nerkn/skills/deepgram) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI installation, authentication, transcription options, output handling, and privacy guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
