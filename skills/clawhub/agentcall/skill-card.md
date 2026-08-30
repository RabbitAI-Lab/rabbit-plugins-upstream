## Description:

AgentCall gives agents access to phone numbers, SMS, OTP retrieval for owned apps, inbound and outbound voice calls, AI voice receptionists, two-way AI SMS, scheduling, webhooks, text-to-speech, and auditable call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent manage AgentCall telephony workflows, including provisioning numbers, sending and receiving texts, placing calls, configuring AI receptionists, handling webhooks, and reviewing call memory. It is intended for users who want an agent to perform real phone or messaging operations with explicit confirmation for costly, irreversible, or external-effect actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact real people by SMS or voice call and can configure agents to answer incoming calls or texts.

Mitigation: Confirm recipient numbers, message or call content, schedules, recording settings, and user authorization before initiating contact or enabling persistent inbound behavior.

Risk: Provisioning numbers, sending texts, placing calls, AI voice usage, premium voice, recording, text-to-speech, and Pro upgrades can incur subscription or usage-based costs.

Mitigation: Review the plan, current limits, expected usage, and per-action pricing with the user before authorizing billable operations or upgrade flows.

Risk: BYOK mode handles customer-supplied AI provider keys for inbound AI voice billing.

Mitigation: Confirm the exact number, billing mode change, and key-handling intent before setting or removing BYOK credentials.

Risk: Call recordings and transcript or memory features may capture sensitive personal or business information.

Mitigation: Use explicit recording opt-in, disclose recording where required, review notification destinations, and disable or purge memory when it is no longer needed.

## Reference(s):

- [ClawHub AgentCall Listing](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API Reference](https://api.agentcall.co/llms.txt)
- [AgentCall Voice Prompt Guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Post-Call Webhook Walkthrough](https://agentcall.co/docs/post-call-webhook)
- [AgentCall Billing](https://agentcall.co/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline API examples, JSON request and response shapes, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to make authenticated AgentCall API calls that contact real people, create persistent telephony configuration, or incur subscription and per-minute costs.]

## Skill Version(s):

2.13.0 (source: server release metadata and artifact claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
