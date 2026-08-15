## Description:

AgentCall lets agents provision phone numbers, send and receive SMS, place voice and AI voice calls, manage AI receptionists, schedules, webhooks, text-to-speech, and call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agents to real phone and SMS workflows, including AI receptionists, outbound calls, OTP handling for apps they control, scheduled texts, webhooks, and auditable call memory. It is intended for agent workflows where the user explicitly authorizes contact with real recipients and accepts the associated billing.

### Deployment Geography for Use:

Global, with phone-number and AI-voice carrier support focused on the United States and Canada.

## Known Risks and Mitigations:

Risk: Billable telephony actions can provision numbers, send SMS, place calls, enable AI voice, record calls, synthesize speech, or schedule future outreach.

Mitigation: Require explicit user confirmation of recipient, message or prompt, schedule, recording setting, duration, and expected cost before invoking billable actions.

Risk: External-effect actions can contact real people or configure a number to keep answering future inbound calls.

Mitigation: Act only within the user's stated authorization, monitor usage after configuration, disable inbound AI or cancel schedules when the purpose is complete, and surface API guardrail errors instead of retrying blindly.

Risk: The skill can handle sensitive phone numbers, call and SMS content, transcripts, recordings, memory, webhooks, and BYOK provider keys.

Mitigation: Install only for trusted AgentCall use, protect credentials and webhook secrets, verify webhook signatures, and purge or disable stored memory when it is no longer needed.

## Reference(s):

- [AgentCall ClawHub skill page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall pricing](https://agentcall.co/#pricing)
- [Voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [Hermes context webhook walkthrough](https://agentcall.co/docs/hermes)
- [Post-call transcript webhook guide](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with REST request examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENTCALL_API_KEY for authenticated requests; some actions are billable, contact real people, or change persistent phone-number behavior.]

## Skill Version(s):

2.12.9 (source: evidence release metadata and claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
