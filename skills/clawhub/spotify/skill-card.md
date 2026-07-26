## Description: <br>
Control Spotify playback on macOS. Play/pause, skip tracks, control volume, play artists/albums/playlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2mawi2](https://clawhub.ai/user/2mawi2) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent control the local Spotify desktop app on macOS, including playback, track navigation, volume, status checks, and playing Spotify artists, albums, or tracks by URI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic requests such as playing music could cause an agent to use Spotify even when the user did not explicitly choose it. <br>
Mitigation: Ask the user to confirm Spotify as the intended music service when the request does not name it. <br>
Risk: The skill controls a local macOS desktop application and may install shpotify through Homebrew. <br>
Mitigation: Use it only on macOS systems where Spotify desktop control and the Homebrew-installed spotify CLI are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/2mawi2/skills/spotify) <br>
- [Publisher profile](https://clawhub.ai/user/2mawi2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the macOS Spotify desktop app through the spotify CLI and AppleScript.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
