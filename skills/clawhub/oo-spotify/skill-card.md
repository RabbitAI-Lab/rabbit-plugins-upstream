## Description:

Spotify skill for reading, creating, updating, and deleting Spotify data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search Spotify content, inspect user library and playback state, and manage playlists, saved items, follows, queues, devices, and playback through the oo CLI after the account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run the installer automatically; install or verify the CLI through a trusted method before using the skill.

Risk: Write and destructive Spotify actions can change playback, playlists, follows, saved content, queue state, or library contents.

Mitigation: Require confirmation for write actions and explicit approval for destructive actions, including the exact target and payload.

## Reference(s):

- [ClawHub Spotify Skill](https://clawhub.ai/oomol/skills/oo-spotify)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Spotify](https://spotify.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown instructions with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect connector schemas and run Spotify actions; executed actions return JSON responses.]

## Skill Version(s):

1.0.4 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
