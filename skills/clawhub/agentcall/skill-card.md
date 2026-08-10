## Description:

AgentCall gives agents phone numbers for SMS, OTP verification, voice calls, AI voice calls, webhooks, proactive scheduling, and auditable call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent provision phone numbers, send and receive SMS, place voice calls, configure AI receptionists, manage call memory, and register webhooks. It is intended for real telephony workflows where the user authorizes outbound contact, paid features, and persistent configuration changes.

### Deployment Geography for Use:

Global, with AI voice and inbound AI carrier support documented for US and Canada numbers.

## Known Risks and Mitigations:

Risk: The skill can send SMS messages, place calls, configure AI voice, and schedule proactive outreach to real people, which may incur charges and create unwanted contact if used without clear authorization.

Mitigation: Require explicit user confirmation for the recipient, message or prompt, timing, recording setting, and expected cost before invoking billable or external-effect actions.

Risk: Inbound AI, proactive schedules, BYOK billing mode, call memory, and webhooks can persist after the immediate task is finished.

Mitigation: Review persistent settings after setup, monitor usage, and disable inbound AI, cancel schedules, remove BYOK keys, or turn off memory when they are no longer needed.

Risk: Call recording and call memory can capture sensitive conversations and may require disclosure or consent depending on the jurisdiction and use case.

Mitigation: Default recording to off unless the user opts in, disclose recording in call prompts, and use memory deletion or purge workflows when retention is no longer appropriate.

Risk: Outbound calls, SMS, and proactive schedules may fail due to account restrictions, A2P registration state, opt-outs, carrier limits, or unsupported destinations.

Mitigation: Surface API error codes and delivery state to the user, avoid retry loops, and verify sender registration, destination eligibility, and STOP status before repeated outreach.

Risk: Webhook integrations can duplicate events or accept forged payloads if the receiving service does not validate delivery.

Mitigation: Verify AgentCall HMAC signatures, deduplicate by call or message identifiers, and store webhook payloads before asynchronous agent processing.

## Reference(s):

- [AgentCall Skill Page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API Reference](https://api.agentcall.co/llms.txt)
- [AgentCall Pricing](https://agentcall.co/#pricing)
- [AgentCall Voice Prompt Guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Pre-call Context Walkthrough](https://agentcall.co/docs/hermes)
- [AgentCall Post-call Webhook Walkthrough](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with REST examples, JSON request and response shapes, and operational checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AgentCall API key for authenticated operations; many workflows affect real phone numbers, real recipients, billing, or persistent account state.]

## Skill Version(s):

2.12.6 (source: server release metadata and artifact/claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
