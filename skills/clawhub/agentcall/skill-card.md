## Description:

AgentCall lets an agent provision and manage phone numbers for SMS, OTP extraction for controlled apps, voice calls, AI voice receptionists, proactive text schedules, webhooks, and call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give an AI agent controlled telephony capabilities for business messaging, phone-number management, voice calling, AI receptionist setup, post-call records, and related webhook integrations.

### Deployment Geography for Use:

Global, subject to AgentCall carrier and feature restrictions documented for specific telephony paths such as US and Canada support for AI voice features.

## Known Risks and Mitigations:

Risk: Telephony actions can contact real people or incur charges.

Mitigation: Require explicit user confirmation for recipients, message or call purpose, scope, and expected cost before sending SMS, placing calls, scheduling proactive texts, or provisioning numbers.

Risk: Persistent inbound AI can continue answering calls, accumulating usage, and storing conversation data after setup.

Mitigation: Confirm the exact number, prompt, recording setting, notification destinations, duration, and budget before enabling; monitor usage and disable the configuration when it is no longer needed.

Risk: Recording calls and BYOK provider keys introduce privacy and secret-handling concerns.

Mitigation: Confirm recording opt-in and disclosure expectations, confirm BYOK billing-mode changes before storing a provider key, and avoid retrying or probing when API guardrails return plan, payment, or verification errors.

## Reference(s):

- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Hermes walkthrough](https://agentcall.co/docs/hermes)
- [AgentCall post-call webhook walkthrough](https://agentcall.co/docs/post-call-webhook)
- [ClawHub skill page](https://clawhub.ai/kintupercy/skills/agentcall)
- [Publisher profile](https://clawhub.ai/user/kintupercy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API endpoints, JSON request examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated AgentCall API calls that contact real people, incur charges, configure persistent AI receptionists, store call records, or manage webhooks.]

## Skill Version(s):

2.12.2 (source: server release evidence and artifact claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
