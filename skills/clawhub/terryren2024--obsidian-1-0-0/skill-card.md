## Description:

Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terryren2024](https://clawhub.ai/user/terryren2024)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Obsidian users can use this skill to locate vaults, search notes, create notes, move or rename notes, delete notes, and choose safer direct Markdown edits when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delete or bulk-edit operations can remove or alter important notes if the wrong vault or note path is targeted.

Mitigation: Confirm the active vault and target note path first, keep backups or version control for important vaults, and prefer move or archive workflows when possible.

Risk: The skill depends on obsidian-cli from a third-party Homebrew tap.

Mitigation: Install only when the Homebrew tap and package source are trusted for the deployment environment.

## Reference(s):

- [Obsidian Help](https://help.obsidian.md)
- [ClawHub Skill Page](https://clawhub.ai/terryren2024/skills/obsidian-1-0-0)
- [Publisher Profile](https://clawhub.ai/user/terryren2024)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local vault paths, Obsidian configuration files, and obsidian-cli commands.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
