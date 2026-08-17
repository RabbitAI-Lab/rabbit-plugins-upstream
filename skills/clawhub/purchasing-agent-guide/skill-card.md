## Description:

Guides agents through a third-party MCP shopping workflow for login, browsing, category selection, USDT checkout, order checks, payment verification, refunds, and messaging while enforcing disclaimer and no-refund confirmations within shopping scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yohyow](https://clawhub.ai/user/yohyow)

### License/Terms of Use:

MIT-0

## Use Case:

External users and MCP-client developers use this skill to configure a third-party purchasing MCP and guide shopping sessions that require login, store browsing, USDT checkout, order status checks, payment verification, refunds, and messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote shopping MCP may ask users for phone or email, password, order information, transaction hash, and USDT payment details.

Mitigation: Use only with a trusted remote MCP operator; do not reuse important passwords, share wallet seed phrases, or provide unrelated secrets.

Risk: USDT purchases through the third-party service may be irreversible or non-refundable.

Mitigation: Require the user to type the no-refund confirmation verbatim, choose the payment network themselves, and verify the exact payment amount, address, and domain before sending funds.

Risk: The server evidence marks the skill suspicious because it combines password collection in chat with third-party USDT purchases.

Mitigation: Review before installation, keep use limited to the documented shopping workflow, and treat all payment details as user-verified rather than agent-trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yohyow/skills/purchasing-agent-guide)
- [MCP setup guide](artifact/mcp-setup.md)
- [Conversation examples](artifact/examples.md)
- [Public MCP endpoint](https://mcp.137449244.xyz/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, inline tool parameters, and user-facing response text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes required user confirmation phrases, payment network selection guidance, and QR-code URL handling for checkout flows.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
