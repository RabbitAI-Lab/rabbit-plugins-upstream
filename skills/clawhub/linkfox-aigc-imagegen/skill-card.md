## Description:

AIGC图像生成 helps agents generate or edit images from prompts and reference image URLs using LinkFox image-generation models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to ask an agent to generate image assets from one or more reference image URLs, prompt text, and model settings. It is suited for image generation, image editing, batch image outputs, and saving generated media paths for later use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to download and install an additional LinkFox onboarding skill during authentication or billing troubleshooting.

Mitigation: Review that behavior before installation and require explicit approval before downloading or installing additional skills from external URLs.

Risk: Prompts, reference image URLs, generated outputs, and task metadata may be sent to LinkFox services and stored locally.

Mitigation: Avoid confidential prompts, private image URLs, and sensitive reference images unless that data handling is acceptable for the use case.

Risk: Generated media is fetched from external URLs and saved to the local session media directory.

Mitigation: Use trusted inputs and review generated files and raw response records before reusing or sharing them.

## Reference(s):

- [AI 生图 API 参考](references/api.md)
- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen)

## Skill Output:

**Output Type(s):** [Files, JSON, Text]

**Output Format:** [Plain text stdout with saved file paths, generated image files, and JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates an asynchronous image-generation task, polls for completion for up to 10 minutes, downloads generated media locally, and stores the raw task response.]

## Skill Version(s):

1.2.0 (source: evidence.release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
