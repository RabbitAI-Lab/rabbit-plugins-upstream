## Description:

Use Axiom Wallet via MCP to manage payment methods, review account activity, and complete user-requested purchases through Axiom's server-managed browser checkout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[axiom-wallet](https://clawhub.ai/user/axiom-wallet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to connect to Axiom Wallet over MCP, inspect saved payment and transaction information, and complete user-requested purchases through Axiom's managed checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a payment wallet and can start user-requested purchases against a saved card.

Mitigation: Verify the saved payment method before purchase, start purchases only from clear user requests, preserve approval flows, and treat mandate denials or policy blocks as terminal outcomes.

Risk: The documented temporary-file OAuth URL interception fallback can expose live authentication setup material.

Mitigation: Prefer the normal mcporter log-based or browser-based authentication flow; if the fallback is unavoidable, protect the captured file path and delete the file immediately after use.

Risk: Purchase state can be misreported if polling is stopped too early or internal browser progress is inferred.

Mitigation: Poll get_purchase_status until a documented terminal or approval state is returned, and never claim success unless the returned status is completed.

## Reference(s):

- [Authentication guide](references/authentication.md)
- [Axiom Wallet ClawHub homepage](https://clawhub.ai/axiom-wallet/axiom)
- [Axiom skill page](https://clawhub.ai/axiom-wallet/skills/axiom)
- [Axiom MCP endpoint](https://mcp.useaxiom.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides OAuth setup, payment-method checks, transaction review, purchase initiation, status polling, and user approval handoffs.]

## Skill Version(s):

0.1.1 (source: server release evidence and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
