## Description:

Set up and use 1Password CLI for sign-in, desktop integration, and reading or injecting secrets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure 1Password CLI authentication modes and run secret read, injection, and troubleshooting workflows through an agent. It is intended for environments where the user already has a 1Password subscription and wants agent guidance without exposing secrets unnecessarily.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to print or write real secrets through 1Password CLI examples.

Mitigation: Review commands before execution, prefer `op run` or `op inject`, and avoid examples that print secrets or write private keys/configs unless strict permissions, cleanup, and logging controls are in place.

Risk: Using the skill gives the agent access to the user's 1Password CLI context.

Mitigation: Install and use it only when that access is acceptable, verify `op whoami` before secret reads, and scope access with service accounts, account selection, or vault permissions where possible.

## Reference(s):

- [1Password CLI Get Started](https://developer.1password.com/docs/cli/get-started/)
- [Get Started Reference](references/get-started.md)
- [CLI Examples Reference](references/cli-examples.md)
- [ClawHub Skill Page](https://clawhub.ai/azizbrownint/skills/1password)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that access a user's local 1Password CLI context; commands should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
