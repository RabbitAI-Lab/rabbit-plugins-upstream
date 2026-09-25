## Description:

Search MuseScore sheet music and read score metadata through a MuseScore MCP server that uses a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find MuseScore arrangements, inspect score metadata, resolve download links for free or entitled scores, and create PDFs when supported by the configured MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use the user's signed-in MuseScore browser session.

Mitigation: Install only when the musescore-mcp server and fetchproxy extension are trusted, and prefer project-local MCP configuration.

Risk: The tools can resolve download links or create PDFs for score content.

Mitigation: Request downloads or PDF creation only for scores the user is entitled to access.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with MCP tool guidance, JSON configuration examples, and links or local file paths returned by tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on a signed-in MuseScore browser tab, fetchproxy, musescore-mcp, and rsvg-convert for SVG-to-PDF conversion.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
