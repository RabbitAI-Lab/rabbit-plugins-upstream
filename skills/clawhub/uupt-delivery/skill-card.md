## Description:

UU跑腿同城配送服务，帮助代理处理同城帮送、帮取、帮买和现场帮办任务，并支持询价、下单、订单查询、取消订单和跑男位置追踪。

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to arrange local UU Paotui delivery or on-site errand services, including price checks, order creation, payment handoff, order lookup, cancellation, and courier tracking. It is appropriate only when the user intends to interact with real delivery services and provides the required phone, address, and order details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send phone numbers, addresses, public IP information, order details, and payment links to external services, and can create real delivery orders.

Mitigation: Require explicit user confirmation before paid or real-world actions, verify address and phone details before submission, and share only the minimum information needed for the requested order.

Risk: The security evidence reports a hidden self-updater that can download and install new code in the background without user approval.

Mitigation: Disable or remove the updater before installation, pin the reviewed release, and apply future updates only after review and scanning in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/uupt-mcp/skills/uupt-delivery)
- [UU Paotui Open Platform](https://open.uupt.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured command output such as order IDs, price tokens, payment links, and QR-code file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce real service actions through external APIs and may require phone numbers, addresses, public IP information, order details, and payment links.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
