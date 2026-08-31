## Description:

Search MuseScore sheet music and read score metadata via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, musicians, and agents use this skill to search MuseScore for sheet music, inspect score metadata, check license and downloadability details, and resolve entitled score downloads or PDFs through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a signed-in MuseScore browser tab through the fetchproxy extension and an external MCP server.

Mitigation: Use project-level MCP configuration, keep the browser tab limited to musescore.com, and verify the private musescore-mcp and fetchproxy sources before use.

Risk: Downloads and PDF generation depend on free or entitled score access and MuseScore-exposed download data.

Mitigation: Check score license, free/downloadable/access flags, and entitlement before opening download links or generating PDFs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source](https://github.com/chrischall/musescore-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP tool names, JSON configuration examples, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MuseScore score metadata, official download URLs, PDF paths, and healthcheck results when the MCP server is configured.]

## Skill Version(s):

0.16.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
