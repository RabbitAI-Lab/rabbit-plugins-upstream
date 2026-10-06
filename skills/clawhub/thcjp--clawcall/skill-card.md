## Description:

语音通话服务 enables an agent to place real US phone calls, handle menus or wait time, bridge a user into live calls, and return call outcomes, transcripts, and recording links when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to delegate US phone calls for reservations, price checks, customer-service queues, order confirmations, account workflows, and inbound call handling. It is not suitable for emergency help or decisions requiring 100% certainty.

### Deployment Geography for Use:

United States phone calls; agent usage otherwise Global

## Known Risks and Mitigations:

Risk: Overbroad activation text may lead an agent to use the skill for coding, generic automation, or other non-call tasks.

Mitigation: Invoke it only for explicit phone-call, live-bridge, inbound-call, or call-preference tasks.

Risk: Stored API keys, user phone numbers, transcripts, and recording links can expose sensitive personal or account information.

Mitigation: Do not allow storage or reuse of API keys or phone numbers unless the user understands where the data is kept and how to remove it; treat transcripts and recording links as sensitive.

Risk: Calls may involve consent, recording rules, identity verification, OTPs, payment details, or real-time commitments.

Mitigation: Confirm user consent and applicable recording rules before calls, avoid collecting passwords or expired OTPs in advance, and bridge the user into sensitive or decision-heavy calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/clawcall)
- [Voice Call API base URL](https://api.voicecall.example)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce call IDs, lifecycle status, call outcomes, transcripts, recording links, and call-preference configuration.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
