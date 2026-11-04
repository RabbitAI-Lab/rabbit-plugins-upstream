## Description:

Generate and edit AI images with ByteDance's Seedream models through Atlas Cloud, supporting text-to-image, image editing, sequential batch generation, up to 4K output, PNG output, and prompt optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xixihhhh](https://clawhub.ai/user/xixihhhh)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, designers, and developers use this skill to generate, edit, upload reference images for, and batch-produce AI visuals through Atlas Cloud using Seedream model variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, and uploaded local images are sent to Atlas Cloud for generation or editing.

Mitigation: Use only non-confidential prompts and images, and confirm the destination service before uploading or editing user-provided files.

Risk: Atlas Cloud API usage may bill the user's account, and the API key grants access to all models available on that account.

Mitigation: Confirm model choice, expected number of outputs, and cost-sensitive batch settings before running paid generation requests.

Risk: The upload command accepts arbitrary local file paths.

Mitigation: Review each local path before upload and prefer sandboxed input and output directories.

Risk: The skill includes broad activation language and generic model control beyond a narrowly scoped Seedream-only workflow.

Mitigation: Confirm that the user intends Atlas Cloud image generation and explicitly verify any non-Seedream model choice.

## Reference(s):

- [Project homepage from ClawHub metadata](https://github.com/AtlasCloudAI/nano-banana-2-skill)
- [ClawHub skill page](https://clawhub.ai/xixihhhh/skills/seedream)
- [Atlas Cloud](https://www.atlascloud.ai)
- [fal.ai Seedream 5.0 reference](https://fal.ai/seedream-5.0)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown guidance with shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download one or more JPEG or PNG image files to a user-selected output directory.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
