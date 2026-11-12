## Description:

Work with Obsidian vaults as plain Markdown notes and automate common vault tasks with notesmd-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and automation agents use this skill to find, create, move, edit metadata for, and delete notes in Obsidian vaults through a command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install an unpinned third-party CLI dependency.

Mitigation: Vet or pin the Homebrew dependency before installing it in a trusted environment.

Risk: The skill can change, move, or delete Obsidian notes and update links across a vault.

Mitigation: Use it only with vaults the agent is allowed to access, keep backups or version control, and require explicit confirmation before delete, move, or bulk link updates.

## Reference(s):

- [Obsidian Help](https://help.obsidian.md)
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/obsidian)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose direct edits to local Markdown notes and Obsidian vault metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
