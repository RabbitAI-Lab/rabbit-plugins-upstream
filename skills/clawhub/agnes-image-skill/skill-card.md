## Description:

调用 Agnes Image 2.1 Flash 生成图像，支持文生图、图生图、URL / Base64 输出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[neil-huang](https://clawhub.ai/user/neil-huang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and other external users use this skill to generate or transform images with Agnes Image 2.1 Flash. It helps an agent collect the prompt, image input, size, and output format, then call the bundled script to return an image URL or saved image file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any provided image files or URLs are sent to Agnes's remote service.

Mitigation: Avoid sending sensitive or proprietary content unless the user has reviewed Agnes's current data-handling terms and is comfortable with the remote processing.

Risk: The skill requires an Agnes API key.

Mitigation: Keep AGNES_API_KEY private, store it only in local environment configuration, and do not commit the .env file.

Risk: Image-to-image requests can use local files or external URLs.

Mitigation: Confirm the exact image source before sending it, and use only intended, accessible inputs.

## Reference(s):

- [Agnes Image 2.1 Flash documentation](https://agnes-ai.com/zh-Hans/docs/agnes-image-21-flash)
- [ClawHub skill page](https://clawhub.ai/neil-huang/skills/agnes-image-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; invoked runs return plain-text image URLs or saved image file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AGNES_API_KEY and sends prompts plus optional image inputs to Agnes's remote API.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
