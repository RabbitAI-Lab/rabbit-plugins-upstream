## Description:

Search MuseScore sheet music and read score metadata via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and music-focused agent users use this skill to search MuseScore sheet music, inspect score metadata, resolve eligible download URLs, and create PDFs through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MuseScore requests are routed through a signed-in browser session.

Mitigation: Use a browser tab limited to musescore.com and install only if that session routing is acceptable.

Risk: The skill depends on a separate private MCP server and fetchproxy extension.

Mitigation: Verify the MCP server and browser extension installation before use, and run the health check to confirm the bridge.

Risk: Generated download URLs or PDF paths may point to files the user will open or save locally.

Mitigation: Review generated download links and output paths before opening, saving, or sharing files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp repository link](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return score metadata, official download links, local PDF paths, or setup and health-check guidance.]

## Skill Version(s):

0.15.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
