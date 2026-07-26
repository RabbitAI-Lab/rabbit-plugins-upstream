## Description: <br>
Helps developers build Azure VoiceLive real-time voice AI applications with WebSocket streaming, audio transcription, session management, VAD, function calling, authentication, and voice/model selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design and troubleshoot Azure VoiceLive Python applications for voice assistants, customer-service conversations, real-time translation, meeting transcription, and telephony voice workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive voice and transcript data. <br>
Mitigation: Avoid recording or streaming sensitive conversations without consent, and apply the organization's data handling and retention controls. <br>
Risk: Azure credentials may grant access to Cognitive Services resources. <br>
Mitigation: Use dedicated Azure credentials with least privilege, prefer managed identity where practical, and keep API keys out of source control. <br>
Risk: Callback URLs can expose results to unintended systems if misconfigured. <br>
Mitigation: Use only callback URLs that the deploying organization controls and trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-ai-voicelive-py) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces implementation guidance, configuration patterns, and troubleshooting steps for Azure VoiceLive applications.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
