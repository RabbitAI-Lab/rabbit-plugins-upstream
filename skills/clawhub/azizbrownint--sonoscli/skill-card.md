## Description:

Control Sonos speakers (discover/status/play/volume/group).

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and home automation users use this skill to control local Sonos speakers through the `sonos` command-line tool, including discovery, playback, volume, grouping, favorites, queue management, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go install target uses a mutable `@latest` module version.

Mitigation: Pin and review a specific upstream version before installing in controlled environments.

Risk: The installed binary needs local-network access to discover and control Sonos devices.

Mitigation: Run it only where local-network access to Sonos devices is expected and approved.

Risk: Spotify search may require Spotify Web API credentials.

Mitigation: Provide Spotify credentials only when using Spotify search and handle them as secrets.

## Reference(s):

- [sonoscli homepage](https://sonoscli.sh)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/sonoscli)
- [Go install module](https://github.com/steipete/sonoscli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional Spotify credential guidance and troubleshooting advice for local-network or sandbox permission errors.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
