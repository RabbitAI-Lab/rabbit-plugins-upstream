## Description:

AgentCall gives agents access to phone numbers, SMS, voice calls, inbound and outbound AI voice, proactive text scheduling, and auditable call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent provision phone numbers, send and receive SMS, place calls, configure AI receptionists, manage call memory, and connect AgentCall events to their own systems. It is best suited for workflows where the user has authorized real-world telephony actions and understands the associated costs, consent duties, and privacy impact.

### Deployment Geography for Use:

Global; carrier-dependent telephony features are documented for US and Canada numbers.

## Known Risks and Mitigations:

Risk: The skill can guide an agent to contact real people by SMS or phone and create persistent inbound AI configurations.

Mitigation: Require explicit user confirmation for recipients, call or message content, system prompts, transfer destinations, recording, schedules, and persistent inbound AI settings before taking action.

Risk: Telephony, AI voice, recording, premium voice, and scheduling features can incur usage-based costs.

Mitigation: Review pricing and plan limits before authorizing billable actions, and monitor or disable persistent configurations when they are no longer needed.

Risk: Calls, recordings, webhooks, BYOK keys, and auditable memory can involve sensitive personal or business information.

Mitigation: Use only trusted endpoints and credentials, follow applicable consent and recording requirements, and review call-memory and webhook settings before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API Reference](https://api.agentcall.co/llms.txt)
- [AgentCall Pricing](https://agentcall.co/#pricing)
- [Hermes Context Webhook Walkthrough](https://agentcall.co/docs/hermes)
- [Voice Prompt Guide](https://agentcall.co/docs/voice-prompts)
- [Post-call Webhook Walkthrough](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with API examples, JSON payloads, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent toward authenticated AgentCall API calls that contact real phone numbers, create persistent configurations, register webhooks, or manage call memory.]

## Skill Version(s):

2.12.5 (source: evidence.release.version and artifact/claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
