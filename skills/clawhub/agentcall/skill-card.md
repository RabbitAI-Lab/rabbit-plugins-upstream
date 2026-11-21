## Description:

Manage phone numbers, SMS, and AI voice through AgentCall, including OTP retrieval for apps you control and call-memory tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kintupercy](https://clawhub.ai/user/kintupercy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to give agents a business phone number for messaging and calls, configure AI receptionists, and work with call records and memory. Phone numbers and AI voice are supported in the United States and Canada.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with high confidence and flags guidance that could interrupt incoming calls if inbound AI is disabled during a billing or call investigation without confirming the affected number or getting approval.

Mitigation: Review the instructions before installation, verify the affected number and destination, and confirm authorization before changing call service or sending data. Scan coverage was partial, so review the remaining components as well.

## Reference(s):

- [AgentCall API reference](https://api.agentcall.co/llms.txt)
- [AgentCall voice prompt guide](https://agentcall.co/docs/voice-prompts)
- [AgentCall post-call webhook guide](https://agentcall.co/docs/post-call-webhook)
- [AgentCall on ClawHub](https://clawhub.ai/kintupercy/skills/agentcall)

## Skill Output:

**Output Type(s):** [API calls, Configuration, Text and call data, Guidance]

**Output Format:** [JSON API requests and responses with human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions contact real people, change call handling, or incur charges; confirm the user's authorization and check current account limits before acting.]

## Skill Version(s):

2.15.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
