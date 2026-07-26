## Description: <br>
Mayar.id Payment helps agents generate invoices and payment links, track transactions, manage subscriptions, and support Indonesian payment workflows through the Mayar MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ahsanatha](https://clawhub.ai/user/ahsanatha) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to Mayar.id payment workflows for invoice creation, payment-link generation, transaction checks, customer messaging, and membership or subscription handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent access to live payment-account operations and customer messaging workflows. <br>
Mitigation: Use sandbox first and require human confirmation before creating invoices, sending payment messages, or taking customer-facing payment actions. <br>
Risk: Mayar API tokens and customer or transaction data could be exposed if stored in shared configuration or passed through visible command arguments. <br>
Mitigation: Use safer secret-management mechanisms when available, avoid sharing raw tokens, restrict access to credential files, and apply privacy and retention controls to customer and transaction data. <br>
Risk: The skill depends on a remote Mayar MCP endpoint with broad payment and account capabilities. <br>
Mitigation: Install only when the Mayar MCP endpoint is trusted and review the configured tool scope before production use. <br>


## Reference(s): <br>
- [MCP Tools Reference](references/mcp-tools.md) <br>
- [Integration Examples](references/integration-examples.md) <br>
- [API Reference](references/api-reference.md) <br>
- [Mayar API Documentation](https://docs.mayar.id/api-reference/introduction) <br>
- [ClawHub Skill Page](https://clawhub.ai/ahsanatha/skills/mayar-payment-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Mayar MCP tool names, request fields, payment-link handling guidance, webhook guidance, and transaction-status workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
