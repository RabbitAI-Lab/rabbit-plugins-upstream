## Description:

Helps agents operate Spotify through the OOMOL oo CLI for reading, searching, playback control, library management, and playlist changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Spotify catalog and account data, manage playlists and saved content, and control playback through an OOMOL-connected Spotify account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Use a verified package-manager or pinned installer path, and do not let an agent run installer commands automatically.

Risk: The skill brokers Spotify requests through OOMOL and can access connected account data.

Mitigation: Install only if the user trusts OOMOL with the connected Spotify account and understands the data exposure.

Risk: Write and destructive actions can change playback, playlists, follows, saved content, and library state.

Mitigation: Review exact payloads and effects before approving write actions, and require explicit approval for destructive operations.

## Reference(s):

- [ClawHub Spotify skill page](https://clawhub.ai/oomol/skills/oo-spotify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Spotify](https://spotify.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Spotify connector action names, schemas, JSON payloads, execution commands, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
