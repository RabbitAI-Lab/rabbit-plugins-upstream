## Description: <br>
Uses Azure AI to batch transcribe audio to text with basic transcription and timestamps for personal audio workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual creators and developers use this skill to configure Azure-based batch speech-to-text for podcasts, meeting recordings, and subtitle drafts. It is intended for audio transcription workflows that can use Azure Blob storage and Azure AI credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive meetings, interviews, or recordings may be uploaded to Blob storage and processed by Azure without the user confirming they are allowed to do so. <br>
Mitigation: Confirm consent, data handling requirements, and retention rules before uploading audio or running transcription jobs. <br>
Risk: The skill requires TRANSCRIPTION_KEY and related Azure configuration, which are credentials that could be exposed in commands, files, or logs. <br>
Mitigation: Store credentials in environment variables or a secret manager, avoid committing them, and rotate keys if exposure is suspected. <br>
Risk: The trigger text incorrectly points to translation and localization tasks, which could lead users to apply the skill outside its speech-to-text scope. <br>
Mitigation: Use the skill only for Azure-based audio transcription and timestamped transcript generation, not translation or localization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-transcription-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command snippets; generated transcription text or SRT-style subtitle content when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Azure transcription credentials and Blob-hosted audio inputs when the workflow is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
