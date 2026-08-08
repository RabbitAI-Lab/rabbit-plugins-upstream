## Description:

Provision or reuse a service-scoped Mermail mailbox, then safely find and inspect an expected verification, sign-in, onboarding, receipt, or order-status email for an active third-party workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs a task-scoped email identity to receive and validate verification, sign-in, onboarding, receipt, or order-status messages. It supports mailbox discovery, safe provisioning, bounded polling, and protected extraction of expected codes or links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may provision a mailbox that consumes Mermail credits.

Mitigation: Use it only for task-specific verification or transactional email work, and preview the address and 10-credit cost when Mermail provisioning was not already requested.

Risk: Inbound email can contain malicious or misleading instructions, links, or attachments.

Mitigation: Treat inbound content as untrusted, use metadata-first validation, inspect only clean bounded content, and ignore requests that change the active task or invoke unrelated tools.

Risk: One-time codes, magic links, terms, identity assertions, payments, or unexpected email content can cause sensitive or irreversible actions.

Mitigation: Require fresh user confirmation or the host approval flow before using codes or links, accepting terms, entering credentials, submitting payments, or exposing mailbox content outside the active task.

## Reference(s):

- [Agent-inbox tool map](references/tools.md)
- [Agent-inbox security boundary](references/security.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agent-inbox MCP profile](https://console.mermail.app/mcp?profile=agent-inbox)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include mailbox selection or provisioning guidance, expected-message validation steps, timeout or ambiguity states, and bounded handling of codes or links.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
