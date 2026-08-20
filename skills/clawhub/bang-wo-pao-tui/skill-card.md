## Description:

帮我跑腿 enables an agent to price, create, query, cancel, and track UU same-city delivery and errand orders, including send, pick-up, buying, and on-site help services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to arrange real-world same-city delivery and errand services through UU, including fee estimates, order creation, payment handoff, order status checks, cancellation, and courier tracking.

### Deployment Geography for Use:

China, subject to UU service availability.

## Known Risks and Mitigations:

Risk: The skill can create or cancel real-world paid delivery and errand orders with limited confirmation safeguards.

Mitigation: Require explicit human confirmation before running order creation or cancellation commands, including review of addresses, phone numbers, notes, price, and cancellation fees.

Risk: The skill can display sensitive order, recipient, address, phone, payment, and courier information.

Mitigation: Redact sensitive fields in shared logs and responses, and limit use to environments where local configuration and output files are protected.

Risk: The skill can contact UU and other network services and stores an authorization identifier locally.

Mitigation: Install only after reviewing the network behavior and store local configuration with least-privilege file permissions.

Risk: The skill includes behavior that can silently replace its installed code from a remote update source.

Mitigation: Disable silent self-update, use platform-managed updates, and review and scan any new version before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/uupt-mcp/skills/bang-wo-pao-tui)
- [UU Open Platform](https://open.uupt.com)
- [UU Open API v3 Endpoint](https://api-open.uupt.com/openapi/v3/)
- [UU Agent Skill Quick Start](https://open.uupt.com/#/development/agentSkill/quickStart)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON, Files]

**Output Format:** [Markdown guidance with shell commands, structured script output, payment links, and optional QR-code image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local authorization/configuration files and payment QR-code files.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
