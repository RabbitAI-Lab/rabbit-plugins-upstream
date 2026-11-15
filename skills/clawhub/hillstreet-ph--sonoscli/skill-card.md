## Description:

Control Sonos speakers (discover/status/play/volume/group).

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

People using Sonos speakers can ask an agent to discover speakers and check status, control playback and volume, manage groups and queues, and search music services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change playback, volume, and speaker grouping on the local Sonos system.

Mitigation: Confirm the intended speaker and requested control action before running a command.

Risk: The skill instructions may not fit the user's intended setup.

Mitigation: Review the skill description and instructions before installing.

## Reference(s):

- [Sonos CLI](https://sonoscli.sh)
- [ClawHub release](https://clawhub.ai/hillstreet-ph/skills/sonoscli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act on Sonos speakers on the local network; optional Spotify Web API search requires Spotify credentials.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
