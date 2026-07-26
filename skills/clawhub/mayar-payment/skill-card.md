## Description: <br>
Integrates Mayar.id payments so agents can create invoices and payment links, track transactions, manage subscriptions, and support Indonesian payment workflows through MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ahsanatha](https://clawhub.ai/user/ahsanatha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to a Mayar.id account for invoice creation, payment-link generation, transaction reporting, webhook setup, and customer payment messaging. It is most relevant for Indonesian e-commerce, services, memberships, and digital product workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents using this skill can access a live Mayar payment account and initiate payment-related actions such as invoices, payment links, webhooks, reports, and customer messages. <br>
Mitigation: Start with sandbox credentials, require explicit human review before sending invoices, webhooks, reports, or WhatsApp messages, and deploy only where live payment-account access is intended. <br>
Risk: Mayar API tokens are sensitive credentials and could expose account access if stored or shared unsafely. <br>
Mitigation: Store tokens in a secret manager or locked-down local configuration, avoid hard-coding credentials, and rotate tokens if they may have been exposed. <br>
Risk: The skill depends on a remote MCP connection, so the package and endpoint source should be trusted before use. <br>
Mitigation: Verify the MCP package/source and endpoint before installation or production use. <br>


## Reference(s): <br>
- [Mayar API Reference](artifact/references/api-reference.md) <br>
- [Mayar Integration Examples](artifact/references/integration-examples.md) <br>
- [Mayar MCP Tools Reference](artifact/references/mcp-tools.md) <br>
- [Mayar Official API Documentation](https://docs.mayar.id/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Mayar MCP tool calls, API endpoint references, invoice payload examples, and payment workflow checklists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
