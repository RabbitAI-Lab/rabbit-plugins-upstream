## Description:

Foodora-only CLI for checking past orders and active order status (Deliveroo WIP).

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Foodora customers use the skill to check active order status, review past orders and order details, and add a previous order to their cart for reordering. Deliveroo commands are documented as work in progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cookie import and session commands involve account authentication data, and reorder commands can add items to a Foodora cart.

Mitigation: Use only your own account and a trusted local browser profile; review the cart and delivery address before confirming a reorder.

## Reference(s):

- [ordercli homepage](https://ordercli.sh)
- [ordercli on ClawHub](https://clawhub.ai/hillstreet-ph/skills/ordercli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and order information (optionally JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Foodora order status and history; reorder commands can add items to a cart. Deliveroo support is work in progress.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
