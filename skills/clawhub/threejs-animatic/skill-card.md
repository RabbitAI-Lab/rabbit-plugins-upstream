## Description:

Build a three.js animatic to review camera, blocking, timing, and look before rendering a video reference for video-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to turn a storyboard into a reviewable 3D previz, camera plan, and reference clip for video-to-video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unpinned package commands.

Mitigation: Review package names and versions, and pin dependencies before running package commands.

Risk: The starter involves project edits and browser-run HTML and scripts.

Mitigation: Inspect the files and changes, and run the starter in a disposable project with an isolated browser profile.

Risk: The workflow can send reference media to an external generation service.

Mitigation: Confirm the destination and obtain approval for each asset before uploading; use only media approved for that service.

Risk: The security analysis was partial and does not establish that every component is safe.

Mitigation: Review the release and its dependencies before installation, following the security guidance in the release evidence.

## Reference(s):

- [Camera language](artifact/references/camera-language.md)
- [Sets and blocking](artifact/references/sets-and-blocking.md)
- [Mannequin rig](artifact/references/mannequin-rig.md)
- [Seek-safe rendering](artifact/references/seek-safe-rendering.md)
- [Seedance video-to-video pack](artifact/references/seedance-v2v-pack.md)
- [Look blockout](artifact/references/look-blockout.md)
- [ClawHub release page](https://clawhub.ai/vargai/skills/threejs-animatic)
- [varg MCP endpoint](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Markdown guidance with JavaScript, TypeScript, and JSON project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a camera plan, review stills, and an MP4 animatic reference clip.]

## Skill Version(s):

1.0.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
