## Description:

Make short videos through Clipwright's MCP server: an AI actor speaking your script, or a faceless video of up to 90 seconds with narration over generated scenes. Quote first for free, then start a run and collect the MP4. Clipwright returns the file and does not publish anywhere.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seocombat](https://clawhub.ai/user/seocombat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the MCP tools to turn a script or brief into a short AI-actor or narrated faceless video, review a free quote, and retrieve the generated MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting can trigger additional paid renders without the user's approval.

Mitigation: Check existing runs first; obtain and show a fresh quote, then get explicit approval before each additional render.

Risk: Retrying an uncertain paid request with a new request key can create another charge.

Mitigation: Check the existing run and preserve the original idempotency key when retrying.

Risk: Exposed service credentials or unrestricted credits can increase account impact.

Mitigation: Keep credentials private and limit available credits; pin a reviewed package version for local installation.

## Reference(s):

- [Clipwright website](https://clipwright.io/?ref=clawhub)
- [Clipwright hosted MCP server](https://mcp.clipwright.io/mcp)
- [ClawHub skill release](https://clawhub.ai/seocombat/skills/clipwright)

## Skill Output:

**Output Type(s):** [MP4 video files, Text]

**Output Format:** [MP4 video with run status and a downloadable video link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is returned to the user and is not automatically published.]

## Skill Version(s):

0.32.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
