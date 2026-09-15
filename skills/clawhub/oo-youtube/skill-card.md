## Description:

This skill lets agents search, read, create, update, upload, rate, comment on, and delete YouTube resources through an OOMOL-connected YouTube account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate YouTube through an authenticated OOMOL connection, including search and retrieval workflows as well as playlist, comment, caption, metadata, thumbnail, rating, and upload management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review the installer source and prefer a verified package, pinned release, checksum, or signed installer before installing the oo CLI.

Risk: The skill can perform state-changing YouTube actions, including posting, uploading, updating, rating, and playlist changes.

Mitigation: Confirm the exact target and payload with the user before running any write action.

Risk: The skill can perform destructive YouTube actions, including deleting captions, playlists, playlist items, and owned videos.

Mitigation: Require explicit approval for the specific destructive target before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-youtube)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [YouTube](https://www.youtube.com/)
- [YouTube Icon](https://static.oomol.com/logo/third-party/youtube.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces agent instructions for calling the oo CLI and interpreting JSON connector responses.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
