## Description: <br>
Terminal Spotify playback/search via spogo (preferred) or spotify_player. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nabssku](https://clawhub.ai/user/nabssku) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to control Spotify playback, search tracks, manage devices, and configure terminal Spotify clients with spogo or spotify_player. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow recommends importing Chrome browser cookies into spogo, which may expose Spotify session credentials. <br>
Mitigation: Install only trusted Spotify CLI tools, prefer OAuth or device-login authentication when available, and confirm where imported credentials are stored and how to revoke them before using cookie import. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nabssku/skills/spongo) <br>
- [Spotify](https://www.spotify.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Spotify Premium account and either spogo or spotify_player.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
