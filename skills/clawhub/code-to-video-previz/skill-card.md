## Description:

Prototype video shots with code by selecting an approach, staging scenes and cameras, evaluating frames, and preparing handoffs to video-generation models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to plan shots, build lightweight 3D or 2.5D prototypes, evaluate composition and camera movement, and prepare approved previz for video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Three.js preview server can expose files beside the selected scene to other computers.

Mitigation: Bind the server to 127.0.0.1, restrict requests to the renderer and selected scene, use a dedicated scene directory without sensitive files, and stop live previews when finished.

Risk: Footage and images sent to generation providers may be shared externally, and generation may incur charges.

Mitigation: Confirm which media may be shared with providers and approve costs before generation.

## Reference(s):

- [Staging format](references/staging-format.md)
- [Reference video workflow](references/reference-video.md)
- [Video model handoff guidance](references/handoff.md)
- [Blender guidance](references/blender.md)
- [Blender Lab MCP documentation](https://www.blender.org/lab/mcp-server/)
- [Skill release page](https://clawhub.ai/vargai/skills/code-to-video-previz)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Markdown guidance, Preview frames and clips]

**Output Format:** [Code and shell commands with JSON scene configuration, Markdown guidance, and rendered preview media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview media supports shot planning and review; human judgment remains necessary for pacing and feel.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; source SKILL.md declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
