## Description:

Composite video layers with green screen chroma key (Keylight spill suppression), AI background removal without green screen, rotoscoping, color grading, .cube 3D LUTs, depth bokeh camera lens blur, glow, face blur, watermark removal, Bezier masks, and 328 GPU VFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creative developers use this skill to describe compositing, keying, masking, optical effects, and color-finishing edits for video projects. It sends the requested edit to the Levea editing service and can return project status and an exported MP4 link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Levea API key to access the external editing service.

Mitigation: Store LEVEA_API_KEY in the plugin or MCP server's secret configuration and avoid sharing it in prompts or public files.

Risk: Security scan coverage is incomplete because one local reference could not be matched to a bundled artifact.

Mitigation: Review the skill's referenced material before installation when assurance about the full content is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/brajendrak00068/skills/vfx-compositing-keying)
- [Levea editing service](https://livecore.ai/)
- [Levea API endpoint](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [API Calls, Guidance]

**Output Format:** [Structured editing requests and project status data, with an MP4 URL when export completes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Levea account and API key; output may include a project ID, verification report, and exported video URL.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
