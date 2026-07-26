## Description: <br>
Terminal Spotify playback/search via spogo (preferred) or spotify_player. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent provide terminal commands and configuration guidance for Spotify playback, search, device selection, and fallback use of spotify_player. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs users to import Spotify authentication cookies from Chrome, which can expose credential material if the CLI or storage location is not trusted. <br>
Mitigation: Prefer an official OAuth or device-code login when available; before using cookie import, verify where tokens are stored and how to revoke or remove them. <br>


## Reference(s): <br>
- [Spotify](https://www.spotify.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/steipete/skills/spotify-player) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires either spogo or spotify_player, and Spotify Premium for playback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
