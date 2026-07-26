## Description: <br>
Azure Ai Transcription Py helps agents guide Python-based Azure AI speech-to-text workflows for real-time streaming and batch transcription, including diarization, timestamps, language selection, backpressure handling, and session cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure Azure AI transcription credentials, choose between batch and real-time transcription, and produce guidance or Python-oriented examples for converting speech recordings into transcripts, subtitles, or meeting notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure subscription keys or transcription endpoints may be exposed through shell history, logs, or source control. <br>
Mitigation: Use TRANSCRIPTION_ENDPOINT and TRANSCRIPTION_KEY as environment variables or a secret manager, avoid pasting secrets into persistent command history, and rotate any exposed keys. <br>
Risk: Private, regulated, or confidential recordings may be uploaded to Azure storage or submitted through callback and transcription workflows without appropriate approval. <br>
Mitigation: Use the skill only with approved Azure storage, SAS URLs, regions, callback endpoints, and retention settings for the sensitivity of the audio data. <br>
Risk: The skill documentation contains confusing or overbroad claims that may overstate what the helper provides. <br>
Mitigation: Review generated commands, Python examples, and operational guidance before deployment, and confirm them against the actual Azure transcription service and package in use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-ai-transcription-py) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure endpoint and key configuration guidance, transcription workflow examples, troubleshooting steps, and risk-aware handling notes for audio data and credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
