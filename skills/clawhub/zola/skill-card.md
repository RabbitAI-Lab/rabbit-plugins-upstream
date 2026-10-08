## Description:

Helps agents retrieve and manage Zola wedding planning information, including vendors, budgets, guests, seating, events, RSVPs, registries, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People planning a wedding can ask an agent to review and manage their Zola vendors, budget, guests, seating, invitations, RSVPs, registry, and gifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive wedding and guest information may expose private details.

Mitigation: Install only when the agent is intended to access and manage the user's Zola wedding account data.

Risk: Write or delete actions can change addresses, budgets, seating, invitations, or guest records.

Mitigation: Require explicit confirmation before these actions and ensure each request is specifically about Zola.

## Reference(s):

- [Zola skill on ClawHub](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may summarize account data or confirm requested changes.]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
