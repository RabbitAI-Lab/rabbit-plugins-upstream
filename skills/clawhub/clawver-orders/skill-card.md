## Description: <br>
Manage Clawver orders by listing orders, tracking fulfillment status, processing refunds, generating download links, and reviewing order history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External store operators and support agents use this skill to inspect customer orders, check fulfillment and payment state, resend digital download links, create webhooks, and prepare refund requests for Clawver stores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Refund guidance can financially affect customers when executed with an owner API key. <br>
Mitigation: Require explicit human confirmation of the order, amount, reason, and payment status before issuing a refund. <br>
Risk: Webhook creation can establish lasting data flows to external destinations. <br>
Mitigation: Allow only trusted webhook URLs, use a strong secret, and review subscribed events before creating or retaining a webhook. <br>
Risk: Download and order-status links can expose customer order data or digital goods. <br>
Mitigation: Treat public tokens and generated links as sensitive customer secrets and share them only through approved support channels. <br>
Risk: Owner order operations require an API key with administrative access. <br>
Mitigation: Use the least-privilege Clawver API key available and avoid exposing it in logs, screenshots, or shared prompts. <br>


## Reference(s): <br>
- [Clawver Orders on ClawHub](https://clawhub.ai/nwang783/skills/clawver-orders) <br>
- [Clawver Store](https://clawver.store) <br>
- [Orders API Examples](references/api-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code] <br>
**Output Format:** [Markdown with curl commands and Python or JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Clawver API key for authenticated owner operations; public status and download URLs require order-specific tokens.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
