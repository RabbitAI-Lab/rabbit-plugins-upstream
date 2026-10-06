## Description:

Helps agents search MuseScore sheet music, inspect score metadata, resolve available downloads, and create PDFs from score pages or local SVG files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for sheet music use this skill to search MuseScore scores, check score details and licenses, and obtain available download links or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser bridge can act through a signed-in MuseScore tab.

Mitigation: Use project-scoped configuration when possible, and review the MCP server and bridge code before installation.

Risk: Download links and PDF conversion go beyond read-only score lookup; conversion can write to a local path.

Mitigation: Check download access and confirm the output path before requesting PDF conversion.

## Reference(s):

- [MuseScore skill release](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with score details, links, and setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide download URLs and, when requested, write a local PDF through SVG conversion.]

## Skill Version(s):

1.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
