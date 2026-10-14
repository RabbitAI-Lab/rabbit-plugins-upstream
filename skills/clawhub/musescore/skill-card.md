## Description:

Search MuseScore sheet music, inspect score metadata, and obtain download links or PDFs through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians, educators, and developers can find sheet music, check score details and licensing, and retrieve available download links or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external server and browser extension use a signed-in MuseScore tab.

Mitigation: Install only if comfortable with session-backed access; review the extension and limit the session's exposure.

Risk: PDF conversion can write files locally despite the skill's read-only description.

Mitigation: Review and constrain output paths before using PDF conversion tools.

## Reference(s):

- [musescore skill on ClawHub](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge releases (setup)](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Score metadata and download links as text; optional local PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free-only search by default; PDF conversion can write to a specified path.]

## Skill Version(s):

1.1.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
