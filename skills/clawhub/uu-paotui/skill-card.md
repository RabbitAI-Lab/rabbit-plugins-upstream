## Description:

uupaotui helps agents quote, create, manage, cancel, and track UU Paotui intra-city delivery and onsite assistance orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill through an agent to estimate costs, place or cancel delivery and onsite-assistance orders, and retrieve order details or courier tracking. It is intended for workflows that can safely handle local authorization data, payment links, addresses, phone numbers, and real-world service orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place or cancel real-world paid delivery and assistance orders.

Mitigation: Require a final user confirmation that shows address, phone number, service details, and price before creating or canceling an order.

Risk: The skill can silently replace its own code from a remote update source.

Mitigation: Disable silent self-updates or make updates explicit, signed, and user-approved before installation.

Risk: The skill stores delivery authorization data locally and sends delivery or payment data to external services.

Mitigation: Install only after reviewing local credential storage and external data sharing, and limit use to contexts where the user accepts those data flows.

## Reference(s):

- [UU Paotui Open Platform](https://open.uupt.com)
- [UU Paotui Agent Skill Quick Start](https://open.uupt.com/#/development/agentSkill/quickStart)
- [ClawHub Skill Listing](https://clawhub.ai/uupt-mcp/skills/uu-paotui)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with shell command examples and JSON-style status fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output payment links, order codes, QR code file paths, local configuration paths, and delivery tracking details.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter and package.json report 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
