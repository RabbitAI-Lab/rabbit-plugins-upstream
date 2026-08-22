## Description:

uupaotui lets an agent quote, place, inspect, cancel, and track UU Paotui same-city delivery and errand orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving users who need same-city courier, pickup, purchasing, or errand help can use this skill to estimate costs, create UU Paotui orders, provide payment links when needed, view order details, cancel orders, and track couriers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles phone numbers, SMS codes, addresses, payment links, and courier details.

Mitigation: Use it only in trusted environments, collect only the information needed for the order, and protect the saved openId and local configuration files.

Risk: The skill can create paid real-world delivery or errand orders without a final confirmation.

Mitigation: Require an explicit user confirmation after price review and before running the create-order command.

Risk: The skill includes a silent self-update path that can replace its own code from a remote source.

Mitigation: Disable or remove silent self-update behavior and pin a reviewed version before operational use.

## Reference(s):

- [UU Paotui Open Platform](https://open.uupt.com)
- [ClawHub Skill Page](https://clawhub.ai/uupt-mcp/skills/uu-paotui)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local configuration and payment QR-code files during registration or payment flows.]

## Skill Version(s):

1.0.9 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
