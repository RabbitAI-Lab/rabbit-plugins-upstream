## Description:

Use the Sendmux CLI for durable agent inbox registration, owner invites, profiles, and terminal-driven Management, Mailbox, and Sending workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to register agent inboxes, manage Sendmux profiles and accounts, read mail, and send email through the terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, OAuth tokens, stored profiles, and mailbox contents may expose sensitive information.

Mitigation: Use scoped credentials and protected local profiles; do not paste secrets into chat or expose them in command arguments.

Risk: Sending email or changing account settings may have unintended consequences.

Mitigation: Confirm email-sending and account-changing actions before running them, and require explicit confirmation for destructive commands.

## Reference(s):

- [Sendmux CLI skill on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-cli)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux OAuth for REST APIs](https://sendmux.ai/docs/developer-tools/oauth)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples can request JSON-formatted CLI responses.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; skill frontmatter lists 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
