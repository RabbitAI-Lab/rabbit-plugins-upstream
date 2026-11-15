## Description:

Control Sonos speakers (discover/status/play/volume/group).

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Sonos users use this skill to have an agent issue Sonos CLI commands for discovering speakers, checking status, controlling playback and volume, managing groups, opening favorites, working with queues, and optionally searching Spotify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-issued Sonos commands can cause physical-device effects on local speakers, including playback, volume changes, grouping, queue clearing, and favorite opening.

Mitigation: Install only when speaker control is intended, and confirm speaker names or IP addresses before playback, volume, grouping, party, solo, queue clear, or favorite-open commands.

Risk: The configured Go install target uses a mutable latest version.

Mitigation: Prefer a pinned and reviewed sonoscli version when reproducible installation matters.

Risk: Spotify search may require Spotify credentials.

Mitigation: Provide Spotify credentials only when Spotify search is needed.

## Reference(s):

- [sonoscli homepage](https://sonoscli.sh)
- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/sonoscli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local Sonos speaker names or IP addresses and optional Spotify credential environment variables when Spotify search is needed.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
