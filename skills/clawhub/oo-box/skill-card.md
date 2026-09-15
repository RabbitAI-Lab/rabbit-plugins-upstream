## Description:

Box lets an agent use an OOMOL-connected Box account to browse, search, retrieve, create, update, upload, download, and trash Box files and folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Box through an OOMOL-connected account, including reading content, managing files and folders, and performing confirmed write or trash operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Avoid running those installer commands unless the oo CLI installer source has been independently trusted and verified.

Risk: The skill can create, upload, rename, move, describe, and trash Box files or folders.

Mitigation: Review write and destructive payloads carefully, confirm the exact target and effect with the user, and require explicit approval before destructive actions.

Risk: Box actions run through an OOMOL-connected account with delegated account permissions.

Mitigation: Use only a Box account whose permissions the user is comfortable delegating to OOMOL.

## Reference(s):

- [Box Homepage](https://www.box.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Box connector JSON responses when actions are executed.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
