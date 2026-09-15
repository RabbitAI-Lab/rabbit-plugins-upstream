## Description:

Raindrop.io helps an agent read, create, update, search, and delete Raindrop.io bookmarks and collections through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Raindrop.io bookmarks, collections, tags, and profile data from an agent session. It supports read actions directly and requires user confirmation before write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute mutable remote installer scripts directly in a shell.

Mitigation: Prefer the official installer documentation or a verified package or release before installing the oo CLI, and avoid piping downloaded scripts directly into bash or PowerShell.

Risk: Write and destructive actions can modify or delete Raindrop.io bookmarks and collections.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: The skill depends on OOMOL and the oo CLI for account connection and server-side credential handling.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL, the oo CLI, and the connected Raindrop.io account relationship.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-raindrop)
- [Raindrop.io homepage](https://raindrop.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector execution metadata when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
