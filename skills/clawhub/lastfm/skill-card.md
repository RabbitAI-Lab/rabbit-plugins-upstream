## Description: <br>
Access Last.fm listening history, music stats, and discovery. Query recent tracks, top artists/albums/tracks, loved tracks, similar artists, and global charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and music-data users use this skill to have an agent query Last.fm listening history, profile statistics, discovery endpoints, and global music charts with a configured Last.fm API key and username. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query and display listening data tied to the configured Last.fm username. <br>
Mitigation: Install only for accounts whose Last.fm listening data you are comfortable exposing to the agent session. <br>
Risk: The required Last.fm API key may appear in shared logs, screenshots, or shell history if handled carelessly. <br>
Mitigation: Keep the API key out of shared outputs and rotate it if it is exposed. <br>
Risk: The skill examples use the documented Last.fm API endpoint over HTTP. <br>
Mitigation: Use HTTPS for Last.fm API URLs where supported. <br>


## Reference(s): <br>
- [Last.fm API Account Creation](https://www.last.fm/api/account/create) <br>
- [Last.fm API Documentation](https://lastfm-docs.github.io/api-docs/) <br>
- [Last.fm API Base Endpoint](http://ws.audioscrobbler.com/2.0/) <br>
- [ClawHub Skill Page](https://clawhub.ai/gumadeiras/skills/lastfm) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON query examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only Last.fm API query guidance for account-linked music data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
