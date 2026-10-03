## Description:

Search MuseScore sheet music, inspect score metadata, and resolve available downloads or PDFs through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians and developers use this skill to find MuseScore arrangements, check score metadata and licenses, and access available download links or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on external server code and a browser extension outside the reviewed artifact.

Mitigation: Review and trust both components before installing or using them.

Risk: MuseScore requests use a signed-in browser tab through the extension.

Mitigation: Use only a browser session you intend to share with these components and review their access before connecting.

Risk: PDF conversion can write a file to a local path.

Mitigation: Confirm the output path and intended file write before running PDF conversion.

## Reference(s):

- [MuseScore skill on ClawHub](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Links, PDF files]

**Output Format:** [Structured score metadata, download URLs, or a local PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Download URLs open in a browser; the SVG fallback can write a PDF to a local path.]

## Skill Version(s):

1.1.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
