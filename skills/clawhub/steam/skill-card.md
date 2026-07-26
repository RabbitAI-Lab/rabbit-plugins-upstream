## Description: <br>
Browse, filter, and discover games in a Steam library by playtime, reviews, Steam Deck compatibility, genres, and tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to inspect a configured Steam library, filter games by playtime, reviews, Steam Deck compatibility, genres, and tags, and produce game recommendations or library summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a third-party Steam CLI configured with a Steam Web API key and Steam ID. <br>
Mitigation: Use a revocable Steam Web API key, avoid sharing it in chats or logs, and revoke or remove it when no longer needed. <br>
Risk: Library queries can expose personal Steam profile and game-library information. <br>
Mitigation: Review CLI output before sharing it and avoid running the skill where Steam library details should remain private. <br>


## Reference(s): <br>
- [Steam Games CLI page](https://clawhub.ai/mjrussell/skills/steam) <br>
- [Steam CLI homepage listed in skill metadata](https://github.com/mjrussell/steam-cli) <br>
- [Steam Web API key setup](https://steamcommunity.com/dev/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI output descriptions, including table, plain text, or JSON CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the steam CLI binary and a configured Steam Web API key and Steam ID.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
