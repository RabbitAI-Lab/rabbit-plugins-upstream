## Description:

Set up and use 1Password CLI for sign-in, desktop integration, and reading or injecting secrets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to install and authenticate the 1Password CLI, choose an authentication mode, and read or inject secrets from command workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious and identifies an example that prints a database password without masking.

Mitigation: Review the example before use; do not run it in a way that exposes the password in terminal output or logs.

Risk: The security scan was partial because a local path-like reference could not be resolved.

Mitigation: Check the referenced setup material and confirm the unresolved reference before relying on the skill.

## Reference(s):

- [1Password CLI get started](https://developer.1password.com/docs/cli/get-started/)
- [1Password CLI get-started notes](references/get-started.md)
- [1Password CLI examples](references/cli-examples.md)
- [1Password ClawHub release](https://clawhub.ai/hillstreet-ph/skills/1password)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
