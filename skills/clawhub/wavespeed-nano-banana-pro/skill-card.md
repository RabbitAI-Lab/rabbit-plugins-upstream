## Description:

Generate and edit images with Google's Nano Banana Pro model through WaveSpeed AI, including text-to-image prompts, natural-language edits, flexible aspect ratios, 1k/2k/4k outputs, and PNG/JPEG output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to direct an agent through WaveSpeed AI setup and Nano Banana Pro image generation or image-editing runs. It is suited for creating new images from prompts, editing user-provided images, choosing output formats, and saving generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid remote service and uploads prompts plus any selected local images.

Mitigation: Confirm user intent before uploads, pass only user-provided media or prior result URLs, and avoid sending sensitive prompts or images unless the user accepts the remote-service exposure.

Risk: The setup path can rely on global npm installation or ad hoc npx execution for WaveSpeed tooling.

Mitigation: Install WaveSpeed tooling only from trusted sources, prefer pinned package versions or a project-local locked install, and avoid ad hoc npx -y execution when possible.

Risk: Stored WaveSpeed credentials could be misused if local tooling or dependencies are compromised.

Mitigation: Keep WaveSpeed credentials out of chat and rotate the stored credential if dependency compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-nano-banana-pro)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API calls, Files]

**Output Format:** [Markdown with bash command examples, parameter tables, and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When commands are executed, WaveSpeed returns prediction metadata, image URLs, and optionally downloaded PNG or JPEG image files.]

## Skill Version(s):

2.0.1 (source: server release evidence; SKILL.md frontmatter lists 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
