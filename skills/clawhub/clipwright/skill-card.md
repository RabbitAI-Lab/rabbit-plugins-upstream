## Description:

Make short videos through Clipwright's MCP server: an AI actor speaking your script, or a faceless video of up to 90 seconds with narration over generated scenes. Quote first for free, then start a run and collect the MP4. Clipwright returns the file and does not publish anywhere.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seocombat](https://clawhub.ai/user/seocombat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to create short AI presenter or faceless videos from a script, then retrieve the resulting MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented local MCP setup uses an unpinned package version that could change between installs.

Mitigation: Verify the MCP package version and review the setup before installing.

Risk: The security review reports a mismatch between the stated video workflow and behavior it found, with incomplete analysis.

Mitigation: Review the setup and workflow behavior before installation; the available evidence does not establish malicious intent.

## Reference(s):

- [Clipwright documentation](https://clipwright.io/docs)
- [Clipwright API OpenAPI specification](https://api.clipwright.io/openapi.json)
- [Clipwright changelog](https://clipwright.io/changelog)
- [Clipwright MCP overview](https://clipwright.io/mcp)
- [Clipwright homepage](https://clipwright.io/?ref=clawhub)

## Skill Output:

**Output Type(s):** [MP4 video files, Text, Shell commands, Configuration]

**Output Format:** [MP4 video, with supporting text and shell or JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is up to 90 seconds; Clipwright returns the file without publishing it.]

## Skill Version(s):

0.74.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
