## Description: <br>
Controls Spotify playback from Linux command-line sessions with search, playback, status, and device commands for an active Spotify account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shawnpana](https://clawhub.ai/user/shawnpana) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill to prepare commands for searching Spotify, confirming the intended track, and controlling playback on an existing Spotify device. It is intended for Linux environments with Spotify Premium and configured Spotify developer credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installation guidance asks users to install an unprovided Spotify command with sudo and system-wide permissions. <br>
Mitigation: Review the actual spotify script before installing it and prefer a user-local install path instead of system-wide installation. <br>
Risk: Spotify client credentials are stored in a local config file without explicit permission guidance. <br>
Mitigation: Restrict the config file permissions, such as chmod 600 ~/.config/spotify-cli/config, and treat the client secret as sensitive. <br>
Risk: The dependency installation example uses --break-system-packages, which can affect the system Python environment. <br>
Mitigation: Prefer an isolated virtual environment or pipx for installing Python dependencies. <br>


## Reference(s): <br>
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) <br>
- [Spotify Web Player](https://open.spotify.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes search-first guidance so an agent can ask for user confirmation before playback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
