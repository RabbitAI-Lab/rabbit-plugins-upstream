## Description:

Guides an agent in creating looping GPT Image 2.6 GIFs from prompts or still images, choosing frame sizes, refining motion prompts, and converting results to animated WebP or MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn prompts or approved still images into looping animations for chats, social posts, and web pages, with frame sizing and conversion guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to varg and its generation providers, whose retention and access controls were not established by the supplied evidence.

Mitigation: Only submit prompts and images you are comfortable sharing with those services.

Risk: The conversion script can overwrite same-named WebP or MP4 files in its output directory.

Mitigation: Choose a dedicated output directory and check for existing files before conversion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/gpt-image-gif)
- [varg.ai how-to](https://varg.ai/how-to)
- [varg GIF guide](https://varg.ai/how-to/skills/gpt-image-gif)
- [varg MCP connection](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Animated GIF, animated WebP, MP4, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [GIF generation requires a varg account or VARG_API_KEY; local conversion requires ffmpeg and ffprobe, plus a WebP encoder for WebP output.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
