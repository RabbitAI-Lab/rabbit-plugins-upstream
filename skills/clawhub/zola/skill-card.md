## Description:

This skill should be used when the user asks about Zola wedding planning data. Triggers on phrases like "check Zola", "Zola vendors", "wedding budget", "Zola guests", "RSVP status", "seating chart", "vendor inquiries", "wedding registry", "gift tracker", "wedding website", "Zola FAQ", "invitations", "save the dates", or any request involving wedding vendors, guest list, budget, seating, events, registry, inquiries, the wedding website or invitation projects on Zola.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to retrieve and manage their Zola wedding-planning information, including vendors, budgets, guests, seating, RSVPs, registry items, invitations, and wedding-website content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guest contact information may be exposed, and actions can change the Zola account or public wedding website.

Mitigation: Use only the guest details needed for the request. Require explicit user direction before deletions, bulk invitation changes, or public edits, and review the MCP server and its credential handling separately.

## Reference(s):

- [Zola skill release on ClawHub](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language summaries and guidance based on Zola wedding-planning data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive guest details or reflect requested changes to wedding-account and public website content.]

## Skill Version(s):

2.1.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
