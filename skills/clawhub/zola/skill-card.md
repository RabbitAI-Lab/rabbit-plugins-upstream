## Description:

This skill helps an agent work with Zola wedding planning data, including vendors, budget, guests, seating, inquiries, events, RSVPs, registry items, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and manage wedding planning records in Zola, including vendor bookings, guest lists, RSVP tracking, seating, events, registry reconciliation, and gift tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive wedding account data.

Mitigation: Install only when the agent should access Zola planning data, and limit use to trusted sessions and accounts.

Risk: Write or delete actions can change guests, vendors, events, seating, budget items, or invitations.

Mitigation: Confirm the exact change, affected records, and whether the action can be undone before using write or delete tools.

## Reference(s):

- [ClawHub zola skill listing](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Natural-language responses with optional Markdown summaries of Zola data and proposed account changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate Zola account read, write, or delete actions through configured tools.]

## Skill Version(s):

1.10.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
