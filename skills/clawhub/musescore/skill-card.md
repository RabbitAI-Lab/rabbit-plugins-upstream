## Description:

Searches MuseScore sheet music, reads score metadata, and helps resolve download or PDF URLs through a configured MCP server and signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search MuseScore scores, inspect score metadata and licensing, and resolve download or PDF URLs when a local musescore-mcp setup and signed-in browser session are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external private MCP server and fetchproxy browser extension that can use a signed-in MuseScore browser session.

Mitigation: Install only if the MCP server and extension are trusted, prefer project-local MCP configuration, and use a dedicated browser profile or session.

Risk: Download and PDF workflows may use the user's signed-in MuseScore access and can involve free, purchased, or otherwise entitled scores.

Mitigation: Invoke the tools deliberately and confirm the score is free or that the user has appropriate access before resolving downloads or PDFs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return MuseScore metadata, official download links, or local PDF paths depending on the selected MCP tool.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
