## Description:

This skill should be used when the user asks about Zola wedding planning data. Triggers on phrases like "check Zola", "Zola vendors", "wedding budget", "Zola guests", "RSVP status", "seating chart", "vendor inquiries", "wedding registry", "gift tracker", "wedding website", "Zola FAQ", "invitations", "save the dates", or any request involving wedding vendors, guest list, budget, seating, events, registry, inquiries, the wedding website or invitation projects on Zola.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning a wedding use this skill to review and manage their Zola vendors, budget, guest list, seating, events, registry, invitations, and wedding website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Zola account can expose private guest information or change invitations, registry items, budgets, and public website content.

Mitigation: Connect only through a Zola connector you trust, review bulk or destructive changes before execution, and check how the connector stores and revokes its refresh token.

Risk: The separate connector implementation is not included for verification.

Mitigation: Review the connector and its token controls before connecting a Zola account.

## Reference(s):

- [Zola skill release on ClawHub](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language summaries and responses based on Zola wedding-planning data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include account updates when requested, such as changes to invitations, registry items, budgets, or wedding website content.]

## Skill Version(s):

2.2.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
