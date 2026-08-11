## Description:

帮我跑腿 helps an agent use UU跑腿 local courier and on-site helper services to quote, create, inspect, cancel, and track real-world service orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to arrange same-city delivery or on-site assistance through UU跑腿, including price quotes, order creation, order status checks, cancellation, and courier tracking.

### Deployment Geography for Use:

China, subject to UU跑腿 service coverage.

## Known Risks and Mitigations:

Risk: The skill can create paid real-world delivery or helper orders without a final confirmation step.

Mitigation: Require explicit user confirmation of addresses, recipient phone number, price, service notes, and payment impact before creating an order.

Risk: The skill handles sensitive operational data such as phone numbers, addresses, payment/order links, and courier location details.

Mitigation: Limit disclosure to the active transaction, avoid unnecessary logging or sharing, and confirm the recipient before showing payment or tracking details.

Risk: The bundled updater can silently download replacement code, overwrite the installed skill, and install dependencies.

Mitigation: Disable silent update behavior or require a visible user-approved update flow with provenance and integrity checks before installation.

Risk: Payment QR generation and public IP discovery may disclose transaction or network metadata to third-party services.

Mitigation: Disclose these external services before use and prefer trusted or locally controlled QR-code and network configuration paths.

## Reference(s):

- [UU跑腿开放平台](https://open.uupt.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands, order identifiers, payment links, and status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce payment links, QR-code image paths, order codes, courier contact details, and location/status text.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
