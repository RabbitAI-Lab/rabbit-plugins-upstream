## Description:

Set up and use 1Password CLI (op) for installing the CLI, enabling desktop app integration, signing in, and reading, injecting, or running secrets via op.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to prepare authenticated 1Password CLI sessions and safely retrieve, inject, or run commands with secrets from a 1Password account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example commands can expose real secrets in terminal output, tmux pane captures, or agent logs.

Mitigation: Avoid commands that print secrets, use --no-masking, or read private keys to stdout; keep captures away from secret-producing output.

Risk: Secret material can be persisted into repository files when examples write credentials or injected configuration to disk.

Mitigation: Prefer passing secrets directly to the intended command with op run or op inject, and do not write generated secret-bearing files into a repo.

Risk: Using the skill authorizes access to a real 1Password account.

Mitigation: Use it only in sessions where the user is comfortable granting vault access and verify authorization with op whoami before any secret read.

## Reference(s):

- [1Password CLI get-started](https://developer.1password.com/docs/cli/get-started/)
- [get-started.md](references/get-started.md)
- [cli-examples.md](references/cli-examples.md)
- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/1password)
- [Publisher profile](https://clawhub.ai/user/aperdigaokbk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the op binary and a user-authorized 1Password account before secret reads can succeed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
