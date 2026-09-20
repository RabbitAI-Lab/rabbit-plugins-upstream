## Description:

Control Spotify on Linux via MPRIS DBus. Use when: launching Spotify from command line, playing/pausing/skipping tracks, searching songs and switching playback to a specific track, any Spotify playback control task on Linux.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lxp731](https://clawhub.ai/user/lxp731)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to launch and control the Spotify desktop client on Linux through MPRIS DBus, including playback controls, Spotify URI playback, status checks, and volume control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Playback, Spotify URI, and volume commands can immediately change what is playing on the local desktop client.

Mitigation: Confirm track, album, or playlist URIs and intended volume or playback actions before execution.

Risk: Launching Spotify starts a managed background process in the user's desktop session.

Mitigation: Use the bundled launcher checks and stop command, and run only from the intended non-root desktop user session.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act on the invoking user's local Spotify desktop session.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
