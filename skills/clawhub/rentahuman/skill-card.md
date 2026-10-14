## Description:

Helps agents find and hire people for physical-world tasks through RentAHuman.ai, including searching profiles, posting bounties, reviewing applications, and coordinating work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to find workers for in-person tasks, post paid bounties, review applicants, and coordinate completion through RentAHuman.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bounty can be posted without the preview and confirmation flow, potentially committing funds or accepting workers under unintended terms.

Mitigation: Show the dry-run preview, total funding impact, worker auto-accept settings, and task details; obtain explicit approval before posting.

Risk: Real-world tasks can expose addresses, access codes, IDs, package tracking, schedules, or other people's personal information.

Mitigation: Share only necessary details with consent, and avoid including sensitive personal information in bounty descriptions or messages.

## Reference(s):

- [RentAHuman API reference](references/API.md)
- [RentAHuman](https://rentahuman.ai)
- [ClawHub skill release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and commands; JSON responses from marketplace operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browsing is public; posting bounties, messaging, and managing applications require a RentAHuman API key.]

## Skill Version(s):

3.11.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
