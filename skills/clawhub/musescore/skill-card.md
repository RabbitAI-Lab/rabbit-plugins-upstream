## Description:

Searches MuseScore sheet music and helps an agent read score metadata, license and page details, and permitted download or PDF URLs through musescore-mcp and a signed-in fetchproxy browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent search MuseScore sheet music, inspect score metadata, and resolve permitted download or PDF URLs through a configured MCP server and signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install external MCP and browser extension components that operate through a signed-in MuseScore browser session.

Mitigation: Install only trusted releases, prefer project-local MCP configuration, use a dedicated browser profile or MuseScore session, and remove the extension and MCP configuration when no longer needed.

## Reference(s):

- [musescore-mcp project link](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with JSON configuration examples and MCP tool output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local musescore-mcp, the fetchproxy browser extension, and a signed-in MuseScore browser session; download actions resolve URLs rather than streaming files through the MCP.]

## Skill Version(s):

0.17.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
