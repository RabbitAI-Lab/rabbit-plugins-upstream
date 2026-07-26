## Description: <br>
Transcribes audio from a file ID or HTTPS URL into text, SRT, WebVTT, or JSON, with optional speaker diarization, timestamps, profanity filtering, and task polling through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit audio transcription jobs, poll completion status, and retrieve text, subtitle, or JSON transcript outputs for meetings, interviews, podcasts, webinars, voice memos, and captioning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio submitted for transcription may contain confidential, regulated, or third-party content and is sent to AgentPMT and its transcription providers. <br>
Mitigation: Submit only recordings you are authorized to process, and avoid sensitive content unless the relevant privacy, contractual, and retention requirements are understood. <br>
Risk: Successful transcriptions may create File Manager artifacts and signed URLs that expose transcript content if mishandled. <br>
Mitigation: Prefer persistent file IDs for follow-up operations, avoid sharing signed URLs broadly, and handle transcript artifacts under the same access controls as the source audio. <br>
Risk: Transcription actions charge credits on submission, and a later failure is not automatically refunded. <br>
Mitigation: Choose the transcription tier from the known recording length before submission, and review task errors and recommended actions before resubmitting. <br>
Risk: Public URL inputs download remote audio and must not point to private or internal network resources. <br>
Mitigation: Use only HTTPS URLs intended for this transcription workflow, or provide a File Manager file ID from a prior authorized upload. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/speech-to-text-with-speakers) <br>
- [AgentPMT Marketplace Page](https://www.agentpmt.com/marketplace/speech-to-text-with-speakers) <br>
- [Generated Action Schema](schema.md) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [File Management Skill](https://clawhub.ai/agentpmt/file-management) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Text, Markdown] <br>
**Output Format:** [Markdown instructions with JSON tool-call examples; remote transcription results may be text, SRT, WebVTT, or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses asynchronous task IDs, polling, AgentPMT credits, and optional File Manager result artifacts.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
