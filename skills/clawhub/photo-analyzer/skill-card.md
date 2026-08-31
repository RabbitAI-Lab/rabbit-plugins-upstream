## Description:

Analyzes an uploaded photograph, provides detailed feedback on exposure, focus, composition, lighting, and suggests concrete camera settings and shooting technique.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickliu54](https://clawhub.ai/user/nickliu54)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate uploaded photographs and receive practical feedback on exposure, focus, composition, lighting, camera settings, and shooting technique. When supported by the agent environment, it can also guide generation of a simulated improved version of the photo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded photos may contain personal or sensitive content and may be shared with an image-analysis or image-generation model depending on implementation.

Mitigation: Review model routing and data-handling behavior before use, and avoid submitting sensitive photos unless the deployment environment permits it.

Risk: The included artifact files are mostly placeholders, so real analysis and simulation behavior may be limited until implemented.

Mitigation: Treat generated recommendations as guidance and review any concrete analysis, post-processing, or image-generation implementation before deployment.

## Reference(s):

- [Reference Documentation for Photo Analyzer](references/api_reference.md)
- [ClawHub Skill Page](https://clawhub.ai/nickliu54/skills/photo-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with optional code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommendations for camera settings, shooting technique, post-processing, and optional image-simulation steps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
