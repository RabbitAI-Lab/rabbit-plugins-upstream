## Description:

Operates YouTube through an OOMOL-connected account for reading, creating, updating, and deleting YouTube data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, retrieve, and manage YouTube videos, channels, playlists, comments, captions, ratings, thumbnails, and uploads through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions direct users to run remote installer scripts for the oo CLI.

Mitigation: Review the installer before running it and prefer a pinned or checksum-verified installation path.

Risk: The skill can upload, update, comment on, rate, or delete YouTube content.

Mitigation: Confirm exact payloads and targets before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-youtube)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [YouTube](https://www.youtube.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
