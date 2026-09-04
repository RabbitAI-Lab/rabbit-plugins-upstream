## Description:

Use the Sendmux CLI for durable agent inbox registration, owner invites, profiles, and terminal-driven Management, Mailbox, and Sending workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure Sendmux CLI profiles, register durable agent inboxes, and run Management, Mailbox, and Sending workflows from a terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and mailbox credentials may grant access to account, mailbox, or sending workflows.

Mitigation: Use scoped mailbox or agent tokens where possible, avoid pasting secrets into chat, and reserve root keys for management commands.

Risk: The skill can guide actions that send mail or change account resources.

Mitigation: Require explicit confirmation for destructive or externally visible actions, and prefer idempotency keys and --json output for auditable CLI runs.

Risk: Durable agent inbox profiles can retain mailbox read access while the registration remains active.

Mitigation: Review profile storage and revocation behavior before registering a durable agent inbox; use full registration revocation when read access and delegated tokens must be removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-cli)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI examples favor --json for agent-readable output.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
