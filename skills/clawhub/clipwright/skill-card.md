## Description:

Create short AI actor or faceless narrated videos through Clipwright, quote before rendering, and retrieve the MP4 without publishing it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seocombat](https://clawhub.ai/user/seocombat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to connect an agent to Clipwright, quote video renders, start approved generation runs, and retrieve the resulting MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Additional troubleshooting renders can spend credits before the cost is clear.

Mitigation: Require a free quote and explicit approval before each additional render, including diagnostics.

Risk: Retrying after an uncertain paid response can start another paid render.

Mitigation: Check the existing run and preserve the original request key.

Risk: Installing an automatically updated package can introduce unreviewed changes.

Mitigation: Pin a reviewed package version for local installation.

## Reference(s):

- [Clipwright on ClawHub](https://clawhub.ai/seocombat/skills/clipwright)
- [Clipwright](https://clipwright.io/?ref=clawhub)
- [Clipwright hosted MCP server](https://mcp.clipwright.io/mcp)

## Skill Output:

**Output Type(s):** [Video files (MP4), Text]

**Output Format:** [MP4 video with textual run status and retrieval links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns the video file and does not publish it.]

## Skill Version(s):

0.35.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
