## Description:

Generate and edit Seedance 2.5 videos through WaveSpeed AI from text prompts or reference media, including video extension and synchronized audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from prompts or reference media, restyle or extend existing clips, and retrieve the resulting video URLs through WaveSpeed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, videos, or audio may contain sensitive or third-party material that is uploaded for generation.

Mitigation: Only submit media you have permission to share and are comfortable sending to WaveSpeed.

Risk: Video generation and processing can incur usage charges that vary with the request.

Mitigation: Estimate the request cost and check current endpoint pricing before submission, including duration, resolution, and any input video.

Risk: An API key could be exposed if shared in chat or handled insecurely.

Mitigation: Authenticate with the documented login flow or a protected environment variable; never paste the key into chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wavespeed/skills/wavespeed-seedance-25)
- [WaveSpeed Seedance 2.5 text-to-video model](https://wavespeed.ai/models/bytedance/seedance-2.5/text-to-video)
- [WaveSpeed MCP server](https://api.wavespeed.ai/mcp)
- [WaveSpeed access key sign-in](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Video, Video URLs]

**Output Format:** [Generated video media linked by output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Duration, resolution, aspect ratio, source media, and audio vary by request.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
