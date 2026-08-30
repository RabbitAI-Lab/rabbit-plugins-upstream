## Description:

Controls the eppie-console CLI mail client so agents can inspect accounts, folders, messages, and contacts; send mail; sync folders; and manage local vaults with JSON-oriented automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eppieapp](https://clawhub.ai/user/eppieapp)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to automate Eppie CLI email workflows, including mailbox inspection, folder synchronization, message sending, account setup, and vault operations. It is best suited to user-directed tasks where structured JSON output and deterministic command behavior are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and send email, exposing sensitive mailbox contents and enabling unintended outbound messages.

Mitigation: Use it only for clear user-directed tasks and require explicit confirmation before sending mail or reading sensitive message content.

Risk: The skill can delete messages and reset local vault data.

Mitigation: Require explicit confirmation before delete or reset operations, and use disposable vault directories for tests or destructive workflows.

Risk: The skill handles account credentials, vault passwords, and 2FA-related values.

Mitigation: Pass secrets through documented standard-input paths and avoid logging secrets or message bodies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eppieapp/skills/eppie-email-cli)
- [Eppie CLI repository](https://github.com/Eppie-io/Eppie-CLI)
- [Eppie CLI releases](https://github.com/Eppie-io/Eppie-CLI/releases/latest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command patterns, JSON response shapes, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Favors bounded JSON output, explicit standard-input contracts, and predictable command results for agent automation.]

## Skill Version(s):

0.2.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
