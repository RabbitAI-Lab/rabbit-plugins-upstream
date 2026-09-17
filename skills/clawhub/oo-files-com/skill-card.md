## Description:

Files.com helps agents read, create, update, delete, download, list, and manage metadata in Files.com through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Files.com from an agent session, including folder creation, file deletion, downloads, metadata lookup, folder listing, and custom metadata updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes a remote installer command that pipes downloaded code directly to a shell.

Mitigation: Prefer a documented, versioned, verifiable oo CLI installation method or inspect the installer before execution.

Risk: The skill can run write and destructive Files.com actions.

Mitigation: Confirm exact targets and payloads with the user before creating folders, updating metadata, or deleting files and folders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-files-com)
- [Files.com homepage](https://www.files.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
