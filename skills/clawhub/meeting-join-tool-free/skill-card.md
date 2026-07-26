## Description: <br>
AI会议助手免费版 helps an agent join Google Meet, Microsoft Teams, or Zoom meetings by voice to provide live transcription, contextual Q&A, and Markdown meeting notes for personal use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals, freelancers, students, and other external users use this skill to bring a voice-based AI assistant into online meetings for transcription, contextual questions, and post-meeting notes. It is intended for meetings where participants have consented to recording or transcription. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live meeting audio and transcripts, which can expose private or confidential discussion content. <br>
Mitigation: Use it only in meetings where recording and transcription are permitted and participants have consented. <br>
Risk: The evidence does not fully scope where audio, transcripts, callback results, or derived notes are processed, stored, retained, or deleted. <br>
Mitigation: Clarify processing location, storage, access controls, retention, and deletion before using it for confidential, regulated, client-sensitive, or internal-sensitive meetings. <br>
Risk: The skill requires an AgentCall API key and supports callback URLs, creating credential and result-delivery exposure risks. <br>
Mitigation: Protect the API key, restrict file and environment access, and use callback URLs only when their recipient, transport, and access controls are trusted. <br>
Risk: Meeting transcripts, answers, and summaries may be incomplete or inaccurate, especially for critical decisions. <br>
Mitigation: Review generated notes and answers before acting on them, and avoid relying on the skill for medical, legal, or other high-stakes determinations. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/meeting-join-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON status responses, live transcript text, contextual answers, and Markdown meeting notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, callback results, speaker-aware transcript content, decisions, and action-item summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
