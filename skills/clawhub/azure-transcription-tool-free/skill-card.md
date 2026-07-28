## Description: <br>
Azure语音转写免费版 helps agents guide personal users through Azure AI speech-to-text transcription for Blob-hosted audio, including timestamped transcript and subtitle workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal creators use this skill to prepare Azure speech-to-text transcription jobs for podcasts, meeting recordings, voice notes, and video subtitle generation. It is scoped to Azure transcription workflows and is not intended for certified translation, simultaneous interpretation, or general localization tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio recordings may contain sensitive personal or business information, and the skill asks users to process cloud-accessible Blob URLs. <br>
Mitigation: Use tightly scoped, time-limited storage access for private audio, avoid public Blob URLs for sensitive recordings, and confirm retention expectations before processing. <br>
Risk: The trigger guidance is mismatched with the skill's speech-to-text scope and may be invoked for translation or localization tasks it does not support. <br>
Mitigation: Use the skill only for Azure speech-to-text transcription tasks and route translation, localization, and certified language work to appropriate tools. <br>
Risk: The workflow depends on Azure credentials and a cloud transcription service. <br>
Mitigation: Keep Azure credentials in environment variables or managed secret storage, review credential handling before execution, and avoid committing keys or transcripts to shared repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-transcription-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python snippets, and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure endpoint and subscription-key environment variable setup, Blob URL inputs, locale settings, timestamped transcript handling, and SRT subtitle generation examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
