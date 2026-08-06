## Description: <br>
Azure AI Transcription Py helps agents guide Python-based real-time and batch speech-to-text workflows with Azure AI Transcription, including diarization, timestamps, locale selection, authentication setup, and session handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure Azure transcription credentials, choose between batch and streaming transcription patterns, and produce transcript, subtitle, or timestamped speech-to-text implementation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and exec tool access and contains unrelated command-execution and code-analysis capabilities beyond its transcription purpose. <br>
Mitigation: Install and run it only in a sandboxed agent environment where broad tool access is acceptable, and limit use to the documented transcription workflow. <br>
Risk: Audio recordings and transcripts may contain confidential or regulated content and are sent to Azure services when transcription workflows are followed. <br>
Mitigation: Submit recordings only after Azure data handling is approved for the content, and avoid using confidential recordings in unapproved environments. <br>
Risk: Azure subscription keys can be exposed if copied into source files, logs, or shared prompts. <br>
Mitigation: Configure only TRANSCRIPTION_ENDPOINT and TRANSCRIPTION_KEY through environment variables or approved secret storage, rotate leaked keys, and avoid hardcoding credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-ai-transcription-py) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include environment variable setup, Azure transcription client examples, transcript export guidance, and operational troubleshooting notes.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
