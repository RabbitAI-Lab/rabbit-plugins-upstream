## Description: <br>
Access Vibo event music planning through MCP so an agent can read events, timelines, song requests, playlists, and related planning details, and can perform confirm-gated updates such as adding songs, joining events, or exporting playlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to their Vibo event music account for natural-language planning, review, playlist management, and event music updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an agent to a user's Vibo event music account and relies on sensitive authentication material. <br>
Mitigation: Install only when the vibo-mcp npm package is trusted, keep VIBO_PASSWORD, VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, and ~/.vibo-mcp/session.json out of shared files, logs, screenshots, and source control, and rotate or revoke exposed credentials. <br>
Risk: Agent actions can change event music planning data such as songs, comments, sections, event membership, and exports. <br>
Mitigation: Use the skill's confirm-gated write behavior so mutating operations are reviewed as dry-run previews before network calls are made with confirm set to true. <br>


## Reference(s): <br>
- [Vibo](https://vibodj.com) <br>
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mutating Vibo operations are confirm-gated and return dry-run previews until confirm is true.] <br>

## Skill Version(s): <br>
1.5.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
