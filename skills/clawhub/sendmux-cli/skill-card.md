## Description:

Use the Sendmux CLI for durable agent inbox registration, owner invites, profiles, and terminal-driven Management, Mailbox, and Sending workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to install and run the Sendmux CLI for inbox registration, profile setup, connection checks, mailbox reads, sending workflows, and account management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide commands with sensitive mailbox, sending, and account-management authority.

Mitigation: Grant only the Sendmux scopes and profiles needed for the task, use agent-readable output for review, and require explicit confirmation before destructive or email-sending commands.

Risk: The install path uses an unpinned global npm package, so installed CLI behavior may differ from the reviewed artifact.

Mitigation: Use a pinned, trusted version of @sendmux/cli where possible and avoid running npm as root or administrator.

Risk: Misconfigured credentials can expose excessive account authority or fail against the wrong API surface.

Mitigation: Use root keys only for management commands, mailbox or approved agent credentials for mailbox and sending commands, and do not ask users to paste secrets into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-cli)
- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [OAuth for REST APIs](https://sendmux.ai/docs/developer-tools/oauth)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses --json examples for agent-readable CLI output.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
