## Description: <br>
Search MuseScore sheet music and read score metadata via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and musicians use this skill to search MuseScore scores, inspect score metadata, resolve eligible downloads, and create PDFs through a configured MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes MuseScore requests through a signed-in browser session and a separate browser extension. <br>
Mitigation: Install only if you trust the musescore-mcp server and fetchproxy extension, and are comfortable using the active browser session for these requests. <br>
Risk: Global MCP configuration can expose the tool outside the intended project. <br>
Mitigation: Prefer project-local MCP configuration when possible. <br>
Risk: PDF generation may write to a local output path. <br>
Mitigation: Review the requested output path before generating PDFs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return MuseScore metadata, download URLs, healthcheck guidance, and PDF output path guidance depending on the invoked MCP tool.] <br>

## Skill Version(s): <br>
0.15.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
