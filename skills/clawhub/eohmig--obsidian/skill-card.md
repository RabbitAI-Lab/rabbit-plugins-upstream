## Description:

Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to locate Obsidian vaults, search notes, create notes, and safely move or delete Markdown notes through obsidian-cli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing obsidian-cli from the third-party yakitrak/yakitrak Homebrew tap.

Mitigation: Install only after trusting the tap or reviewing the obsidian-cli source to be installed.

Risk: Move and delete operations can affect notes in the wrong vault or remove important note content.

Mitigation: Confirm the active vault and exact note path before destructive operations, and keep backups for important vaults.

## Reference(s):

- [Obsidian Help](https://help.obsidian.md)
- [ClawHub skill page](https://clawhub.ai/eohmig/skills/obsidian)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires obsidian-cli and an installed Obsidian desktop app with a working URI handler.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
