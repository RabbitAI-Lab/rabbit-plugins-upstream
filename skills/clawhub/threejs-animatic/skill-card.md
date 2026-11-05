## Description:

Plan, review, and render multi-shot three.js animatics with consistent sets, blocking, camera moves, and timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers and developers use the skill to block and review shots in a three.js previz, then export a camera plan and reference render for video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unprotected save feature can preserve injected scripts that execute in the review page.

Mitigation: Use a loopback-only, read-only preview until save requests are protected and camera values are validated and safely displayed.

Risk: Project media may contain material that is not authorized for sharing with varg.

Mitigation: Share project media with varg only when authorized.

Risk: The optional HyperFrames path depends on an external package that was not audited with the packaged source.

Mitigation: Pin HyperFrames when using the optional path.

## Reference(s):

- [Camera language](artifact/references/camera-language.md)
- [Sets and blocking](artifact/references/sets-and-blocking.md)
- [Mannequin rig](artifact/references/mannequin-rig.md)
- [Seek-safe rendering](artifact/references/seek-safe-rendering.md)
- [Seedance video-to-video pack](artifact/references/seedance-v2v-pack.md)
- [Look blockout](artifact/references/look-blockout.md)
- [Starter project guide](artifact/starter/README.md)
- [ClawHub release page](https://clawhub.ai/vargai/skills/threejs-animatic)
- [varg MCP service](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Code, Markdown, JSON, Shell commands, Configuration instructions, Video files, Images]

**Output Format:** [Starter project files, Markdown and JSON camera plans, rendered MP4s and still images, plus command-line instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frame-by-frame renders; optional HyperFrames path and look-blockout stills.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
