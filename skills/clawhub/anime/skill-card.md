## Description: <br>
CLI for AI agents to search and look up anime information using the public Jikan API for MyAnimeList data, without authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
AI agents assisting humans use this skill to search anime titles, retrieve MyAnimeList details by MAL ID, browse current or upcoming seasons, and list top ranked anime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Anime searches are sent to the public Jikan/MyAnimeList API and may disclose user query text to a third-party service. <br>
Mitigation: Avoid using private or sensitive information in anime searches. <br>
Risk: The skill depends on an external anime CLI script and common command-line tools. <br>
Mitigation: Before installing or running it, confirm the script source is the intended publisher release and review the commands requested by the agent. <br>


## Reference(s): <br>
- [Anime skill on ClawHub](https://clawhub.ai/jeffaf/skills/anime) <br>
- [jeffaf publisher profile](https://clawhub.ai/user/jeffaf) <br>
- [Jikan API](https://jikan.moe) <br>
- [Jikan API documentation](https://docs.api.jikan.moe/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text and terminal output from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Jikan v4 rate limits of 3 requests per second and 60 requests per minute; no authentication required.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
