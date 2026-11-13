## Description:

Creates short two-character podcast and dialogue videos with consistent AI-generated characters, spoken audio, an HTML storyboard, and a stitched MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a short dialogue and character references into a two-host podcast, interview, debate, or explainer video. It generates consistent scene images and short spoken clips, then prepares an HTML storyboard and a stitched MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends character images and scripts to an external generation service, and the security guidance notes no reported privacy warning.

Mitigation: Get permission to use the images and scripts, avoid sensitive material, and review the service's privacy terms before uploading.

Risk: The security summary notes image generation capability broader than the skill's stated video workflow.

Mitigation: Review requested prompts and generated images to confirm they fit the intended task.

Risk: The security guidance identifies an unpinned package installation command.

Mitigation: Review the package and install command before running it, and use a pinned release when available.

Risk: The security guidance says the scan is partial because two referenced local paths could not be resolved.

Mitigation: Inspect referenced local files and related skills before installation or execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-podcast-video)
- [Varg](https://varg.ai)
- [Varg MCP server](https://mcp.varg.ai/mcp)
- [Varg API](https://api.varg.ai/v2)

## Skill Output:

**Output Type(s):** [Video files, HTML files, Shell commands, Guidance]

**Output Format:** [MP4 video, HTML storyboard, and Markdown scripts with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenes are generated as short clips and assembled into a single video; spoken audio may be generated with the video.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
