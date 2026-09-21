## Description:

Manage Sendmux domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations administrators use this skill to guide Sendmux account-management work across domains, mailboxes, sending accounts, webhooks, logs, billing, and permission checks. It helps an agent choose the right Sendmux surface, produce CLI or SDK examples, and route mailbox or setup tasks to the appropriate companion skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using broad Sendmux credentials could perform account-level management actions beyond the user's immediate task.

Mitigation: Use the narrowest Sendmux credential or OAuth scopes that fit the requested operation, and keep root keys in a secret store.

Risk: Destructive or sensitive operations such as deletes, suspensions, key changes, webhook secret rotations, or test sends could affect the wrong resource.

Mitigation: Verify resource names and ask for confirmation before approving those operations.

Risk: One-time mailbox keys or webhook secrets could be exposed if printed into chat or reused incorrectly.

Mitigation: Write one-time secrets only to the user's chosen secret store or secure output path.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-management)
- [Publisher profile](https://clawhub.ai/user/sendmux.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline bash, JSON, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-scope, routing, confirmation, and secret-handling guidance for Sendmux management operations.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
