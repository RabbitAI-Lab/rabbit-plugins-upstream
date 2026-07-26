## Description: <br>
Twilio Voice helps agents place and manage Twilio-backed phone calls, conferences, recordings, IVR sessions, transcripts, and live calls through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to give agents controlled access to a business Twilio account for outbound calling, conferencing, recording, transcription, IVR, DTMF, and live-call workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Phone calls, customer outreach, recordings, transcripts, and DTMF or IVR automation can affect customer privacy, consent, and regulated communications. <br>
Mitigation: Enable the skill only for agents authorized to use the organization's Twilio account and business phone number; confirm recipient consent, call-recording legality, and retention and access rules before use. <br>
Risk: The skill can place, redirect, end, record, and manage real calls and conferences from a connected Twilio credential. <br>
Mitigation: Limit credential access and caller IDs to appropriate agents, review call history and status, and terminate calls or conferences when activity is no longer intended. <br>


## Reference(s): <br>
- [ClawHub Twilio Voice listing](https://clawhub.ai/agentpmt/skills/twilio-voice) <br>
- [AgentPMT Twilio Voice marketplace page](https://www.agentpmt.com/marketplace/twilio-voice) <br>
- [Twilio Voice action schema](schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON action examples and generated action schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers 28 Twilio Voice actions, including calls, conferences, recordings, IVR, DTMF, and live-call transcript workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
