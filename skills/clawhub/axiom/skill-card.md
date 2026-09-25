## Description:

Orders physical products the user asks for through Axiom, using the payment method saved in their Axiom account, checks which payment method Axiom has on file, and reviews past Axiom orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[axiom-wallet](https://clawhub.ai/user/axiom-wallet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to place clearly requested physical-product orders through Axiom, check the saved payment method, and review Axiom order status or receipts. The skill is intended for specific purchase requests, not browsing, price comparison, subscriptions, digital goods, or unrequested orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate real physical-product purchase attempts through the user's Axiom account.

Mitigation: Use it only after a clear user request, confirm merchant, product, and required options before calling purchase tools, and rely on Axiom approval links and spending rules before an order is placed.

Risk: Authentication involves OAuth flow URLs and payment-account access.

Mitigation: Share only the activation URL with the user, never expose OAuth tokens, cookies, browser state, or internal authorization URLs, and reconnect with the required scopes if access is insufficient.

Risk: The documented /tmp PATH interception troubleshooting workaround can alter local command resolution.

Mitigation: Avoid that workaround unless necessary, understand the local PATH risk before using it, and clean up the temporary shim after troubleshooting.

## Reference(s):

- [Axiom ClawHub Page](https://clawhub.ai/axiom-wallet/axiom)
- [Authentication](references/authentication.md)
- [Axiom MCP Tool Reference](references/tool-reference.md)
- [Worked Examples](references/examples.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing order progress, approval, receipt, and troubleshooting guidance while keeping internal tool instructions and identifiers out of user-facing responses.]

## Skill Version(s):

0.2.0 (source: artifact/VERSION and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
