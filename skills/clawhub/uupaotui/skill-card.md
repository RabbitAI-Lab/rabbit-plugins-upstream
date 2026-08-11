## Description:

UU跑腿 provides intra-city delivery and on-site help services, including price quotes, order placement, order lookup, cancellation, and courier tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to price, create, manage, cancel, and track local UU跑腿 delivery or on-site assistance orders.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can place real paid delivery or on-site service orders using phone numbers, addresses, payment flows, order status, and courier tracking.

Mitigation: Review order details, payment requirements, and user intent before deployment and before allowing actions that create or pay for real service orders.

Risk: Evidence.security reports that the skill can silently replace its own code through background updates without user approval.

Mitigation: Pin a reviewed version, disable or remove background self-update behavior where possible, and rescan any updated package before use.

## Reference(s):

- [UU Open Platform](https://open.uupt.com)
- [ClawHub skill page](https://clawhub.ai/uupt-mcp/skills/uupaotui)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown text with inline shell commands and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment links, order identifiers, order status, and courier tracking details.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
