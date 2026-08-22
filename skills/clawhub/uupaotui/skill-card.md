## Description:

UU跑腿 helps agents quote, create, pay for, inspect, cancel, and track local delivery and errand orders through UU Paotui services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to arrange local courier delivery, pickup, purchasing, and on-site errand services, including price quotes, order creation, payment handling, order lookup, cancellation, and courier tracking.

### Deployment Geography for Use:

China (service availability depends on UU跑腿 coverage)

## Known Risks and Mitigations:

Risk: The skill can initiate real-world delivery or errand orders and payment flows.

Mitigation: Require explicit final user confirmation of address, phone number, order type, price, and payment channel before creating an order.

Risk: The skill silently self-updates by downloading and installing remote code.

Mitigation: Disable or remove the silent updater and review updates before installation in normal user environments.

Risk: The skill can store an authorization token locally and expose order, payment, and courier details in terminal output.

Mitigation: Protect the local config file, avoid sharing terminal logs, and limit use to environments where this data handling is acceptable.

Risk: The skill may use a third-party QR generation service for payment QR images.

Mitigation: Avoid third-party QR generation where possible and prefer official payment links or trusted QR generation paths.

## Reference(s):

- [UU跑腿开放平台](https://open.uupt.com)
- [ClawHub Skill Page](https://clawhub.ai/uupt-mcp/skills/uupaotui)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash command examples, JSON terminal output, payment links, and optional generated QR-code file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store an authorization token in a local user config file and may print order, payment, and courier details to terminal output.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter, package.json, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
