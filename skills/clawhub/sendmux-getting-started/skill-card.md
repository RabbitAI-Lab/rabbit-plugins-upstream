## Description:

Set up Sendmux for agents, register a durable inbox without an existing key, link an owner, choose a runtime surface, and make the first harmless call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose the right Sendmux credential, runtime surface, package, and first connection check before using Sendmux email, mailbox, or management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package installation commands may install software from external Sendmux package sources.

Mitigation: Confirm the Sendmux package sources are trusted before running install commands.

Risk: Using a root key or broad OAuth scope for mailbox tasks can grant more access than the workflow needs.

Mitigation: Use the smallest key or OAuth scope needed, and avoid root keys for mailbox-scoped tasks.

Risk: API keys or durable agent credentials could be exposed through chat, logs, screenshots, or repo files.

Mitigation: Use environment variables, local CLI profiles, or a secret manager; rotate any key that appears in chat or logs.

Risk: Self-registration creates a durable local profile that persists until revoked.

Mitigation: Use self-registration only when appropriate and revoke the profile when it is no longer needed.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-getting-started)
- [Sendmux publisher profile](https://clawhub.ai/user/sendmux.ai)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell, text, and TypeScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-scope guidance, package selection, connection checks, and routing to related Sendmux skills.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
