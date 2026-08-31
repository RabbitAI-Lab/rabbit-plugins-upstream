## Description:

Files.com (files.com). Use this skill for ANY Files.com request - reading, creating, updating, and deleting data. Whenever a task involves Files.com, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected Files.com account through OOMOL for folder listing, metadata lookup, file download, folder creation, metadata updates, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create folders or update Files.com metadata in the connected account.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: The destructive delete action can remove a Files.com file or folder path.

Mitigation: Require explicit user approval for the target path before running delete_file.

Risk: The skill operates a user's Files.com account through OOMOL-connected credentials.

Mitigation: Install only when the agent is intended to operate Files.com through OOMOL, and review write, delete, and metadata payloads carefully before approval.

## Reference(s):

- [ClawHub Files.com Skill Page](https://clawhub.ai/oomol/skills/oo-files-com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Files.com Homepage](https://www.files.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
