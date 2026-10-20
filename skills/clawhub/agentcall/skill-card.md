## Description:

Enables agents to manage phone numbers, SMS, voice calls, AI receptionists, and call memory through AgentCall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use AgentCall to provision phone numbers, send and receive texts, place calls, configure AI voice receptionists, and manage caller context.

### Deployment Geography for Use:

United States and Canada for phone number provisioning

## Known Risks and Mitigations:

Risk: Provisioning numbers, outbound communications, AI calling, and recurring schedules can create charges and contact real people.

Mitigation: Check current account limits and costs, confirm the recipient and scope with the user before acting, and monitor ongoing usage.

Risk: Call recording, stored caller memory, and BYOK credentials can expose sensitive information or create consent obligations.

Mitigation: Enable these features only with explicit authorization; review applicable recording and privacy requirements and limit access to keys and call data.

## Reference(s):

- [AgentCall skill release](https://clawhub.ai/kintupercy/skills/agentcall)
- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall post-call webhook guide](https://agentcall.co/docs/post-call-webhook)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration instructions, Text]

**Output Format:** [Markdown and structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate real-world communications and persistent account changes.]

## Skill Version(s):

2.14.1 (source: ClawHub release metadata and claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
