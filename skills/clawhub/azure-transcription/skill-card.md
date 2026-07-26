## Description: <br>
Azure Transcription helps agents guide Azure Speech transcription workflows for real-time and batch audio transcription, speaker diarization, custom speech models, and transcript export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and run Azure-based transcription workflows for meetings, customer calls, and media subtitle generation. It supports guidance for real-time transcription, batch queues, speaker diarization, and exporting transcripts as text, SRT, VTT, or JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio and transcripts may contain sensitive information and may be sent to Azure or stored locally. <br>
Mitigation: Confirm authorization before processing audio, use approved storage locations, and delete or encrypt transcript outputs as appropriate. <br>
Risk: Azure credentials are required for execution. <br>
Mitigation: Protect TRANSCRIPTION_KEY and related endpoint configuration, and avoid committing credentials or transcript outputs to version control. <br>
Risk: The skill includes executable setup and SDK examples. <br>
Mitigation: Review commands and generated code before running them in an agent environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-transcription) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with Python and shell snippets; transcript exports may be text, SRT, VTT, or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Azure Speech endpoint and key, network access, and approved local storage for transcript outputs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
