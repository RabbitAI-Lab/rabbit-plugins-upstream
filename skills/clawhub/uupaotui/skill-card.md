## Description:

UU跑腿 helps an agent price, create, manage, cancel, and track same-city courier or errand orders and claim related coupons through UU Paotui services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to arrange real same-city delivery, pickup, purchase, onsite assistance, coupon claiming, order lookup, cancellation, and courier tracking through UU跑腿 workflows.

### Deployment Geography for Use:

China, limited to UU跑腿 supported service areas

## Known Risks and Mitigations:

Risk: The skill can create real delivery or errand orders and may generate payment links.

Mitigation: Confirm the user's intent, addresses, phone numbers, order details, and payment context before running order creation or cancellation workflows.

Risk: The security summary reports silent background updates that can replace skill code and run dependency installation without a prompt.

Mitigation: Review or disable self-update behavior before deployment, pin the validated release, and inspect update sources before executing updated code.

Risk: The security guidance says the skill handles phone numbers, addresses, order details, public IP lookup, payment links, and courier tracking data.

Mitigation: Share only the minimum necessary personal and order data, restrict access to saved configuration, and remove stored credentials or identifiers when no longer needed.

## Reference(s):

- [UU跑腿开放平台](https://open.uupt.com)
- [ClawHub skill page](https://clawhub.ai/uupt-mcp/skills/uupaotui)
- [ClawHub publisher profile](https://clawhub.ai/user/uupt-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with command outputs, order status summaries, payment or coupon links, QR image references, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce payment links, coupon details, local or remote QR image references, and saved registration configuration.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact SKILL.md and package.json report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
