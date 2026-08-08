## Description:

AgentCall gives agents phone numbers for SMS, OTP workflows, voice calls, inbound and outbound AI voice calls, two-way AI SMS, scheduling, and auditable call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA teams, and operators use this skill to give an agent real telephony capabilities: provisioning numbers, sending and receiving SMS, extracting OTP codes for applications they control, configuring AI receptionists, placing AI voice calls, and using call memory for follow-up context. It is suited to customer-facing communication workflows where the agent must confirm recipients, content, recording choices, schedules, and costs before taking action.

### Deployment Geography for Use:

Global, with documented carrier support limits for US and Canada phone and AI voice workflows.

## Known Risks and Mitigations:

Risk: Phone, SMS, AI voice, scheduling, and recording actions can contact real people or incur charges.

Mitigation: Confirm recipient numbers, message or call content, recording choice, language, schedule, and expected cost before invoking side-effecting tools.

Risk: Persistent inbound AI receptionists can keep answering calls and accumulating usage after setup.

Mitigation: Monitor usage and disable inbound AI, schedules, recordings, and memory when the workflow is complete or no longer needed.

Risk: Call recording and post-call artifacts can create consent and privacy obligations.

Mitigation: Default recording to off unless explicitly requested, disclose recording when enabled, and review transcript, recording, and memory behavior with the user.

Risk: Unsupported carrier regions, new-account outbound restrictions, payment gates, or rate limits can make calls or messages fail.

Mitigation: Surface API errors to the user, do not retry blocked destinations blindly, and verify business details or destination authorization when required.

Risk: BYOK voice mode stores a customer-supplied AI provider key for a phone number.

Mitigation: Confirm the specific number, billing-mode change, and key availability before setting BYOK, and remove the BYOK key when managed billing is preferred.

## Reference(s):

- [AgentCall Skill Page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API Plain-Text Reference](https://api.agentcall.co/llms.txt)
- [AgentCall Pricing](https://agentcall.co/#pricing)
- [AgentCall Voice Prompt Guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Pre-Call Context Webhook Walkthrough](https://agentcall.co/docs/hermes)
- [AgentCall Post-Call Webhook Walkthrough](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with REST endpoints, JSON request and response examples, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Side-effecting workflows may contact real people, incur usage costs, configure persistent AI receptionists, store call memory, or change billing mode.]

## Skill Version(s):

2.12.3 (source: server release metadata and claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
