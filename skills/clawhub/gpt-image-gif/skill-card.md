## Description:

Guides agents through creating and troubleshooting looping GIFs with GPT Image 2.6 on varg, including frame sizing, prompt design, and conversion to WebP or MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a still image or prompt into a looping animated GIF, tune frame count and size, troubleshoot visual issues, and convert finished GIFs to WebP or MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images are sent to varg and its processing providers, and GIF generation may incur charges.

Mitigation: Use only prompts and images you are authorized to send, and check generation costs before submitting requests.

Risk: The conversion script can replace matching WebP and MP4 files in the selected output folder.

Mitigation: Choose an output folder where those files can safely be replaced.

## Reference(s):

- [Varg how-to guide](https://varg.ai/how-to)
- [Varg MCP connection](https://mcp.varg.ai/mcp)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/gpt-image-gif)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Animated media files]

**Output Format:** [Markdown instructions with JSON request examples and Bash commands; GIF, WebP, and MP4 files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [GIF frame counts, dimensions, and timing are selected to fit documented sprite-sheet limits; WebP and MP4 conversion options include loop count, background, and quality settings.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
