## Description:

uupaotui helps agents use UU Paotui local delivery services to quote, create, track, cancel, and inspect orders, register users, and claim coupons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to arrange local courier and errand services through UU Paotui, including price checks, order placement, payment handoff, order lookup, cancellation, courier tracking, and coupon claiming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and cancel real delivery orders and expose payment handoff links.

Mitigation: Require explicit user confirmation before order creation, cancellation, or payment handoff, and review all addresses, phone numbers, notes, and price tokens before execution.

Risk: The skill stores account identifiers locally and may display personal delivery details such as order, courier, contact, and location information.

Mitigation: Use it only on trusted hosts, protect the local configuration file, and avoid sharing order output in public or multi-user channels.

Risk: The skill can silently replace its own code and run package installation in the background.

Mitigation: Disable or remove the self-update path in sensitive environments, pin reviewed versions, and require manual review before accepting updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/uupt-mcp/skills/uu-paotui)
- [UU Paotui Open Platform](https://open.uupt.com)
- [UU Paotui Agent Skill documentation](https://open.uupt.com/#/development/ai/agentSkill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with command invocations, JSON-like API result summaries, payment links, QR-code image references, and order status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce order identifiers, courier contact/location details, coupon tables, payment handoff URLs, and local account configuration updates.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter and package.json report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
