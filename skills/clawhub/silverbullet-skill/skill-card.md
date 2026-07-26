## Description: <br>
Provides an MCP server for SilverBullet that lets agents read, write, search, and manage markdown pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramonitor](https://clawhub.ai/user/ramonitor) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users can connect an MCP-compatible agent to a trusted SilverBullet note-taking server to read, create, update, append, search, and delete markdown notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, change, and delete notes on the configured SilverBullet server. <br>
Mitigation: Install it only for intended SilverBullet spaces and require explicit confirmation before write, append, or delete actions. <br>
Risk: A misconfigured SILVERBULLET_URL or base_url can direct agent actions to the wrong server. <br>
Mitigation: Keep SILVERBULLET_URL and per-call base_url values pointed at the intended trusted server before allowing note operations. <br>
Risk: Outdated dependencies can increase operational or security exposure. <br>
Mitigation: Keep the skill dependencies updated as recommended by the security guidance. <br>


## Reference(s): <br>
- [SilverBullet](https://silverbullet.md) <br>
- [SilverBullet HTTP API](https://silverbullet.md/HTTP%20API) <br>
- [ClawHub Skill Page](https://clawhub.ai/ramonitor/skills/silverbullet-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/ramonitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text responses from MCP tool calls, plus configuration snippets and shell commands for setup.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool outputs may include SilverBullet page content, file metadata, server status, and error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, pyproject.toml, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
