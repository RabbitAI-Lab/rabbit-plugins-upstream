## Description:

YouTube (youtube.com). Use this skill for ANY YouTube request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected YouTube account through OOMOL, including search, listing, comments, playlist management, ratings, thumbnails, captions, and video uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change YouTube account state through comments, ratings, playlist edits, metadata updates, thumbnails, captions, and uploads.

Mitigation: Confirm the exact requested action, target, and payload before approving write actions.

Risk: The skill includes destructive actions that can remove playlists, playlist items, videos, or caption tracks.

Mitigation: Require explicit approval for destructive actions and verify the target identifier before execution.

Risk: The skill depends on the oo CLI and an OOMOL-connected YouTube account.

Mitigation: Install only when OOMOL and the connected account are trusted for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-youtube)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [YouTube homepage](https://www.youtube.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
