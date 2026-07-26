## Description: <br>
Search MuseScore sheet music and read score metadata via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, music researchers, and agents use this skill to search MuseScore for sheet music, inspect score metadata, resolve download URLs, and create PDFs for free or entitled scores when the required local MCP setup is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MuseScore-related requests may be handled through this skill and may use the user's MuseScore browser session when the runtime is configured that way. <br>
Mitigation: Install only in workspaces where MuseScore browsing and metadata lookup through that session is acceptable, and keep the signed-in MuseScore tab under user control. <br>
Risk: Broad activation wording within the MuseScore domain may route general MuseScore score, arrangement, or sheet-music metadata requests through the skill. <br>
Mitigation: Review agent routing before deployment and limit use to MuseScore sheet-music workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, files] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return MuseScore metadata, official download URLs, or a local PDF path for SVG-to-PDF fallback; depends on a configured musescore-mcp server and fetchproxy browser extension.] <br>

## Skill Version(s): <br>
0.14.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
