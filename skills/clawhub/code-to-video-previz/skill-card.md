## Description:

Prototype video shots in Three.js or Blender, check staging and camera movement, and prepare guide clips for video-generation models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to decide whether a shot needs previz, stage camera and action in 3D, review the resulting frames, and prepare a guide clip or handoff for video-generation tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The live Three.js preview server could expose unrelated private project files to other devices on the network.

Mitigation: Use the Blender rendering path until the Three.js server binds explicitly to localhost and serves only required files. Keep confidential material outside served directories and stop live previews when finished.

Risk: External services, dependencies, and network reachability are outside this security review.

Mitigation: Approve the specific media and provider before external generation, prefer a reviewed installer version, and treat network reachability as untested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/code-to-video-previz)
- [Publisher profile](https://clawhub.ai/user/vargai)
- [Staging format](artifact/references/staging-format.md)
- [Blender setup](artifact/references/blender.md)
- [Reference video workflow](artifact/references/reference-video.md)
- [Video handoff guidance](artifact/references/handoff.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Rendered images and video, Guidance, Shell commands]

**Output Format:** [JSON scene files, Three.js or Blender scripts, rendered stills and MP4 guide clips, with Markdown guidance and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected renderer determines local tool requirements; the Three.js path needs Bun, Chrome, ffmpeg, and network access for its jsDelivr import.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
