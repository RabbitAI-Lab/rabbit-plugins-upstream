## Description:

Terminal Spotify playback/search via spogo (preferred) or spotify_player.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Spotify users and agents use this skill to search tracks, control playback, select devices, check status, and configure terminal Spotify clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags spogo cookie import from Chrome as sensitive because scope, storage, and revocation are not explained in the skill.

Mitigation: Prefer spotify_player or a safer OAuth/device-login flow when available; if spogo is used, inspect the tool and tap, understand credential storage, and revoke Spotify sessions afterward.

Risk: The skill delegates Spotify playback and authentication actions to external terminal tools.

Mitigation: Install tools only from trusted sources and review proposed commands before execution.

## Reference(s):

- [Spotify](https://www.spotify.com)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/spotify-player)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require a Spotify Premium account and either spogo or spotify_player.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
