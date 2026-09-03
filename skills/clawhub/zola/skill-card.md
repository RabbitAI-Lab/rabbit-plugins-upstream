## Description:

This skill helps agents access and manage Zola wedding planning data, including vendors, budgets, guests, seating, RSVPs, registry items, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning weddings can use this skill through an agent to review and manage Zola workflows such as guest lists, RSVPs, seating, vendors, budget, registry, and gifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive wedding planning data, including guests, addresses, RSVPs, seating, budgets, vendors, registry items, and gifts.

Mitigation: Enable it only when the user intends to grant agent access to Zola data, and review how retrieved personal or event data will be handled before use.

Risk: The skill includes mutating actions for guests, addresses, RSVPs, seating, budgets, invitations, vendors, registry, and gifts without clear scoping or confirmation guidance.

Mitigation: Require explicit user confirmation before any action that creates, updates, deletes, invites, removes, assigns, reconciles, or otherwise changes Zola data.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zola wedding planning data such as guests, addresses, RSVPs, seating assignments, budget items, vendors, registry items, and gift tracker details.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
