## Description: <br>
Spotify Player helps agents control Spotify playback on headless Linux servers through the spogo CLI using cookie-based authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to set up and control Spotify playback from remote Linux servers where a local OAuth browser callback is not practical. It provides installation, cookie configuration, playback, device, status, and troubleshooting guidance for the spogo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spotify session cookies are stored locally and can grant playback access if exposed. <br>
Mitigation: Keep ~/.config/spogo and cookie files permission-restricted, never paste or log cookie values, and remove the cookies when no longer needed. <br>
Risk: Installing spogo with an unpinned latest version can change behavior over time. <br>
Mitigation: Review or pin the upstream spogo version before installation in controlled environments. <br>
Risk: The optional browser fallback can start playback through the agent's browser profile. <br>
Mitigation: Use the fallback only when an active Spotify device is needed and confirm the agent only navigates to Spotify playback pages. <br>


## Reference(s): <br>
- [Spotify Player on ClawHub](https://clawhub.ai/shaharsha/skills/spotify-linux) <br>
- [spogo GitHub repository](https://github.com/steipete/spogo) <br>
- [Go downloads](https://go.dev/dl/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash, TOML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the spogo CLI, a Spotify Premium account, and user-provided Spotify browser cookies.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
