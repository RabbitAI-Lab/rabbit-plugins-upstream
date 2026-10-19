## Description:

Search MuseScore sheet music, inspect score metadata, and resolve downloads or create PDFs through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for sheet music can search MuseScore, inspect score details and licensing, obtain available download links, and create PDFs from rendered pages when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP server and browser extension use a signed-in MuseScore session.

Mitigation: Install only if comfortable with that access; review the server and extension source or release provenance before use.

Risk: PDF tools can write files even though the skill notes describe it as read-only.

Mitigation: Review PDF output paths and treat conversions as file-writing operations.

## Reference(s):

- [musescore ClawHub listing](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Links, Files]

**Output Format:** [Score metadata and download URLs as text; optional local PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an external MCP server and browser bridge connected to a signed-in MuseScore tab; PDF conversion can write local files.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
