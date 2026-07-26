## Description: <br>
Access Spotify listening history, top artists/tracks, and get personalized recommendations via the Spotify Web API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[braydoncoyer](https://clawhub.ai/user/braydoncoyer) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to fetch Spotify listening history, top artists, top tracks, and personalized music recommendations after one-time OAuth setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests access to Spotify listening history, top items, recommendations, and current playback data. <br>
Mitigation: Install only when those scopes are acceptable, and revoke the Spotify app authorization when the skill is no longer needed. <br>
Risk: Client secrets and OAuth tokens are stored locally and could expose Spotify account access if shared or read by another process. <br>
Mitigation: Keep the client secret and ~/.config/spotify-clawd/token.json private, avoid entering secrets while screen sharing, and delete local credentials and tokens when retiring the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/braydoncoyer/skills/spotify-history) <br>
- [Publisher Profile](https://clawhub.ai/user/braydoncoyer) <br>
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Command-line text or JSON responses with setup guidance in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Spotify account, a Spotify Developer App, OAuth authorization, and local credential/token storage.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
