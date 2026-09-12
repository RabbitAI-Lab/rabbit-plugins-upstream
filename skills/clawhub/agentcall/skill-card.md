## Description:

AgentCall gives agents access to real phone numbers for SMS, authorized OTP retrieval, voice calls, AI receptionists, proactive messages, and call memory through the AgentCall API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use AgentCall to let an agent provision phone numbers, send and receive SMS, answer or place calls with AI voice, retrieve authorized OTPs, schedule proactive messages, and maintain call memory. It is suited for authorized business communication and agent-to-phone workflows that require user confirmation for real-world actions.

### Deployment Geography for Use:

Global; telephony features depend on AgentCall's documented carrier and destination support.

## Known Risks and Mitigations:

Risk: The skill can make real-world calls, send SMS messages, and trigger billing.

Mitigation: Review costs and require explicit user confirmation before outbound calls, texts, number provisioning, premium voice, recording, schedules, or other paid actions.

Risk: OTP retrieval can be misused against services the user does not control.

Mitigation: Use OTP workflows only for systems the user owns or is authorized to test.

Risk: Call recording and call memory can retain sensitive communications.

Mitigation: Confirm recording consent, monitor retained call memory, and disable or purge configurations when no longer needed.

Risk: Persistent AI receptionists, schedules, and webhooks can continue acting after initial setup.

Mitigation: Monitor active configurations and disable receptionists, schedules, webhooks, or memory when the user's task is complete.

## Reference(s):

- [AgentCall ClawHub Skill Page](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API Reference](https://api.agentcall.co/llms.txt)
- [AgentCall Billing](https://agentcall.co/billing)
- [AgentCall Voice Prompt Guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall Pre-Call Context Webhook Walkthrough](https://agentcall.co/docs/hermes)
- [AgentCall Post-Call Webhook Walkthrough](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API paths, JSON examples, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENTCALL_API_KEY for authenticated AgentCall API actions; some actions can bill money, contact real people, create persistent configurations, or retain call data and must be confirmed with the user.]

## Skill Version(s):

2.13.1 (source: evidence.release.version and artifact/claw.json version; changelog dated 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
