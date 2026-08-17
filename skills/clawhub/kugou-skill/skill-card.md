## Description:

Kugou is an agent skill for searching songs, generating recommendations, viewing charts and listening activity, managing favorites and playlists, and controlling the local Kugou desktop player when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shamo88](https://clawhub.ai/user/shamo88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent interact with Kugou Music through CLI commands for music discovery, account-backed listening data, playlist workflows, and optional PC/Mac player control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store Kugou account login state and access personal music history, favorites, and listening statistics.

Mitigation: Install only when account connection is acceptable, review authentication prompts, and log out or remove local login state when access is no longer needed.

Risk: The skill can control a local PC/Mac Kugou player, including playback and queue changes.

Mitigation: Use player-control commands only after an explicit user request and prefer non-disruptive playback modes when the current queue should be preserved.

Risk: The update workflow includes a force-upgrade path for a globally installed npm package.

Mitigation: Require explicit approval before running global update commands and prefer update checks before installation changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shamo88/skills/kugou-skill)
- [Authentication commands](artifact/references/auth.md)
- [Music commands](artifact/references/music.md)
- [Desktop player control commands](artifact/references/control.md)
- [Output format guidance](artifact/references/output-format.md)
- [Error handling](artifact/references/error-handling.md)
- [Install commands](artifact/references/install.md)
- [Update commands](artifact/references/update.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and JSON-derived music results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Song results should include Markdown playback links; recommendation responses may include concise recommendation rationale.]

## Skill Version(s):

0.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
