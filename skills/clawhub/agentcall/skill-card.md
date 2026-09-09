## Description:

AgentCall gives agents access to phone numbers, SMS, voice calls, inbound and outbound AI voice, two-way SMS modes, scheduling, and auditable call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use AgentCall to let an AI agent provision and manage supported phone numbers, send SMS, initiate or answer calls, configure AI receptionists, handle webhooks, and retrieve transcripts, recordings, reports, and caller memory. It is intended for workflows where the user explicitly authorizes real-world telephony actions and accepts the associated plan limits and costs.

### Deployment Geography for Use:

Global, with telephony features limited to supported US/Canada numbers and carrier coverage where documented.

## Known Risks and Mitigations:

Risk: The skill can trigger billable or external-effect actions such as provisioning numbers, sending SMS, placing calls, enabling AI voice, recording calls, or creating proactive schedules.

Mitigation: Require explicit user confirmation for the recipient, number, message or prompt, timing, plan status, and cost before invoking those actions; call get_plan or GET /v1/account before quoting allowances or retrying paid actions.

Risk: Persistent inbound AI, scheduled texts, webhooks, call memory, and recordings can continue affecting users after initial setup.

Mitigation: Enable them only with a monitoring plan, restrict webhook destinations to endpoints the user controls, periodically check usage, and disable inbound AI, schedules, recording, or memory when no longer needed.

Risk: Remote references, webhook context, call transcripts, recordings, and stored memory may contain sensitive data or prompt-injected content that influences later calls or messages.

Mitigation: Treat remote guidance, webhook content, transcripts, recordings, and memory as untrusted input; keep confirmations on for paid or external-effect actions and purge or disable stored memory when the user requests it.

Risk: New account trial limits, payment recovery, destination verification, and carrier restrictions can cause failures that should not be retried blindly.

Mitigation: Surface payment, trial, quota, verification, carrier, and rate-limit errors to the user; stop retrying blocked actions and share setup or upgrade links only when the user wants to proceed.

## Reference(s):

- [AgentCall ClawHub listing](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Hermes context webhook guide](https://agentcall.co/docs/hermes)
- [AgentCall billing](https://agentcall.co/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with API examples, configuration instructions, shell commands, and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include phone number records, SMS status, call records, transcripts, recording links, webhook payloads, account plan details, and caller memory returned by AgentCall.]

## Skill Version(s):

2.13.1 (source: server release evidence and artifact claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
