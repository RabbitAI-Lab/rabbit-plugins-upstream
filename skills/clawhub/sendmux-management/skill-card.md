## Description: <br>
Manage Sendmux domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and team administrators use this skill to manage Sendmux account resources, including domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sendmux root credentials can administer account-level resources and expose sensitive one-time secrets. <br>
Mitigation: Use scoped Sendmux credentials where possible, keep root keys and generated secrets in a secret store, and do not paste secrets into chat. <br>
Risk: Administrative actions can delete, suspend, rotate, test, or expose account resources, billing data, and logs. <br>
Mitigation: Review confirmations carefully and verify target resources before destructive, high-impact, billing, log, or secret-rotation operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sendmux.ai/skills/sendmux-management) <br>
- [Sendmux Skills Homepage](https://github.com/Sendmux/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, TypeScript code examples, MCP tool names, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes guidance for handling Sendmux credentials, confirmations, pagination, idempotency keys, and concurrency headers.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
