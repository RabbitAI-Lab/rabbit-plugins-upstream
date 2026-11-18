## Description:

Composite video layers with green screen chroma key, AI background removal, rotoscoping, color grading, .cube 3D LUTs, depth bokeh camera lens blur, glow, face blur, watermark removal, Bezier masks, and GPU VFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to request compositing, chroma keying, background removal, optical effects, and color finishing on a video timeline. It returns edit status and, when export completes, a URL for the rendered video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Levea account and API key, and the supplied security assessment notes that one referenced path was not resolved during scanning.

Mitigation: Review the current plugin or MCP setup and provider references before use, and provide the API key through the tool's secret configuration rather than in prompts.

## Reference(s):

- [ClawHub release](https://clawhub.ai/brajendrak00068/skills/vfx-compositing-keying)
- [Levea editing service setup](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=vfx-compositing-keying)
- [Levea API](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [API Calls, Text, Video files or export URLs]

**Output Format:** [Structured edit status and project details, with an MP4 URL when export completes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edits may return a waiting status while rendering; an exported video URL is optional.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
