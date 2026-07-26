## Description: <br>
Terminal Spotify playback/search via spogo (preferred) or spotify_player. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[engahmedsalah358-lgtm](https://clawhub.ai/user/engahmedsalah358-lgtm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users who manage Spotify from a terminal use this skill to search tracks, control playback, switch devices, and configure a supported CLI client. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup can ask users to import Chrome browser cookies into a third-party CLI, which may expose Spotify session credentials if mishandled. <br>
Mitigation: Only run cookie import if you trust the CLI and accept the credential risk; prefer a separate browser profile or official OAuth/client-id flow when available, and know how to revoke Spotify sessions or remove stored CLI auth state. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/engahmedsalah358-lgtm/skills/ahmed) <br>
- [Spotify](https://www.spotify.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands assume a Spotify Premium account and either spogo or spotify_player installed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
