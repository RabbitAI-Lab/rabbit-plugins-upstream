## Description:

Manage Sendmux domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and account administrators use this skill to guide Sendmux team administration, including domain and mailbox setup, sending accounts, webhooks, billing, and delivery monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad management credentials can change account resources and permissions.

Mitigation: Prefer scoped OAuth or a limited profile; check access before each operation.

Risk: Root keys and one-time secrets could be exposed during setup.

Mitigation: Store secrets securely and never request or reveal them in chat.

Risk: Deletion, suspension, provider changes, secret rotation, and webhook tests can disrupt service.

Mitigation: Confirm the target and review the action with the user before execution.

## Reference(s):

- [Sendmux Management on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-management)
- [Sendmux skills homepage (skill metadata)](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires appropriate Sendmux access for account-management operations.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; skill frontmatter lists 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
