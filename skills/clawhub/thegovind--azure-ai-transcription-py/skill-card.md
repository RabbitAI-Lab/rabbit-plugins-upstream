## Description: <br>
Azure AI Transcription SDK for Python supports real-time and batch speech-to-text transcription with timestamps and diarization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install and use the Azure AI Transcription Python client for batch and real-time speech-to-text workflows, including diarization, timestamps, and streaming. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure subscription keys can be exposed if copied into code, logs, transcripts, or shared prompts. <br>
Mitigation: Store the key in environment variables or a secret manager, avoid logging it, and rotate it promptly if exposure is suspected. <br>
Risk: Audio content or storage URLs may contain sensitive or unauthorized information before being sent to Azure transcription services. <br>
Mitigation: Transcribe only audio and storage URLs the user is authorized to process, and review Azure retention, logging, and compliance settings for sensitive data. <br>
Risk: Speech-to-text output, timestamps, and speaker diarization may be incomplete or inaccurate for downstream records or subtitles. <br>
Mitigation: Review generated transcripts before relying on them, specify the correct language, and verify speaker labels and timestamps for important uses. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with shell and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment variable names, subscription key authentication guidance, batch and streaming examples, and best practices.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
