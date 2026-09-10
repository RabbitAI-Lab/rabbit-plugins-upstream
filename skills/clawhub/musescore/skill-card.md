## Description:

Search MuseScore sheet music and read score metadata through a configured MuseScore MCP server and signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to help agents find MuseScore sheet music, inspect score metadata, resolve entitled download links, and create PDFs for free or accessible scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unaudited private MCP bundle and browser extension through a signed-in browser session.

Mitigation: Install only when the private MCP server author and fetchproxy extension are trusted, and review extension permissions before use.

Risk: A global MCP configuration can expose the tool across unrelated projects.

Mitigation: Prefer a project-scoped MCP configuration over a global configuration.

Risk: Using a normal browser profile may expose sensitive MuseScore account context to the extension and MCP workflow.

Mitigation: Use a dedicated MuseScore browser profile or account where possible, and avoid sensitive accounts until source, version pinning, and permission limits are clear.

## Reference(s):

- [musescore-mcp project link](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, files, guidance]

**Output Format:** [Markdown responses with MCP tool results, URLs, JSON configuration snippets, and optional PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured musescore-mcp server, the fetchproxy browser extension, a signed-in musescore.com browser tab, and rsvg-convert for SVG-to-PDF fallback.]

## Skill Version(s):

0.17.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
