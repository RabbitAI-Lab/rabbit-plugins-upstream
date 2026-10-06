## Description:

Helps users review and manage Zola wedding-planning data, including vendors, budgets, guests, events, seating, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People planning a wedding use this skill to review their Zola account information and request changes to vendors, budgets, guest lists, seating, invitations, and events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable operations can change sensitive wedding-account data without clear confirmation boundaries.

Mitigation: Require explicit confirmation before adding, updating, removing, inviting, assigning seats, changing budgets, or making bulk invitation changes.

Risk: Broad wedding-planning triggers may lead to unnecessary access to Zola account data.

Mitigation: Use the skill only when the request requires Zola account access; give general planning advice without accessing the account.

## Reference(s):

- [Zola skill on ClawHub](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown summaries of Zola account information and requested actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report wedding-account data or request changes to that account.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
