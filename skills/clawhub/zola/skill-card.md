## Description:

This skill helps an agent work with Zola wedding planning data, including vendors, budget, guests, seating, events, RSVPs, registry, and gift tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and update Zola wedding-planning records across vendors, budgets, guests, seating, events, RSVPs, registry items, and gifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private guest, event, budget, vendor, RSVP, registry, and gift data.

Mitigation: Install it only when access to Zola wedding-planning data is intended, and scope use to the specific planning tasks requested.

Risk: The skill can make high-impact changes such as removing guests, changing addresses, altering invitations, updating budgets, or booking and unbooking vendors.

Mitigation: Require explicit confirmation before destructive or high-impact actions are executed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or text summaries of Zola data and requested changes, with API-backed tool actions when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private wedding-planning records and proposed or completed updates.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
