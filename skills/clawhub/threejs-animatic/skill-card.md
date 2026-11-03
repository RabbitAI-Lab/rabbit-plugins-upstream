## Description:

Creates browser-based three.js animatics for planning multi-shot scenes, reviewing camera blocking, and rendering video references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production teams use this skill to block multi-shot scenes in 3D, refine camera and action timing, and export camera plans or rendered references for video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tampered saved settings can make the local editor run scripts that access project files.

Mitigation: Fix save protections and unsafe HTML rendering before using private projects.

Risk: Project media may be exposed to an external video-generation service during processing.

Mitigation: Upload only media approved for varg and Seedance processing.

Risk: Optional HyperFrames dependencies may change or introduce unexpected behavior.

Mitigation: Pin optional HyperFrames dependencies and isolate rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/threejs-animatic)
- [Camera language](references/camera-language.md)
- [Mannequin rig](references/mannequin-rig.md)
- [Sets and blocking](references/sets-and-blocking.md)
- [Seek-safe rendering](references/seek-safe-rendering.md)
- [Seedance video-to-video pack](references/seedance-v2v-pack.md)
- [Starter project guide](starter/README.md)
- [varg MCP](https://mcp.varg.ai/mcp)
- [Bun runtime](https://bun.sh)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration, Video]

**Output Format:** [Markdown guidance, JavaScript and TypeScript starter code, JSON camera plans, and rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a browser-based three.js starter project; video is rendered frame by frame.]

## Skill Version(s):

1.0.0 (source: evidence.release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
