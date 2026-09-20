## Description:

This skill should be used when the user asks about Zola wedding planning data. Triggers on phrases like "check Zola", "Zola vendors", "wedding budget", "Zola guests", "RSVP status", "seating chart", "vendor inquiries", "wedding registry", "gift tracker", or any request involving wedding vendors, guest list, budget, seating, events, registry, or inquiry management on Zola.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent work with Zola wedding planning data, including vendors, budgets, guests, seating charts, inquiries, events, RSVPs, registry items, gifts, and planning dashboard information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad Zola account-changing capabilities across guests, vendors, budget, seating, registry, and invitations.

Mitigation: Require explicit Zola intent and user confirmation before changing or deleting wedding records.

Risk: A user may unintentionally invoke actions that alter wedding planning data.

Mitigation: Review the requested operation and affected records before installing or enabling the skill for account-changing use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text with tool-backed wedding planning results and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-changing Zola actions through MCP tools when the user authorizes those operations.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
