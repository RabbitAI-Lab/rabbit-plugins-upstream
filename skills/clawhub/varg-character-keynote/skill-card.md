## Description:

Creates an 8-second vertical keynote video in which a custom character delivers a short line with native audio and audience applause.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use it to make short keynote-style spokesperson, mascot, or character clips for speaker-style ads and social video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue, character details, and reference images are sent to external generation services.

Mitigation: Send only material you are authorized to share and review the providers’ retention practices.

Risk: Cloud rendering incurs a charge.

Mitigation: Estimate the cost and approve it before starting a render.

Risk: An exposed VARG_API_KEY could allow unauthorized API use.

Mitigation: Keep the key private and use a protected secret store or the varg MCP sign-in flow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-character-keynote)
- [varg.ai](https://varg.ai)
- [varg character keynote guide](https://varg.ai/how-to/skills/varg-character-keynote)
- [Seedance 2.5 model guide](https://varg.ai/models/seedance_2_5.md)
- [varg MCP server](https://mcp.varg.ai/mcp)
- [varg render API](https://api.varg.ai/v2/render)

## Skill Output:

**Output Type(s):** [Video file, Shell commands, Guidance]

**Output Format:** [8-second 9:16 MP4 video with spoken audio and applause, plus render instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-generated; typical 720p render cost is estimated at about $3.50.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
