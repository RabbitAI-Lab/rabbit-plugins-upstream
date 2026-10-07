## Description:

Search MuseScore sheet music, inspect score metadata, and resolve available downloads or PDFs through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for sheet music use this skill to find MuseScore arrangements, check score details and access available downloads or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external MCP server and browser extension access the signed-in MuseScore tab.

Mitigation: Review the musescore-mcp and ContextMint Bridge code or provenance before installation, and use only if comfortable granting that access.

Risk: PDF generation can write a local file despite the skill's read-only note.

Mitigation: Review the requested output path before converting or generating PDFs.

## Reference(s):

- [ContextMint Bridge source and setup](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Files]

**Output Format:** [Markdown search results, score metadata and download links; optional local PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in MuseScore tab and ContextMint Bridge; PDF conversion may write a local file.]

## Skill Version(s):

1.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
