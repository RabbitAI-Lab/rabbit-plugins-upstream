## Description:

Prototype video shots in code, choose when a 3D previz is useful, stage and check scenes in Three.js or Blender, and prepare handoffs for video models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, filmmakers, and creative teams use this skill to block shots, preserve camera and scene continuity, inspect frames and measurements, and prepare guide clips or storyboards for a video model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unauthenticated preview server may expose files in the scene directory; the security review was incomplete, with two files only partly inspected.

Mitigation: Keep the preview server local or access-controlled, exclude sensitive files from its served directory, and review the partially inspected files before deployment.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/code-to-video-previz)
- [Staging format](references/staging-format.md)
- [Reference video workflow](references/reference-video.md)
- [Painting and still workflow](references/paintings.md)
- [Blender setup](references/blender.md)
- [Video model handoff](references/handoff.md)
- [Previz guide](https://varg.ai/how-to/previz-a-video-in-threejs-or-blender)
- [Video making guide](https://varg.ai/how-to/make-a-video-in-ten-steps)

## Skill Output:

**Output Type(s):** [Code, Configuration, Images, Video, Markdown, Shell commands, Guidance]

**Output Format:** [Scene JSON, Python or TypeScript code, checked stills or guide clips, and Markdown handoff prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deliverables vary with the shot and selected prototype workflow.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
