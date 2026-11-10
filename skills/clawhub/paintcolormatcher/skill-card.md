## Description:

Match any HEX/RGB color to real-world Sherwin-Williams, Benjamin Moore, and Behr paint swatches using perceptual CIEDE2000 Delta-E colorimetry and LRV lookup via PaintColorMatcher MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paintcolormatcher](https://clawhub.ai/user/paintcolormatcher)

### License/Terms of Use:

MIT-0

## Use Case:

External users can give an agent a HEX or RGB color to find visually similar paint swatches from Sherwin-Williams, Benjamin Moore, and Behr. The agent can use the matches and light reflectance value information to guide paint selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented match request sends a color and paint brand to the external PaintColorMatcher endpoint.

Mitigation: Send only color and brand values you are comfortable sharing with PaintColorMatcher.

Risk: The security evidence is incomplete because two references could not be resolved.

Mitigation: Review the service and endpoint documentation before sending data.

## Reference(s):

- [PaintColorMatcher Color Studio](https://paintcolormatcher.com)
- [HEX to Paint Swatch Converter](https://paintcolormatcher.com/hex-to-paint-color)
- [Find Paint Color from Room Photo](https://paintcolormatcher.com/find-paint-color-from-photo)
- [Sherwin-Williams LRV and Swatch Index](https://paintcolormatcher.com/sherwin-williams-paint-colors)
- [Benjamin Moore Cross-Brand Equivalents](https://paintcolormatcher.com/benjamin-moore-paint-colors)
- [Behr Paint Color Equivalents](https://paintcolormatcher.com/behr-paint-colors)
- [PaintColorMatcher MCP endpoint](https://paintcolormatcher.com/api/mcp)
- [ClawHub skill page](https://clawhub.ai/paintcolormatcher/skills/paintcolormatcher)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text describing matching paint swatches and color details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None stated]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
