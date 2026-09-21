## Description:

Use the Sendmux CLI for durable agent inbox registration, owner invites, profiles, and terminal-driven Management, Mailbox, and Sending workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install and operate the Sendmux CLI for profile setup, OAuth checks, durable agent inbox registration, owner invitations, mailbox workflows, and sending workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through mailbox access, email sending, and management actions using Sendmux credentials.

Mitigation: Use scoped mailbox or agent tokens where possible, keep root keys limited to management setup, and review email sends and management changes before execution.

Risk: Local profiles may persist credentials until logout or revocation.

Mitigation: Use named profiles deliberately, run logout or revoke credentials when access is no longer needed, and avoid exposing secrets in chat or command arguments.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [OAuth for REST APIs](https://sendmux.ai/docs/developer-tools/oauth)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommends --json for agent-readable command output and environment variables for credentials.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
