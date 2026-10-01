## Description:

Helps users find products, prepare and approve purchases through Portage, hand off checkout when needed, and track Portage orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomtom87](https://clawhub.ai/user/tomtom87)

### License/Terms of Use:

MIT-0

## Use Case:

People who explicitly ask an agent to buy or reorder a product use this skill to compare offers, review a checkout total, approve a purchase or finish payment in their browser. It also helps set up Portage and track orders placed through it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A purchase or checkout hand-off could proceed without the user's informed approval of the exact total.

Mitigation: Show the itemized quote and total, obtain explicit approval for that quote, and retain Portage's approval requirement.

Risk: The raw UCP/MCP fallback handles purchasing outside the Portage CLI's built-in safeguards.

Mitigation: Prefer the Portage CLI; avoid the raw fallback unless the store protocol and its checkout safeguards are understood.

Risk: Checkout flows may expose payment details or credentials if shared in chat.

Mitigation: Never provide card numbers or credentials in chat; enter sensitive details only through the user's own secure setup or checkout flow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tomtom87/skills/portage-buy)
- [Portage documentation](https://portage.readthedocs.io/en/latest/)
- [Purchase outcomes and approvals](artifact/references/outcomes.md)
- [Hand-off-only retailers](artifact/references/handoff-only.md)
- [Raw UCP/MCP fallback](artifact/references/raw-ucp.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with offers, purchase summaries, checkout links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval steps and order outcomes when applicable.]

## Skill Version(s):

0.10.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
