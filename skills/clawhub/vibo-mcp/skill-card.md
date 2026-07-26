## Description: <br>
Access Vibo event music planning through an MCP server for events, timelines, song requests, playlists, guest activity, and connected music exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and event hosts use this skill to let an agent inspect and manage Vibo event music planning, including timeline sections, requested songs, playlists, guest participation, and Spotify or Apple Music exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can depend on Vibo passwords, access tokens, refresh tokens, or captured browser sessions. <br>
Mitigation: Keep `.mcp.json`, environment variables, and `~/.vibo-mcp/session.json` private, avoid committing them, and rotate Vibo credentials or sessions if exposed. <br>
Risk: Write tools can modify event songs, comments, sections, guests, notifications, and connected music exports. <br>
Mitigation: Review dry-run previews first and only rerun mutating tools with `confirm: true` when the proposed change is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp) <br>
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp) <br>
- [Vibo](https://vibodj.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON configuration snippets, tool guidance, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP tool calls that read or mutate Vibo account and event data; mutating tools are described as confirm-gated.] <br>

## Skill Version(s): <br>
1.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
