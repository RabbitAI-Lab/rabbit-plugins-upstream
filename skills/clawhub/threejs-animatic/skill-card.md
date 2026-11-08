## Description:

Build and review a three.js animatic with timed shots, blocked scenes, camera plans, and MP4 exports for video-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers, animators, and developers use this skill to turn a storyboard into a timed 3D previz, review camera blocking, and export a camera plan or video reference before video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local editor can store untrusted changes that may later execute scripts in the preview.

Mitigation: Use a clean, read-only preview bound to loopback until save requests are authorized and validated and saved camera fields render as text; stop the server when finished.

Risk: Optional generation sends selected clips, images, and prompts to varg/Seedance and may charge credits.

Mitigation: Review the material being shared and get approval from the person paying before sending or starting a generation run.

Risk: Browser exploitability, remote packages, and external services were not runtime-tested.

Mitigation: Pin executable dependencies and render trusted scenes in an isolated project.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/threejs-animatic)
- [Varg MCP endpoint](https://mcp.varg.ai/mcp)
- [Camera language guide](references/camera-language.md)
- [Seek-safe rendering guide](references/seek-safe-rendering.md)
- [Seedance video-to-video guide](references/seedance-v2v-pack.md)
- [Sets and blocking guide](references/sets-and-blocking.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Configuration, Shell commands]

**Output Format:** [Project files, Markdown camera plans, JSON exports, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific; may include a browser preview, stills, or an MP4 animatic.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
