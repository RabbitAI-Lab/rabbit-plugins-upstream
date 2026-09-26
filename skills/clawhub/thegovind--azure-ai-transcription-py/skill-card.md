## Description:

Azure AI Transcription SDK for Python supports real-time and batch speech-to-text transcription with timestamps and diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thegovind](https://clawhub.ai/user/thegovind)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to add Azure AI speech-to-text transcription flows to Python agents, including batch jobs, streaming transcription, timestamps, and speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio recordings or content URLs sent for transcription may contain personal, confidential, or regulated speech.

Mitigation: Only transcribe recordings or URLs the user is authorized to send to Azure, and review data-handling requirements before use.

Risk: Azure subscription keys can be exposed if copied into prompts, code, logs, or shared files.

Mitigation: Store the key in protected environment variables or a secrets manager and avoid printing or committing it.

Risk: The installation example uses an unpinned package dependency.

Mitigation: Install in a virtual environment and pin and review the package version before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-ai-transcription-py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment-variable configuration and Azure subscription-key authentication guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
