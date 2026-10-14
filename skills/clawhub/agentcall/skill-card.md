## Description:

Helps agents manage phone numbers, SMS, AI voice calls, and opt-in call memory through AgentCall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AgentCall users can equip an agent to provision numbers, exchange texts, handle inbound calls, place authorized outbound calls, and use opt-in call memory.

### Deployment Geography for Use:

United States and Canada for phone numbers and AI voice; other destinations depend on carrier and account restrictions.

## Known Risks and Mitigations:

Risk: Number provisioning, calls, texts, and persistent inbound configurations can incur charges.

Mitigation: Check account limits and costs, and obtain the user's approval before paid actions; disable inbound AI when no longer needed.

Risk: Outbound calls and messages contact real people.

Mitigation: Confirm the recipient, content or call purpose, and the user's authorization before outreach.

Risk: Recording and call memory may retain sensitive conversations.

Mitigation: Review applicable recording consent rules and retention settings; enable recording or memory only with informed approval.

Risk: Webhook destinations and bring-your-own-key settings can expose call data or credentials.

Mitigation: Review webhook endpoints and access controls, and handle provider keys securely before enabling these features.

## Reference(s):

- [AgentCall skill listing](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [Voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [Post-call webhook guide](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls, Configuration]

**Output Format:** [Markdown guidance and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide real-world telephony actions through an authenticated AgentCall account.]

## Skill Version(s):

2.14.0 (source: ClawHub release metadata and skill manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
