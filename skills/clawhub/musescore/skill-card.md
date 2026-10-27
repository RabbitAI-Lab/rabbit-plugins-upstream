## Description:

Search MuseScore sheet music, inspect score metadata, and access available score downloads through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians and other users can find sheet music, check score metadata and licensing, and retrieve available scores or PDFs through their MuseScore account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on external components and uses a signed-in MuseScore browser session.

Mitigation: Review and trust the MCP server and browser extension before installation; use a browser session you are comfortable sharing with this workflow.

Risk: Downloads or PDF conversion may write files locally, while paid scores may be gated or only partially rendered.

Mitigation: Choose an appropriate output location, check result status and page coverage, and confirm access rights before using downloaded files.

## Reference(s):

- [MuseScore skill on ClawHub](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Links, Files]

**Output Format:** [Structured score metadata and download links; optional local or inline PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Download results distinguish complete, partial, gated, and open-in-browser outcomes.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
