## Description:

Builds code-based three.js animatics from storyboards, with staged sets, posed mannequins, and shot cameras, then reviews, plans, and renders the blocking for video-to-video reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to turn a multi-shot storyboard into a reviewable 3D blockout, camera plan, and animatic render before video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a risky local save endpoint.

Mitigation: Review the local save behavior and destination before use, especially in workspaces containing sensitive files.

Risk: The security summary reports unpinned command-line tools.

Mitigation: Review tool sources and versions before running commands, and pin versions where repeatable builds matter.

Risk: The security guidance flags external media sharing.

Mitigation: Check which media will be uploaded or shared and confirm it is appropriate for the selected service.

Risk: The security analysis is incomplete.

Mitigation: Treat scan coverage as partial and review the skill's instructions and commands before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/threejs-animatic)
- [Camera language guide](artifact/references/camera-language.md)
- [Look blockout guide](artifact/references/look-blockout.md)
- [Mannequin rig guide](artifact/references/mannequin-rig.md)
- [Seedance video-to-video pack guide](artifact/references/seedance-v2v-pack.md)
- [Seek-safe rendering guide](artifact/references/seek-safe-rendering.md)
- [Sets and blocking guide](artifact/references/sets-and-blocking.md)
- [Varg MCP service](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [JavaScript and TypeScript source, JSON and Markdown camera plans, shell commands, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a rendered animatic, camera plans, and still previews.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
