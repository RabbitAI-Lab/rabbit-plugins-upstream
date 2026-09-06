## Description:

Search MuseScore sheet music, read score metadata, and resolve download or PDF workflows through a MuseScore MCP setup that uses a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find MuseScore arrangements, inspect score metadata such as license, pages, measures, key, parts, and duration, and work with free or entitled download and PDF paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests run through the user's signed-in MuseScore browser tab, so installing untrusted MCP or extension code could expose session-backed access.

Mitigation: Install only if the musescore-mcp and fetchproxy projects are trusted, review the MCP command path, and keep the extension limited to the intended MuseScore workflow.

Risk: Download and PDF workflows depend on whether a score is free or the user is otherwise entitled to access it.

Mitigation: Use the skill only for free or entitled scores and verify the returned license, access, and downloadability metadata before relying on the output.

## Reference(s):

- [ClawHub musescore skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with text responses, JSON configuration snippets, and MCP setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MuseScore metadata, download URLs to open in a browser, or local PDF output paths when the MCP workflow creates a PDF from SVG pages.]

## Skill Version(s):

0.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
