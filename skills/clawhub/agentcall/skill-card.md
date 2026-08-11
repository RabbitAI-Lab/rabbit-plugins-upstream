## Description:

AgentCall gives agents access to phone numbers, SMS, OTP retrieval for owned apps, voice calls, AI voice receptionists, two-way AI SMS or relay mode, proactive schedules, and call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent provision and manage AgentCall phone numbers, send and receive SMS, place voice or AI voice calls, configure AI receptionists, and retrieve call records or memory. It is suited to telephony workflows where the user authorizes real-world contact, costs, recording, scheduling, and memory behavior.

### Deployment Geography for Use:

Global, subject to AgentCall telephony availability and documented US/Canada limits for AI voice capabilities.

## Known Risks and Mitigations:

Risk: The skill can cause real-world contact and spend through SMS, voice calls, AI voice, phone-number provisioning, recording, premium voice, and proactive schedules.

Mitigation: Confirm recipients, messages, call prompts, schedules, recording settings, and expected costs with the user before taking these actions.

Risk: Call recording and call memory can capture privacy-sensitive conversation data.

Mitigation: Enable recording or memory only when appropriate for callers, disclose recording where required, and use the documented delete, purge, disable, and review controls when data should no longer be retained or used.

Risk: Inbound AI configuration can keep answering future calls and accumulating usage after initial setup.

Mitigation: Use the documented pre-flight checklist, monitor usage, and disable inbound AI when testing, campaigns, or seasonal needs are complete.

Risk: Webhook integrations can receive sensitive call, SMS, transcript, recording, and report events.

Mitigation: Use HTTPS endpoints, verify HMAC signatures, deduplicate delivery by event or call identifier, and acknowledge only after the event is safely persisted or queued.

## Reference(s):

- [AgentCall ClawHub skill page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall pricing](https://agentcall.co/#pricing)
- [Voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [Pre-call context walkthrough](https://agentcall.co/docs/hermes)
- [Post-call webhook walkthrough](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with REST examples, JSON request bodies, and occasional curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AgentCall API key for authenticated account operations.]

## Skill Version(s):

2.12.7 (source: evidence release.version and artifact claw.json version; released 2026-08-10 per artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
