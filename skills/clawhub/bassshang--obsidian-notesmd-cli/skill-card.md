## Description:

Work with Obsidian vaults (plain Markdown notes) and automate via notesmd-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bassshang](https://clawhub.ai/user/bassshang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to help agents find, create, move, delete, and edit metadata for Markdown notes in Obsidian vaults through notesmd-cli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can modify, move, or delete notes in an Obsidian vault.

Mitigation: Verify the target vault and note paths before running move, frontmatter delete, or note delete commands, and keep backups or Obsidian sync/history enabled for important notes.

Risk: The skill depends on the third-party notesmd-cli executable.

Mitigation: Install only if you are comfortable granting notesmd-cli access to the target Obsidian vault.

## Reference(s):

- [Obsidian Help](https://help.obsidian.md)
- [ClawHub Skill Page](https://clawhub.ai/bassshang/skills/obsidian-notesmd-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires notesmd-cli and access to the target Obsidian vault.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
