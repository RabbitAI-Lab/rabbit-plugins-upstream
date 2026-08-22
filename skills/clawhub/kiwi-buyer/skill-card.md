## Description:

Guides agents through Kiwi procurement workflows for supplier discovery, quote requests, offer comparison, negotiation, non-binding agreement acceptance, and checkout or purchase-order handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[harrylabsj](https://clawhub.ai/user/harrylabsj)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and purchasing assistants use this skill to guide procurement conversations through Kiwi buyer tools for supplier discovery, RFQs, quote comparison, negotiation, user-confirmed approvals, and handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user or agent could approve an agreement or handoff without fully confirming procurement terms.

Mitigation: Present quote and agreement summaries to the user and only run approval or handoff actions after explicit confirmation.

Risk: The skill depends on Kiwi procurement tools and is not useful in environments that do not intend to use the Kiwi plugin.

Mitigation: Install and use it only for Kiwi procurement workflows with the Kiwi plugin available.

Risk: The workflow forms non-binding agreements and handoff links but does not handle payment, order creation, or inventory reservation.

Mitigation: Confirm downstream checkout, purchase order, payment, and fulfillment steps outside the skill before treating a purchase as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/harrylabsj/skills/kiwi-buyer)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown instructions with tool names, workflow steps, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Kiwi plugin tools named kiwi_buyer_*; approval and handoff actions require explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
