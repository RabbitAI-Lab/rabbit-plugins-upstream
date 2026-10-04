## Description:

Guides an agent in reading a user's SimplePractice Client Portal for appointments, billing, paperwork, payment methods, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and authorized representatives use the skill to ask an agent about their portal appointments, balances, insurance superbills, outstanding forms, and announcements. The agent should confirm which client's record is being discussed when a login covers multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal reads can expose sensitive medical, billing, and saved payment information.

Mitigation: Use only an account the user is authorized to access, report only the requested information, and sign out when the session should no longer be reused.

Risk: A portal login may cover several clients, including family members.

Mitigation: Confirm the intended client before sharing any record.

## Reference(s):

- [SimplePractice skill release on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain-text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes authorized portal reads; does not cancel appointments, sign forms, or pay bills.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
