## Description:

Search MuseScore sheet music and read score metadata via MCP. Triggers on phrases like "find sheet music for", "search MuseScore for", "is there a free arrangement of", "what's the license on this MuseScore score", "how many pages is", or any request involving MuseScore scores, arrangements, or sheet-music metadata. Requires musescore-mcp installed and the fetchproxy extension active with a signed-in musescore.com tab (see Setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and music-focused agents use this skill to search MuseScore scores, inspect score metadata, resolve download links, and create PDFs for scores available through an entitled signed-in MuseScore browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external MCP server and browser extension that act through a signed-in MuseScore browser tab.

Mitigation: Use project-scoped MCP configuration, review the external source and extension permissions, pin known-good versions, and avoid sensitive browser sessions while using the skill.

Risk: The ClawHub security verdict is suspicious because the release has limited auditability while relying on private external components.

Mitigation: Install only after accepting that trust boundary, and review or obtain the external components before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source referenced by the skill](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension referenced by the skill](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with MCP tool results, JSON configuration snippets, URLs, and optional local PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only for MuseScore account state; PDF files may be written locally when the SVG fallback path is used.]

## Skill Version(s):

0.17.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
