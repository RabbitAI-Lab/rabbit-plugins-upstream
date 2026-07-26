## Description: <br>
Apple Music integration via AppleScript (macOS) or MusicKit API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[epheterson](https://clawhub.ai/user/epheterson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to control Apple Music, manage playlists and libraries, search catalog or library content, and work with AppleScript or MusicKit API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents toward persistent Apple Music library changes, including playlist deletion and write actions. <br>
Mitigation: Require explicit user confirmation before delete or write actions and review proposed AppleScript or MusicKit API calls before execution. <br>
Risk: MusicKit developer tokens, user music tokens, and .p8 keys are sensitive credentials. <br>
Mitigation: Treat tokens and .p8 keys as secrets, avoid exposing them in prompts or logs, and rotate credentials if disclosure is suspected. <br>
Risk: The artifact references installing an external MCP server from an unpinned repository. <br>
Mitigation: Review and pin the referenced MCP server version before installation. <br>


## Reference(s): <br>
- [ClawHub Apple Music skill](https://clawhub.ai/epheterson/skills/mcp-applemusic) <br>
- [mcp-applemusic repository](https://github.com/epheterson/mcp-applemusic) <br>
- [Apple Developer MusicKit keys](https://developer.apple.com/account/resources/authkeys/list) <br>
- [Apple Music authorization](https://authorize.music.apple.com/woa) <br>
- [Apple Music API](https://api.music.apple.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash, AppleScript, Python, JSON, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes library-first workflow guidance, platform limitations, token handling notes, and MCP server setup examples.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 0.6.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
